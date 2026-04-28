import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import gdData from '../data/gd_notes.json';

const GDModule = () => {
    const [topics, setTopics] = useState([]);
    
    useEffect(() => {
        setTopics(gdData);
    }, []);

    return (
        <div className="max-w-5xl mx-auto py-12 relative z-10">
            <h1 className="text-4xl md:text-5xl font-display font-extrabold mb-6 text-transparent bg-clip-text bg-gradient-to-r from-secondary to-primary tracking-tight drop-shadow-[0_0_10px_rgba(139,92,246,0.3)]">Group Discussion Hub</h1>
            <p className="text-xl text-gray-400 mb-10 max-w-3xl font-light leading-relaxed">Master the art of communication. Review high-impact perspectives and structured pitches for highly discussed GD topics, and learn how to speak effectively.</p>
            
            <div className="glass-card bg-secondary/10 border-secondary/30 rounded-3xl p-8 mb-12 shadow-[0_0_30px_rgba(139,92,246,0.1)]">
                <h3 className="text-2xl font-display font-bold mb-4 flex items-center gap-3 text-white drop-shadow-[0_0_8px_rgba(255,255,255,0.3)]">💡 How to Speak</h3>
                <ul className="list-disc ml-6 space-y-3 text-gray-300 font-light">
                    <li><strong className="text-white font-medium">Starting:</strong> "I'd like to initiate the discussion by stating..."</li>
                    <li><strong className="text-white font-medium">Adding:</strong> "Adding to what [Name] said, I believe..."</li>
                    <li><strong className="text-white font-medium">Handling Interruptions:</strong> "Please allow me to finish my point..."</li>
                    <li><strong className="text-white font-medium">Concluding:</strong> "To summarize the group's consensus..."</li>
                </ul>
            </div>

            <div className="space-y-8">
                {topics.map((topic, i) => (
                    <motion.div 
                        initial={{ opacity: 0, x: -20 }}
                        animate={{ opacity: 1, x: 0 }}
                        transition={{ delay: i * 0.1 }}
                        key={topic.id} 
                        className="glass-card p-8 border border-white/10 relative overflow-hidden group hover:border-primary/30 transition-colors"
                    >
                        <div className="absolute top-0 right-0 w-64 h-64 bg-primary/5 rounded-full blur-[80px] pointer-events-none group-hover:bg-primary/10 transition-all"></div>
                        <h2 className="text-3xl font-display font-bold mb-6 text-white relative z-10">{topic.topic}</h2>
                        
                        {topic.perspective && (
                            <div className="mb-8 p-5 bg-primary/20 border-l-4 border-primary rounded-r-xl relative z-10">
                                <p className="text-sm font-bold text-primary uppercase tracking-wider mb-2 drop-shadow-[0_0_5px_rgba(59,130,246,0.5)]">Overall Perspective</p>
                                <p className="text-gray-300 italic font-light leading-relaxed">{topic.perspective}</p>
                            </div>
                        )}
                        
                        <div className="space-y-4 relative z-10">
                            {topic.pitches && topic.pitches.map((pitch, idx) => (
                                <div key={idx} className="bg-surface p-6 rounded-2xl border border-white/10 hover:border-white/20 transition-colors shadow-md">
                                    <h3 className="text-xl font-semibold text-white mb-3">{pitch.title}</h3>
                                    <p className="text-gray-400 leading-relaxed font-light">{pitch.content}</p>
                                </div>
                            ))}
                        </div>
                    </motion.div>
                ))}
            </div>
        </div>
    );
};

export default GDModule;
