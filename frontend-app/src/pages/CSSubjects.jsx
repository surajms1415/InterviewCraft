import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { Link } from 'react-router-dom';

const CSSubjects = () => {
    const [topics, setTopics] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        // Bypassing API fetch due to backend startup issues. Data fetched from WCode.
        const wcodeData = [
            {
                "id": "os", 
                "title": "Operating Systems", 
                "description": "Dive deep into Operating Systems. OS Fundamentals, Process Management, Memory Management, and Interview Questions."
            },
            {
                "id": "dbms", 
                "title": "DBMS", 
                "description": "Master Database Management Systems and SQL. Database fundamentals, ACID properties, normalization, keys, ER diagrams, relational algebra."
            },
            {
                "id": "cn", 
                "title": "Computer Networks", 
                "description": "Complete CN notes with OSI, TCP/IP, protocols. Learn network layers, routing protocols, and prepare for CN interviews."
            },
            {
                "id": "oop", 
                "title": "Object Oriented Programming", 
                "description": "Master OOPs with inheritance, polymorphism, design patterns, encapsulation, and abstractions."
            }
        ];
        setTopics(wcodeData);
        setLoading(false);
    }, []);

    return (
        <div className="max-w-6xl mx-auto py-12 relative z-10">
            <h1 className="text-4xl md:text-5xl font-display font-extrabold mb-10 text-transparent bg-clip-text bg-gradient-to-r from-primary to-secondary drop-shadow-[0_0_10px_rgba(59,130,246,0.3)]">Core CS Subjects</h1>
            
            {loading ? (
                <div className="flex justify-center"><div className="animate-spin h-10 w-10 border-4 border-primary border-t-transparent rounded-full shadow-[0_0_15px_rgba(59,130,246,0.5)]"></div></div>
            ) : (
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                    {topics.map((topic, i) => (
                        <motion.div 
                            initial={{ opacity: 0, y: 20 }}
                            animate={{ opacity: 1, y: 0 }}
                            transition={{ delay: i * 0.1 }}
                            key={topic.id} 
                            className="glass-card p-8 flex flex-col hover:-translate-y-2 hover:shadow-[0_0_30px_rgba(59,130,246,0.2)] transition-all group relative overflow-hidden"
                        >
                            <div className="absolute top-0 right-0 w-32 h-32 bg-primary/10 rounded-full blur-3xl group-hover:bg-primary/20 transition-all pointer-events-none"></div>
                            <h2 className="text-3xl font-display font-bold mb-3 text-white group-hover:text-primary transition-colors relative z-10">{topic.title}</h2>
                            <p className="text-gray-400 mb-8 leading-relaxed flex-1 relative z-10">{topic.description}</p>
                            <Link to={`/subjects/${topic.id}`} className="btn-secondary w-max mt-auto relative z-10 group-hover:border-primary/50 group-hover:bg-white/10">
                                Read Full Guide
                            </Link>
                        </motion.div>
                    ))}
                </div>
            )}
        </div>
    );
};

export default CSSubjects;
