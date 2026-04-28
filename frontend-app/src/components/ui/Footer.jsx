import React from 'react';
import profilePic from '../../assets/image.jpeg';

const Footer = () => {
  return (
    <footer className="w-full py-10 mt-10 border-t border-gray-800/50 bg-[#0a0a0f] flex flex-col items-center justify-center relative overflow-hidden">
      {/* Background Glow */}
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-64 h-64 bg-purple-600/10 rounded-full blur-[100px] pointer-events-none"></div>
      
      <div className="relative z-10 flex flex-col items-center group cursor-default">
        {/* Profile Image with Glow */}
        <div className="relative mb-4">
          <div className="absolute -inset-1 bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 rounded-full opacity-40 blur-md group-hover:opacity-75 transition duration-500"></div>
          <img 
            src={profilePic} 
            alt="Suraj M S" 
            className="relative w-24 h-24 rounded-full object-cover border-2 border-gray-800/80 shadow-2xl z-10"
          />
        </div>

        {/* Name */}
        <h3 className="text-2xl font-bold text-white tracking-wide mb-1">
          Suraj M S
        </h3>

        {/* Title */}
        <p className="text-[#a5b4fc] font-medium tracking-wider text-sm uppercase">
          Founder & Developer
        </p>
      </div>
    </footer>
  );
};

export default Footer;
