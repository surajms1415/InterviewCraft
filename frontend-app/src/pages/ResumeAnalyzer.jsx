import React, { useState } from 'react';
import { UploadCloud, CheckCircle2, AlertTriangle, FileText } from 'lucide-react';

export default function ResumeAnalyzer() {
  const [file, setFile] = useState(null);
  const [analyzing, setAnalyzing] = useState(false);
  const [results, setResults] = useState(null);

  const handleUpload = (e) => {
    e.preventDefault();
    if (!file) return;
    setAnalyzing(true);
    // Mock API Call delay
    setTimeout(() => {
      setResults({
        atsScore: 78,
        skills: ['React', 'Python', 'FastAPI', 'PostgreSQL', 'Tailwind CSS'],
        weaknesses: ['Lacks quantifiable metrics in Project 1', 'Missing active verbs like "Spearheaded" or "Led"'],
        suggestions: ['Quantify your impact (e.g., "Increased performance by 20%").', 'Add a clear summary at the top.']
      });
      setAnalyzing(false);
    }, 2000);
  };

  return (
    <div className="space-y-8 animate-fade-in max-w-4xl mx-auto">
      <header className="text-center mb-12">
        <div className="w-16 h-16 bg-gradient-to-br from-secondary to-primary rounded-2xl flex items-center justify-center mx-auto mb-6 shadow-lg shadow-primary/20">
            <FileText size={32} className="text-white" />
        </div>
        <h1 className="text-4xl font-display font-bold text-white">AI Resume Analyzer</h1>
        <p className="text-gray-400 mt-3 text-lg">Upload your resume to get instant ATS scoring and improvement suggestions.</p>
      </header>

      {!results && (
        <form onSubmit={handleUpload} className="glass-card p-10 flex flex-col items-center justify-center border-dashed border-2 border-primary/50 relative overflow-hidden group">
            <div className="absolute inset-0 bg-primary/5 group-hover:bg-primary/10 transition-colors z-0"></div>
            
            <UploadCloud size={64} className="text-primary mb-6 relative z-10 group-hover:-translate-y-2 transition-transform duration-300" />
            
            <h2 className="text-xl font-bold mb-2 relative z-10">Select your resume to upload</h2>
            <p className="text-gray-400 mb-8 relative z-10">Supported formats: PDF (Max 5MB)</p>
            
            <input 
              type="file" 
              accept=".pdf" 
              className="hidden" 
              id="resume-upload" 
              onChange={(e) => setFile(e.target.files[0])}
            />
            
            <label htmlFor="resume-upload" className="btn-secondary cursor-pointer relative z-10 mb-4 inline-block">
              {file ? file.name : "Browse Files"}
            </label>

            {file && (
                <button type="submit" disabled={analyzing} className="btn-primary w-64 relative z-10 mt-4 h-12 flex items-center justify-center">
                    {analyzing ? (
                        <>
                           <div className="w-5 h-5 border-2 border-white/30 border-t-white rounded-full animate-spin mr-3"></div>
                           Analyzing...
                        </>
                    ) : (
                        "Generate Score"
                    )}
                </button>
            )}
        </form>
      )}

      {results && (
        <div className="space-y-8 animate-slide-up">
           <div className="glass-card p-8 flex flex-col md:flex-row items-center gap-8 justify-between relative overflow-hidden">
               <div className="absolute top-0 right-0 w-64 h-64 bg-primary/20 blur-3xl rounded-full translate-x-1/2 -translate-y-1/2"></div>
               <div>
                   <h2 className="text-2xl font-display font-bold mb-2">Analysis Complete!</h2>
                   <p className="text-gray-400">Your resume passed the initial ATS screening but needs work.</p>
               </div>
               
               <div className="relative shrink-0">
                  <svg className="w-32 h-32 transform -rotate-90">
                    <circle cx="64" cy="64" r="60" stroke="currentColor" strokeWidth="8" fill="transparent" className="text-gray-700" />
                    <circle cx="64" cy="64" r="60" stroke="currentColor" strokeWidth="8" fill="transparent" strokeDasharray={377} strokeDashoffset={377 - (377 * results.atsScore) / 100} className="text-primary transition-all duration-1000" />
                  </svg>
                  <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 text-center">
                      <span className="text-3xl font-bold font-display">{results.atsScore}</span>
                  </div>
               </div>
           </div>

           <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div className="glass-card p-6 border-t-2 border-t-accent">
                    <h3 className="text-lg font-bold flex items-center gap-2 mb-4"><CheckCircle2 className="text-accent" size={20} /> Detected Strengths</h3>
                    <div className="flex flex-wrap gap-2">
                        {results.skills.map((skill, i) => (
                           <span key={i} className="px-3 py-1 rounded-full bg-white/10 text-sm">{skill}</span>
                        ))}
                    </div>
                </div>

                <div className="glass-card p-6 border-t-2 border-t-red-400">
                    <h3 className="text-lg font-bold flex items-center gap-2 mb-4"><AlertTriangle className="text-red-400" size={20} /> Weaknesses to Fix</h3>
                    <ul className="space-y-3">
                        {results.weaknesses.map((w, i) => (
                           <li key={i} className="flex gap-3 text-gray-300 bg-white/5 p-3 rounded-lg text-sm">
                               <div className="w-1.5 h-1.5 rounded-full bg-red-400 mt-1.5 shrink-0"></div>
                               {w}
                           </li>
                        ))}
                    </ul>
                </div>
           </div>
           
           <div className="flex justify-center mt-8">
               <button className="btn-secondary" onClick={() => setResults(null)}>Upload Another Version</button>
           </div>
        </div>
      )}
    </div>
  );
}
