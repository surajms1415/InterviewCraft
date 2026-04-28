import React, { useState } from 'react';
import { Play, Send, User, Bot, AlertCircle } from 'lucide-react';

export default function MockInterview() {
  const [sessionActive, setSessionActive] = useState(false);
  const [messages, setMessages] = useState([]);
  const [inputText, setInputText] = useState('');
  const [loading, setLoading] = useState(false);

  const startSession = () => {
    setLoading(true);
    // Mock API Delay
    setTimeout(() => {
      setSessionActive(true);
      setMessages([
        { role: 'bot', text: 'Hello! I will be conducting your technical interview today. Can you start by designing a scalable URL shortener like bit.ly?' }
      ]);
      setLoading(false);
    }, 1500);
  };

  const handleSend = (e) => {
    e.preventDefault();
    if (!inputText.trim()) return;
    
    const newMsgs = [...messages, { role: 'user', text: inputText }];
    setMessages(newMsgs);
    setInputText('');
    setLoading(true);

    setTimeout(() => {
       setMessages([...newMsgs, { 
         role: 'bot', 
         text: "That's a good start. How would you handle collisions if two different long URLs hash to the same shortened 7-character string?" 
       }]);
       setLoading(false);
    }, 2000);
  };

  return (
    <div className="flex flex-col h-[calc(100vh-6rem)] animate-fade-in max-w-4xl mx-auto">
      <header className="mb-6 flex justify-between items-end">
        <div>
           <h1 className="text-3xl font-display font-bold text-white">Mock Interview</h1>
           <p className="text-gray-400 mt-1">Real-time technical drilling with AI.</p>
        </div>
        {!sessionActive && (
          <button onClick={startSession} disabled={loading} className="btn-primary flex items-center gap-2">
            <Play size={18} />
            {loading ? 'Connecting...' : 'Start Session'}
          </button>
        )}
      </header>

      {!sessionActive ? (
         <div className="flex-1 glass-card p-10 flex flex-col items-center justify-center text-center">
            <div className="w-20 h-20 bg-primary/10 rounded-full flex items-center justify-center mb-6">
                <Bot size={40} className="text-primary" />
            </div>
            <h2 className="text-2xl font-bold mb-3">Ready when you are!</h2>
            <p className="text-gray-400 max-w-md mx-auto mb-8">
               You are about to start a 15-minute simulated technical interview for an SDE role. 
               The AI will evaluate your answers and dynamically generate follow-up questions.
            </p>
            <div className="bg-yellow-500/10 border border-yellow-500/20 text-yellow-500 px-4 py-3 rounded-xl flex gap-3 text-sm max-w-md text-left">
               <AlertCircle className="shrink-0 mt-0.5" size={18} />
               <p>Avoid searching for answers during this mock. The goal is to identify your weak points.</p>
            </div>
         </div>
      ) : (
         <div className="flex-1 glass-card flex flex-col overflow-hidden relative">
            <div className="flex-1 overflow-y-auto p-6 space-y-6">
               {messages.map((m, i) => (
                  <div key={i} className={`flex gap-4 ${m.role === 'user' ? 'flex-row-reverse' : ''}`}>
                     <div className={`w-10 h-10 rounded-full flex items-center justify-center shrink-0 ${m.role === 'bot' ? 'bg-primary/20 text-primary' : 'bg-secondary/20 text-secondary'}`}>
                        {m.role === 'bot' ? <Bot size={20} /> : <User size={20} />}
                     </div>
                     <div className={`p-4 rounded-2xl max-w-[80%] ${m.role === 'bot' ? 'bg-white/5 border border-white/5 rounded-tl-none' : 'bg-primary rounded-tr-none text-white'}`}>
                        {m.text}
                     </div>
                  </div>
               ))}
               {loading && (
                 <div className="flex gap-4">
                     <div className="w-10 h-10 rounded-full flex items-center justify-center shrink-0 bg-primary/20 text-primary">
                        <Bot size={20} />
                     </div>
                     <div className="p-4 rounded-2xl bg-white/5 border border-white/5 rounded-tl-none flex gap-1 items-center h-[52px]">
                        <div className="w-2 h-2 bg-primary rounded-full animate-bounce" style={{animationDelay: '0ms'}}></div>
                        <div className="w-2 h-2 bg-primary rounded-full animate-bounce" style={{animationDelay: '150ms'}}></div>
                        <div className="w-2 h-2 bg-primary rounded-full animate-bounce" style={{animationDelay: '300ms'}}></div>
                     </div>
                  </div>
               )}
            </div>
            
            <form onSubmit={handleSend} className="p-4 border-t border-white/10 bg-white/5 relative z-10">
               <div className="relative">
                  <input 
                    type="text" 
                    value={inputText}
                    onChange={e => setInputText(e.target.value)}
                    placeholder="Type your answer here..."
                    className="w-full bg-background/50 border border-white/10 rounded-xl pl-4 pr-12 py-4 text-white focus:outline-none focus:ring-2 focus:ring-primary backdrop-blur-md"
                    disabled={loading}
                  />
                  <button 
                    type="submit" 
                    disabled={!inputText.trim() || loading}
                    className="absolute right-2 top-2 bottom-2 w-10 bg-primary rounded-lg flex items-center justify-center text-white disabled:opacity-50 transition-opacity hover:bg-primary/80"
                  >
                     <Send size={18} />
                  </button>
               </div>
            </form>
         </div>
      )}
    </div>
  );
}
