import React from 'react';
import { motion } from 'framer-motion';
import { Link } from 'react-router-dom';
import { BookOpen, Users, Briefcase, MessageSquare, ArrowRight } from 'lucide-react';

const FeatureCard = ({ title, description, icon: Icon, link, color }) => (
    <motion.div whileHover={{ y: -5, scale: 1.02 }} className="glass-card p-6 flex flex-col items-start hover:shadow-[0_0_30px_rgba(255,255,255,0.1)] transition-all group cursor-pointer relative overflow-hidden">
        <div className={`absolute top-0 right-0 w-32 h-32 opacity-20 blur-3xl rounded-full ${color} mix-blend-screen pointer-events-none`}></div>
        <div className={`p-4 rounded-xl mb-4 ${color} bg-opacity-20 border border-white/10 backdrop-blur-md`}>
            <Icon className={`w-8 h-8 text-white drop-shadow-[0_0_8px_rgba(255,255,255,0.8)]`} />
        </div>
        <h3 className="text-xl font-display font-bold text-white mb-2 group-hover:text-primary transition-colors">{title}</h3>
        <p className="text-gray-400 mb-6 flex-1 text-sm leading-relaxed">{description}</p>
        <Link to={link} className="text-primary font-semibold flex items-center gap-2 group-hover:gap-3 transition-all">
            Start Prep <ArrowRight className="w-4 h-4"/>
        </Link>
    </motion.div>
);

const Home = () => {
  return (
    <div className="space-y-20 py-12 pb-24 relative">
        {/* Ambient background glow */}
        <div className="absolute top-0 left-1/2 -translate-x-1/2 w-full max-w-3xl h-64 bg-primary/20 blur-[100px] rounded-full pointer-events-none"></div>

        <section className="text-center max-w-4xl mx-auto space-y-8 relative z-10">
            <motion.div initial={{ opacity: 0, scale: 0.9 }} animate={{ opacity: 1, scale: 1 }} transition={{ duration: 0.5 }}>
                <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-surface border border-white/10 text-primary text-sm font-medium mb-6 shadow-[0_0_15px_rgba(59,130,246,0.2)]">
                    <span className="w-2 h-2 rounded-full bg-primary animate-pulse"></span> Platform Active
                </div>
            </motion.div>

            <motion.h1 
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                className="text-5xl md:text-7xl font-display font-extrabold text-white tracking-tight leading-tight"
            >
                Master Your Interviews with <span className="text-transparent bg-clip-text bg-gradient-to-r from-primary via-blue-400 to-secondary drop-shadow-[0_0_15px_rgba(59,130,246,0.5)]">AI Precision</span>
            </motion.h1>
            <motion.p 
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.1 }}
                className="text-xl text-gray-300 max-w-2xl mx-auto font-light leading-relaxed"
            >
                Your personalized placement assistant. Learn core subjects, simulate group discussions, and face AI-driven technical and HR mock interviews.
            </motion.p>
        </section>

        <section className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 relative z-10">
            <FeatureCard title="CS Core Subjects" description="Master OS, DBMS, CN, and OOPS with structured notes." icon={BookOpen} link="/subjects" color="bg-blue-500" />
            <FeatureCard title="Group Discussions" description="Learn frameworks, tips, and simulate real GD scenarios." icon={Users} link="/gd" color="bg-indigo-500" />
            <FeatureCard title="HR Interviews" description="Upload a resume & GitHub to generate tailored HR questions." icon={Briefcase} link="/hr" color="bg-purple-500" />
            <FeatureCard title="AI Chatbot Help" description="Stuck somewhere? Ask our AI expert for instant clarification." icon={MessageSquare} link="/chatbot" color="bg-teal-500" />
        </section>
        

    </div>
  );
};

export default Home;
