import React from 'react';
import { useParams, Link } from 'react-router-dom';
import { motion } from 'framer-motion';
import { ArrowLeft, CheckCircle2, ChevronRight, HelpCircle } from 'lucide-react';
import csNotes from '../data/cs_notes.json';

const TopicDetail = () => {
    const { id, topicId } = useParams();
    const subject = csNotes[id];
    const topic = subject?.topics?.find(t => t.id === topicId);

    if (!topic) {
        return (
            <div className="text-center py-20">
                <h2 className="text-3xl font-display font-bold text-white">Topic Not Found</h2>
                <Link to={`/subjects/${id}`} className="text-primary mt-4 inline-block hover:underline drop-shadow-[0_0_8px_rgba(59,130,246,0.5)]">Return to {subject?.title || 'Subjects'}</Link>
            </div>
        );
    }

    const renderCard = (card, index) => {
        if (card.type === 'text' || card.type === 'list') {
            return (
                <motion.div 
                    key={index}
                    initial={{ opacity: 0, scale: 0.98 }}
                    animate={{ opacity: 1, scale: 1 }}
                    transition={{ delay: index * 0.1 }}
                    className="glass-card p-8 mb-8 border-l-4 border-l-primary relative overflow-hidden"
                >
                    <div className="absolute top-0 right-0 w-48 h-48 bg-primary/5 rounded-full blur-[60px] pointer-events-none"></div>
                    <h2 className="text-2xl font-display font-bold text-white mb-6 flex items-center gap-3 relative z-10">
                         <CheckCircle2 className="w-6 h-6 text-primary drop-shadow-[0_0_8px_rgba(59,130,246,0.8)]" /> {card.heading}
                    </h2>
                    <div 
                        className="text-gray-300 leading-relaxed space-y-4 whitespace-pre-line relative z-10 font-light"
                        dangerouslySetInnerHTML={{ __html: card.content.replace(/\*\*(.*?)\*\*/g, '<strong class="text-white font-semibold">$1</strong>').replace(/\*(.*?)\*/g, '<em class="text-gray-200 italic">$1</em>') }}
                    />
                </motion.div>
            );
        }

        if (card.type === 'table') {
            return (
                <motion.div 
                    key={index}
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: index * 0.1 }}
                    className="glass-card mb-8 overflow-hidden border border-white/10"
                >
                    <div className="p-8 border-b border-white/10 bg-white/5">
                        <h2 className="text-2xl font-display font-bold text-white flex items-center gap-2">
                            {card.heading}
                        </h2>
                    </div>
                    <div className="overflow-x-auto">
                        <table className="w-full text-left border-collapse">
                            <thead>
                                <tr className="bg-primary/10 border-b border-white/10">
                                    {card.headers.map((h, i) => (
                                        <th key={i} className="py-4 px-6 font-semibold text-white whitespace-nowrap">{h}</th>
                                    ))}
                                </tr>
                            </thead>
                            <tbody className="divide-y divide-white/5">
                                {card.rows.map((row, i) => (
                                    <tr key={i} className="hover:bg-white/5 transition-colors">
                                        {row.map((cell, j) => (
                                            <td key={j} className="py-4 px-6 text-gray-300 align-top font-light">
                                                {cell}
                                            </td>
                                        ))}
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>
                </motion.div>
            );
        }

        if (card.type === 'faq') {
            return (
                <motion.div 
                    key={index}
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: index * 0.1 }}
                    className="glass-card p-8 mb-8 relative overflow-hidden"
                >
                    <div className="absolute inset-0 bg-gradient-to-br from-secondary/5 to-primary/5 pointer-events-none"></div>
                    <h2 className="text-2xl font-display font-bold mb-8 flex items-center gap-3 text-secondary drop-shadow-[0_0_10px_rgba(139,92,246,0.3)] relative z-10">
                        <HelpCircle className="w-6 h-6" /> {card.heading}
                    </h2>
                    <div className="space-y-6 relative z-10">
                        {card.questions.map((q, i) => (
                            <div key={i} className="bg-surface rounded-2xl p-6 border border-white/10 hover:border-secondary/30 transition-colors shadow-lg">
                                <h4 className="text-lg font-semibold mb-3 text-white">{q.q}</h4>
                                <p className="text-gray-400 leading-relaxed font-light">{q.a}</p>
                            </div>
                        ))}
                    </div>
                </motion.div>
            );
        }
        return null;
    };

    return (
        <div className="max-w-4xl mx-auto py-12 relative z-10">
            <div className="flex items-center text-sm font-medium mb-10 text-gray-500">
                <Link to="/subjects" className="hover:text-primary transition-colors">Subjects</Link>
                <ChevronRight className="w-4 h-4 mx-2" />
                <Link to={`/subjects/${id}`} className="hover:text-primary transition-colors">{subject.title}</Link>
                <ChevronRight className="w-4 h-4 mx-2" />
                <span className="text-white drop-shadow-[0_0_5px_rgba(255,255,255,0.3)]">{topic.title}</span>
            </div>
            
            <div className="mb-12 relative">
                <div className="absolute -left-10 top-10 w-32 h-32 bg-primary/20 rounded-full blur-[80px] pointer-events-none"></div>
                <h1 className="text-4xl md:text-5xl font-display font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-white to-gray-400 mb-6 tracking-tight">{topic.title}</h1>
                <p className="text-xl text-gray-400 max-w-2xl font-light leading-relaxed">{topic.description}</p>
            </div>

            <div className="space-y-4">
                {topic.cards.map((card, idx) => renderCard(card, idx))}
            </div>
            
            <div className="mt-16 mb-8 flex justify-center">
                <Link to={`/subjects/${id}`} className="btn-secondary inline-flex items-center">
                    <ArrowLeft className="w-4 h-4 mr-2" /> Back to {subject.title} Curriculum
                </Link>
            </div>
        </div>
    );
};

export default TopicDetail;
