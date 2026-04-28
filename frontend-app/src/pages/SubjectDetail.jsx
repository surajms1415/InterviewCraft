import React from 'react';
import { useParams, Link } from 'react-router-dom';
import { motion } from 'framer-motion';
import { ArrowLeft, BookOpen, ChevronRight } from 'lucide-react';
import csNotes from '../data/cs_notes.json';

const SubjectDetail = () => {
    const { id } = useParams();
    const subject = csNotes[id];

    if (!subject) {
        return (
            <div className="text-center py-20">
                <h2 className="text-3xl font-display font-bold text-white">Subject Not Found</h2>
                <Link to="/subjects" className="text-primary mt-4 inline-block hover:underline drop-shadow-[0_0_8px_rgba(59,130,246,0.5)]">Return to Subjects</Link>
            </div>
        );
    }

    return (
        <div className="max-w-6xl mx-auto py-12 relative z-10">
            <Link to="/subjects" className="inline-flex items-center text-gray-400 hover:text-primary font-medium mb-8 transition-colors hover:drop-shadow-[0_0_8px_rgba(59,130,246,0.5)]">
                <ArrowLeft className="w-4 h-4 mr-2" /> Back to Core Subjects
            </Link>
            
            <motion.div initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} className="glass-card p-10 mb-12 border-l-4 border-l-primary relative overflow-hidden">
                <div className="absolute top-0 right-0 w-64 h-64 bg-primary/10 rounded-full blur-[80px] pointer-events-none"></div>
                <div className="flex items-center gap-4 mb-6 relative z-10">
                    <div className="p-4 bg-primary/20 text-primary rounded-2xl border border-primary/20 shadow-[0_0_15px_rgba(59,130,246,0.2)]">
                        <BookOpen className="w-8 h-8" />
                    </div>
                    <h1 className="text-4xl md:text-5xl font-display font-extrabold text-white tracking-tight">{subject.title}</h1>
                </div>
                <p className="text-lg text-gray-300 leading-relaxed max-w-4xl relative z-10 font-light">{subject.description}</p>
            </motion.div>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {subject.topics?.map((topic, index) => (
                    <motion.div 
                        key={topic.id}
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ delay: index * 0.1 }}
                        className="glass-card p-8 hover:-translate-y-2 hover:shadow-[0_0_30px_rgba(59,130,246,0.15)] transition-all group flex flex-col relative overflow-hidden"
                    >
                        <div className="absolute top-0 right-0 w-24 h-24 bg-primary/5 rounded-full blur-2xl group-hover:bg-primary/20 transition-all pointer-events-none"></div>
                        <h3 className="text-2xl font-display font-bold text-white mb-3 truncate group-hover:text-primary transition-colors relative z-10">
                            {topic.title}
                        </h3>
                        <p className="text-sm text-gray-400 mb-8 flex-1 line-clamp-3 leading-relaxed relative z-10">
                            {topic.description}
                        </p>
                        <Link 
                            to={`/subjects/${id}/${topic.id}`}
                            className="inline-flex items-center text-sm font-semibold text-primary group-hover:text-blue-400 mt-auto relative z-10 drop-shadow-[0_0_5px_rgba(59,130,246,0)] group-hover:drop-shadow-[0_0_8px_rgba(59,130,246,0.5)] transition-all"
                        >
                            Study Topic <ChevronRight className="w-4 h-4 ml-1 group-hover:translate-x-2 transition-transform" />
                        </Link>
                    </motion.div>
                ))}
            </div>
            
            <div className="mt-16 text-center text-gray-500 text-sm font-light">
                Content systematically extracted and curated for PrepForge AI candidates.
            </div>
        </div>
    );
};

export default SubjectDetail;
