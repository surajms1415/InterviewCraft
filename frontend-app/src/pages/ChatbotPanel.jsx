import React, { useState } from 'react';
import { Send, FileDown } from 'lucide-react';
import { motion } from 'framer-motion';
import ReactMarkdown from 'react-markdown';

const ChatbotPanel = ({ msgs, setMsgs, history, setHistory }) => {
    const [query, setQuery] = useState('');
    const [loading, setLoading] = useState(false);
    const [apiKey, setApiKey] = useState('');

    React.useEffect(() => {
        const savedKey = localStorage.getItem('gemini_api_key');
        if (savedKey) setApiKey(savedKey);
    }, []);

    const handleApiKeyChange = (e) => {
        const val = e.target.value;
        setApiKey(val);
        localStorage.setItem('gemini_api_key', val);
    };

    const askChatbot = async () => {
        if (!query.trim()) return;
        
        const newMsgs = [...msgs, { role: 'user', text: query }];
        setMsgs(newMsgs);
        setLoading(true);
        setQuery('');

        try {
            const apiUrl = import.meta.env.VITE_API_URL || 'http://localhost:8000';
            const res = await fetch(`${apiUrl}/api/chat`, {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ query: newMsgs[newMsgs.length-1].text, history: history, api_key: apiKey })
            });
            const data = await res.json();
            
            if (data.response && data.response.includes('API Key limit')) {
                alert("API Key limit reached. Please provide a new API key to continue.");
            } else if (data.response && data.response.includes('provide a valid Gemini API Key')) {
                alert(data.response);
            }
            
            // Format history for gemini
            const updatedHistory = [
                ...history, 
                { role: "user", parts: [newMsgs[newMsgs.length-1].text] },
                { role: "model", parts: [data.response] }
            ];
            
            setHistory(updatedHistory);
            setMsgs([...newMsgs, { role: 'model', text: data.response }]);
            setLoading(false);
        } catch (e) {
            console.error(e);
            setLoading(false);
            setMsgs([...newMsgs, { role: 'model', text: 'Sorry, I am facing an issue right now.' }]);
        }
    };

    const downloadLog = async () => {
        if (history.length === 0) return alert('No chat to export yet.');
        try {
            const apiUrl = import.meta.env.VITE_API_URL || 'http://localhost:8000';
            const res = await fetch(`${apiUrl}/api/export`, {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(history)
            });
            const blob = await res.blob();
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'chat_export.docx';
            document.body.appendChild(a);
            a.click();
            a.remove();
        } catch (e) {
             console.error("Export failed", e);
        }
    };

    const markdownComponents = {
        strong: ({node, ...props}) => <span className="font-bold text-white" {...props} />,
        p: ({node, ...props}) => <p className="mb-2 last:mb-0" {...props} />,
        ul: ({node, ...props}) => <ul className="list-disc pl-5 my-2 space-y-1 text-gray-300" {...props} />,
        ol: ({node, ...props}) => <ol className="list-decimal pl-5 my-2 space-y-1 text-gray-300" {...props} />,
        li: ({node, ...props}) => <li className="text-gray-300" {...props} />,
        h1: ({node, ...props}) => <h1 className="text-xl font-bold mt-4 mb-2 text-white" {...props} />,
        h2: ({node, ...props}) => <h2 className="text-lg font-bold mt-4 mb-2 text-white" {...props} />,
        h3: ({node, ...props}) => <h3 className="text-md font-bold mt-3 mb-2 text-white" {...props} />
    };

    return (
        <div className="max-w-4xl mx-auto py-8 h-[calc(100vh-100px)] flex flex-col relative z-10">
            <div className="flex justify-between items-center mb-6">
                <h1 className="text-4xl font-display font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-primary to-secondary drop-shadow-[0_0_10px_rgba(59,130,246,0.3)]">AI Chatbot Assistant</h1>
                <button 
                   onClick={downloadLog} 
                   className="btn-secondary flex items-center gap-2 py-2"
                >
                   <FileDown className="w-5 h-5"/> Export to Word
                </button>
            </div>

            <div className="mb-6 relative">
                <input 
                    type="password" 
                    value={apiKey}
                    onChange={handleApiKeyChange}
                    placeholder="Enter your Gemini API Key..."
                    className="input-field shadow-[0_0_15px_rgba(255,255,255,0.05)]"
                />
            </div>

            <div className="glass-card flex-1 flex flex-col overflow-hidden border border-white/10 relative">
                <div className="absolute inset-0 bg-gradient-to-b from-primary/5 to-secondary/5 pointer-events-none"></div>
                
                <div className="flex-1 p-6 overflow-y-auto space-y-6 relative z-10 scrollbar-thin scrollbar-thumb-white/10 scrollbar-track-transparent">
                    {msgs.map((log, i) => (
                        <motion.div initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} key={i} className={`flex ${log.role === 'user' ? 'justify-end' : 'justify-start'}`}>
                            <div className={`max-w-[80%] p-5 rounded-2xl leading-relaxed shadow-lg ${log.role === 'user' ? 'bg-primary/80 border border-primary/50 text-white rounded-tr-sm shadow-[0_0_15px_rgba(59,130,246,0.3)]' : 'bg-surface border border-white/10 text-gray-200 rounded-tl-sm'}`}>
                                {log.role === 'user' ? (
                                    <div className="whitespace-pre-wrap">{log.text}</div>
                                ) : (
                                    <ReactMarkdown components={markdownComponents}>
                                        {log.text}
                                    </ReactMarkdown>
                                )}
                            </div>
                        </motion.div>
                    ))}
                    {loading && (
                        <div className="flex justify-start">
                             <div className="bg-surface border border-white/10 text-gray-400 p-4 rounded-2xl rounded-tl-sm text-sm italic flex items-center gap-2">
                                <span className="flex gap-1">
                                    <motion.span animate={{ opacity: [0,1,0] }} transition={{ repeat: Infinity, duration: 1.5, delay: 0 }}>.</motion.span>
                                    <motion.span animate={{ opacity: [0,1,0] }} transition={{ repeat: Infinity, duration: 1.5, delay: 0.2 }}>.</motion.span>
                                    <motion.span animate={{ opacity: [0,1,0] }} transition={{ repeat: Infinity, duration: 1.5, delay: 0.4 }}>.</motion.span>
                                </span>
                                AI is thinking...
                             </div>
                        </div>
                    )}
                </div>

                <div className="p-4 border-t border-white/10 bg-white/5 flex gap-3 relative z-10">
                    <input 
                        type="text" 
                        value={query}
                        onChange={(e) => setQuery(e.target.value)}
                        onKeyDown={(e) => e.key === 'Enter' && askChatbot()}
                        className="input-field"
                        placeholder="Ask me anything..."
                    />
                    <button onClick={askChatbot} disabled={loading} className="btn-primary py-3 px-6 shadow-md disabled:shadow-none flex-shrink-0">
                        <Send className="w-5 h-5" />
                    </button>
                </div>
            </div>
        </div>
    );
};

export default ChatbotPanel;
