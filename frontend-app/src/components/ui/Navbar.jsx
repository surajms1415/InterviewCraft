import React from 'react';
import { Link } from 'react-router-dom';
import { BookOpen, Users, Briefcase, MessageSquare, BriefcaseBusiness } from 'lucide-react';

const Navbar = () => {
  return (
    <nav className="bg-surface backdrop-blur-xl border-b border-white/10 sticky top-0 z-50">
      <div className="container mx-auto px-4 py-3 flex justify-between items-center">
        <Link to="/" className="flex items-center space-x-2 group">
           <BriefcaseBusiness className="w-8 h-8 text-primary group-hover:text-blue-400 transition-colors drop-shadow-[0_0_10px_rgba(59,130,246,0.3)]" />
           <span className="text-xl font-display font-bold text-white tracking-tight">
             PrepForge <span className="text-transparent bg-clip-text bg-gradient-to-r from-primary to-secondary">AI</span>
           </span>
        </Link>
        <div className="hidden md:flex space-x-6 items-center">
          <Link to="/subjects" className="text-gray-300 hover:text-white flex items-center gap-1 font-medium transition-all hover:drop-shadow-[0_0_8px_rgba(255,255,255,0.5)]">
            <BookOpen className="w-4 h-4"/> CS Subjects
          </Link>
          <Link to="/gd" className="text-gray-300 hover:text-white flex items-center gap-1 font-medium transition-all hover:drop-shadow-[0_0_8px_rgba(255,255,255,0.5)]">
            <Users className="w-4 h-4"/> Group Discussion
          </Link>
          <Link to="/hr" className="text-gray-300 hover:text-white flex items-center gap-1 font-medium transition-all hover:drop-shadow-[0_0_8px_rgba(255,255,255,0.5)]">
            <Briefcase className="w-4 h-4"/> HR Interview
          </Link>
          <Link to="/chatbot" className="btn-primary flex items-center gap-2">
            <MessageSquare className="w-4 h-4"/> AI Chatbot
          </Link>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
