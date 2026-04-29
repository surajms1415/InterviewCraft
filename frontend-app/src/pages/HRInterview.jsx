import React, { useState, useEffect } from 'react';
import { UploadCloud, CheckCircle, Link, ListChecks, Play } from 'lucide-react';
import { motion } from 'framer-motion';
import ReactMarkdown from 'react-markdown';
import hrData from '../data/hr_questions.json';

const HRInterview = () => {
    const [file, setFile] = useState(null);
    const [githubLink, setGithubLink] = useState('');
    const [apiKey, setApiKey] = useState('');
    const [analyzing, setAnalyzing] = useState(false);
    const [questions, setQuestions] = useState([]);
    const [manualFallbackMode, setManualFallbackMode] = useState(false);
    const [fallbackStep, setFallbackStep] = useState(1);
    const [projectDomain, setProjectDomain] = useState('');
    const [projectFeatures, setProjectFeatures] = useState('');
    const [fallbackErrorMsg, setFallbackErrorMsg] = useState('');

    useEffect(() => {
        const savedKey = localStorage.getItem('gemini_api_key');
        if (savedKey) setApiKey(savedKey);
    }, []);

    const handleApiKeyChange = (e) => {
        const val = e.target.value;
        setApiKey(val);
        localStorage.setItem('gemini_api_key', val);
    };

    const handleGenerate = async () => {
        if (!githubLink.trim() && !file) return;
        
        setAnalyzing(true);
        const formData = new FormData();
        if (file) {
            formData.append('file', file);
        }
        formData.append('github_link', githubLink);
        formData.append('api_key', apiKey);
        
        try {
            const apiUrl = import.meta.env.VITE_API_URL || 'http://localhost:8000';
            const res = await fetch(`${apiUrl}/api/resume/generate-hr`, {
                method: 'POST',
                body: formData
            });
            const data = await res.json();
            
            if (!res.ok) {
                const err = data.detail || data.error || "An error occurred.";
                console.error(err);
                setAnalyzing(false);
                setFallbackErrorMsg(typeof err === 'string' ? err : JSON.stringify(err));
                setManualFallbackMode(true);
                return;
            }
            
            if (data.questions) {
                if (data.questions.length === 1 && typeof data.questions[0] === 'string' && data.questions[0].includes('API Key limit')) {
                    setFallbackErrorMsg(data.questions[0]);
                    setManualFallbackMode(true);
                } else if (data.questions.length === 1 && data.questions[0].question && data.questions[0].question.includes('API Key')) {
                    setFallbackErrorMsg(data.questions[0].question);
                    setManualFallbackMode(true);
                } else if (data.questions.length === 1 && typeof data.questions[0] === 'string' && data.questions[0].includes('Error generating')) {
                    setFallbackErrorMsg(data.questions[0]);
                    setManualFallbackMode(true);
                } else {
                    setQuestions(data.questions);
                }
            }
            setAnalyzing(false);
        } catch(e) {
            console.error(e);
            setAnalyzing(false);
            setFallbackErrorMsg("Network error or server unreachable.");
            setManualFallbackMode(true);
        }
    };

    const generateStaticQuestions = () => {
        let domainQs = [];
        if (projectDomain === 'Frontend') {
            domainQs = [
                {
                    question: "You mentioned your project involves Frontend work. How exactly did you mitigate prop-drilling or manage state in your application, and what were the architectural trade-offs?",
                    solution: "- **State Management**: Discuss whether you used Context API, Redux, Zustand, etc. and why.\n- **Trade-offs**: Mention bundle size, boilerplate, or performance.\n- **Performance**: Address re-renders and component memoization."
                },
                {
                    question: "Frontend performance is critical. Can you describe a specific time you optimized the Largest Contentful Paint (LCP) or First Input Delay (FID) in your application?",
                    solution: "- **Metrics**: Show you understand Web Vitals.\n- **Actions**: Discuss lazy loading, code splitting, or optimizing images.\n- **Results**: Provide data on the improvement if possible."
                }
            ];
        } else if (projectDomain === 'Backend') {
            domainQs = [
                {
                    question: "For the Backend portion of your project, how did you handle database connection pooling and prevent query bottlenecks under load?",
                    solution: "- **Database**: Discuss ORMs vs raw queries, indexing, and connection pools.\n- **Scaling**: Mention handling high concurrency without dropping connections.\n- **Trade-offs**: ACID compliance vs performance."
                },
                {
                    question: "How did you design your API architecture? If you had to migrate it from a monolith to microservices, what would be your first step?",
                    solution: "- **Design**: REST vs GraphQL vs gRPC.\n- **Migration**: Discuss domain-driven design and separating databases per service.\n- **Challenges**: Mention distributed transactions or network latency."
                }
            ];
        } else if (projectDomain === 'Data/AI') {
            domainQs = [
                {
                    question: "In your Data/AI project, how did you handle data cleaning and ensure your model wasn't overfitting to the training set?",
                    solution: "- **Data Pipeline**: Discuss handling missing values, normalization, and feature engineering.\n- **Validation**: Mention cross-validation techniques.\n- **Metrics**: Discuss precision, recall, and F1 score trade-offs."
                },
                {
                    question: "Deploying AI models can be tricky. How did you serve your model, and how would you scale the inference architecture if traffic spiked 100x?",
                    solution: "- **Serving**: Discuss FastAPI, Flask, or specialized servers like TF Serving.\n- **Scaling**: Mention batch inference vs real-time, GPU utilization, and horizontal scaling."
                }
            ];
        } else {
            domainQs = [
                {
                    question: "For a Full Stack or general project, how did you ensure end-to-end type safety and handle error boundaries between the client and server?",
                    solution: "- **Type Safety**: Discuss TypeScript, tRPC, or OpenAPI spec generation.\n- **Error Handling**: Mention structured API responses and frontend global error catchers."
                },
                {
                    question: "What was the most severe technical debt you accumulated in this project, and how did you plan to pay it down?",
                    solution: "- **Self-Awareness**: Acknowledge that all projects have debt.\n- **Specifics**: Point out a specific rushed feature or non-scalable architectural choice.\n- **Action Plan**: Discuss refactoring steps without stopping feature development."
                }
            ];
        }

        const featureQ = {
            question: `You highlighted these core functionalities: "${projectFeatures}". If a critical bug in this specific area brought down production, what is your exact step-by-step incident response plan?`,
            solution: "- **Triage**: Acknowledge the outage, check logs (Datadog/CloudWatch).\n- **Mitigation**: Roll back the deployment or toggle a feature flag.\n- **Resolution**: Reproduce locally, fix, write a regression test.\n- **Post-Mortem**: Document why it happened and how to prevent it."
        };

        const behavioralQ = {
            question: "Describe a time during this project where you vehemently disagreed with a technical decision made by a teammate or mentor. How did you resolve the professional conflict?",
            solution: "- **Context**: Keep it brief and focused on the technical disagreement.\n- **Action**: Highlight that you used data, benchmarks, or documentation to argue your point, NOT emotion.\n- **Result**: Show that you either convinced them or committed to their decision professionally."
        };

        setQuestions([...domainQs, featureQ, behavioralQ]);
        setManualFallbackMode(false);
        setFallbackStep(1);
        setProjectDomain('');
        setProjectFeatures('');
    };

    const handleExport = () => {
        if (questions.length === 0) return;
        
        let htmlContent = `
            <html xmlns:o='urn:schemas-microsoft-com:office:office' xmlns:w='urn:schemas-microsoft-com:office:word' xmlns='http://www.w3.org/TR/REC-html40'>
            <head><meta charset='utf-8'><title>HR Interview Questions</title></head><body>
            <h1>Personalized HR Interview Questions</h1>
        `;
        
        questions.forEach((q, i) => {
            const qText = typeof q === 'string' ? q : q.question;
            const sText = typeof q === 'object' && q.solution ? q.solution : '';
            htmlContent += `<h3>${i + 1}. ${qText}</h3>`;
            if (sText) {
                htmlContent += `<p><strong>How to reply:</strong> ${sText}</p>`;
            }
        });
        
        htmlContent += `</body></html>`;
        
        const blob = new Blob(['\ufeff', htmlContent], {
            type: 'application/msword'
        });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'HR_Interview_Questions.doc';
        a.click();
        URL.revokeObjectURL(url);
    };

    return (
        <div className="max-w-6xl mx-auto py-12 relative z-10">
             <h1 className="text-4xl md:text-5xl font-display font-extrabold mb-6 text-transparent bg-clip-text bg-gradient-to-r from-primary to-secondary tracking-tight drop-shadow-[0_0_10px_rgba(59,130,246,0.3)]">Intensive HR & Behavioral Interview</h1>
             <p className="text-xl text-gray-400 mb-12 max-w-3xl font-light leading-relaxed">Review frequently asked questions across different categories by HR professionals, or upload your resume and provide your GitHub link to generate intense personalized questions.</p>
             
             {/* Common HR Questions Section */}
             <div className="mb-16 relative">
                 <div className="absolute top-0 right-0 w-64 h-64 bg-primary/5 rounded-full blur-[100px] pointer-events-none"></div>
                 <h2 className="text-3xl font-display font-bold mb-8 text-white relative z-10">Common HR Questions</h2>
                 <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 relative z-10">
                     {Object.entries(hrData).map(([category, qs]) => (
                         <div key={category} className="glass-card p-8 border border-white/10 hover:-translate-y-2 hover:border-primary/30 hover:shadow-[0_0_30px_rgba(59,130,246,0.15)] transition-all">
                             <h3 className="text-2xl font-display font-bold mb-6 text-primary border-b border-white/10 pb-3">{category}</h3>
                             <ul className="space-y-6">
                                 {qs.map((q, idx) => (
                                     <li key={idx} className="text-gray-300">
                                         <p className="font-semibold mb-2 text-white">{q.question}</p>
                                         <p className="text-sm text-gray-400 italic font-light">💡 {q.hint}</p>
                                     </li>
                                 ))}
                             </ul>
                         </div>
                     ))}
                 </div>
             </div>
             
             <div className="border-t border-white/10 my-12"></div>
             
             <h2 className="text-3xl font-display font-bold mb-8 text-white">Generate Personalized Questions</h2>
             
             {questions.length === 0 && !manualFallbackMode && (
                 <div className="space-y-6">
                     <div className="glass-card p-10 border border-white/10 flex flex-col items-center relative overflow-hidden">
                         <div className="absolute inset-0 bg-gradient-to-br from-primary/5 to-secondary/5 pointer-events-none"></div>
                         
                         <div className="w-full mb-8 relative z-10">
                             <label className="block text-gray-300 font-bold mb-3 font-display text-lg">GitHub Profile Link</label>
                             <div className="relative">
                                 <div className="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                                     <Link className="h-5 w-5 text-gray-400" />
                                 </div>
                                 <input 
                                     type="text" 
                                     value={githubLink}
                                     onChange={(e) => setGithubLink(e.target.value)}
                                     placeholder="e.g. https://github.com/username"
                                     className="input-field pl-12"
                                 />
                             </div>
                         </div>

                         <div className="w-full mb-8 relative z-10">
                             <label className="block text-gray-300 font-bold mb-3 font-display text-lg flex items-center gap-2">
                                 Resume Upload <span className="text-gray-500 font-normal text-sm font-sans">(Optional, PDF only)</span>
                             </label>
                             <div className="flex flex-col items-center border-2 border-dashed border-primary/30 bg-primary/5 p-8 rounded-2xl hover:bg-primary/10 transition-colors group">
                                 <UploadCloud className="text-primary w-10 h-10 mb-4 group-hover:scale-110 transition-transform duration-300" />
                                 <label className="cursor-pointer btn-secondary inline-flex font-semibold">
                                     Select PDF
                                     <input type="file" className="hidden" accept=".pdf" onChange={(e) => setFile(e.target.files[0])} />
                                 </label>
                                 {file && <p className="mt-4 text-sm text-accent font-medium break-all flex items-center gap-2"><CheckCircle className="w-4 h-4"/> Selected: {file.name}</p>}
                             </div>
                         </div>

                         <div className="w-full mb-10 relative z-10">
                             <label className="block text-gray-300 font-bold mb-3 font-display text-lg">Gemini API Key <a href="https://aistudio.google.com/app/apikey" target="_blank" rel="noreferrer" className="text-primary hover:text-blue-400 underline font-normal text-sm ml-2 font-sans">(Get your API Key here)</a></label>
                             <div className="relative">
                                 <input 
                                     type="password" 
                                     value={apiKey}
                                     onChange={handleApiKeyChange}
                                     placeholder="AIzaSy..."
                                     className="input-field"
                                 />
                             </div>
                         </div>
                         
                         <button 
                             onClick={handleGenerate} 
                             disabled={(!githubLink && !file) || analyzing} 
                             className={`btn-primary w-full py-5 text-lg flex items-center justify-center gap-3 relative z-10 ${analyzing ? 'animate-pulse' : ''}`}
                         >
                             {analyzing ? 'Analyzing Persona & Generating...' : <><Play className="w-6 h-6"/> Generate Intense Questions</>}
                         </button>
                     </div>
                 </div>
             )}

             {manualFallbackMode && (
                 <div className="space-y-6">
                     {fallbackErrorMsg && (
                         <div className="bg-red-500/10 border border-red-500/30 text-red-400 p-4 rounded-xl flex items-start gap-3">
                             <div className="font-bold flex-shrink-0 mt-0.5">⚠️ API Error:</div>
                             <div className="font-light text-sm">{fallbackErrorMsg}</div>
                         </div>
                     )}
                     <div className="glass-card p-10 border border-emerald-500/30 flex flex-col items-center relative overflow-hidden shadow-[0_0_30px_rgba(16,185,129,0.1)]">
                         <div className="absolute inset-0 bg-gradient-to-br from-emerald-500/5 to-primary/5 pointer-events-none"></div>
                         
                         <div className="text-center mb-8 relative z-10">
                             <h3 className="text-2xl font-display font-bold text-emerald-400 mb-3 flex items-center justify-center gap-3">
                                 <ListChecks className="w-8 h-8"/> Manual Interview Configuration
                             </h3>
                             <p className="text-gray-300 font-light max-w-xl mx-auto">
                                 Our AI is currently at peak capacity or your API limit was reached. Let's get you specialized questions manually!
                             </p>
                         </div>

                         {fallbackStep === 1 && (
                             <div className="w-full max-w-2xl relative z-10 animate-fade-in">
                                 <label className="block text-white font-bold mb-6 font-display text-xl text-center">What is the primary domain of your project?</label>
                                 <div className="grid grid-cols-2 gap-4">
                                     {['Frontend', 'Backend', 'Full Stack', 'Data/AI'].map(domain => (
                                         <button
                                             key={domain}
                                             onClick={() => { setProjectDomain(domain); setFallbackStep(2); }}
                                             className="py-4 px-6 rounded-xl border border-white/10 bg-white/5 hover:bg-primary/20 hover:border-primary/50 text-white font-medium transition-all"
                                         >
                                             {domain}
                                         </button>
                                     ))}
                                 </div>
                             </div>
                         )}

                         {fallbackStep === 2 && (
                             <div className="w-full max-w-2xl relative z-10 animate-fade-in">
                                 <label className="block text-white font-bold mb-4 font-display text-xl">What are the core functionalities or key challenges of this project?</label>
                                 <textarea
                                     value={projectFeatures}
                                     onChange={(e) => setProjectFeatures(e.target.value)}
                                     placeholder="e.g., User authentication, real-time chat using WebSockets, dealing with large dataset pagination..."
                                     className="w-full bg-surface/50 border border-white/10 rounded-xl p-5 text-white placeholder-gray-500 focus:outline-none focus:border-primary/50 focus:ring-1 focus:ring-primary/50 min-h-[150px] mb-6"
                                 />
                                 <div className="flex gap-4">
                                     <button onClick={() => setFallbackStep(1)} className="btn-secondary py-3 px-6 flex-1">Back</button>
                                     <button 
                                         onClick={generateStaticQuestions}
                                         disabled={!projectFeatures.trim()}
                                         className="btn-primary py-3 px-6 flex-2 w-full disabled:opacity-50"
                                     >
                                         Generate Questions
                                     </button>
                                 </div>
                             </div>
                         )}
                     </div>
                 </div>
             )}

             {questions.length > 0 && (
                 <div className="space-y-8">
                      <div className="glass-card bg-emerald-500/10 border border-emerald-500/30 p-8 flex items-center justify-between shadow-[0_0_30px_rgba(16,185,129,0.15)]">
                          <div>
                              <h3 className="text-emerald-400 font-display font-bold text-2xl mb-2 flex items-center gap-3"><CheckCircle className="w-7 h-7"/> Interview Matrix Generated</h3>
                              <p className="text-emerald-200/70 font-light">These questions dive deep into architectural decisions, scale, constraints, and professional conflict.</p>
                          </div>
                          <div className="flex gap-4">
                                  <button 
                                      onClick={handleExport} 
                                      className="btn-primary px-6"
                                  >
                                      Export to Word
                                  </button>
                              <button 
                                  onClick={() => {setQuestions([]); setFile(null); setGithubLink('');}} 
                                  className="btn-secondary px-6"
                              >
                                  Start Over
                              </button>
                          </div>
                      </div>

                      <div className="glass-card border border-white/10 p-10 space-y-8 relative overflow-hidden">
                          <div className="absolute top-0 right-0 w-64 h-64 bg-primary/5 rounded-full blur-[100px] pointer-events-none"></div>
                          <h2 className="text-3xl font-display font-bold flex items-center gap-3 text-white border-b border-white/10 pb-6 relative z-10"><ListChecks className="text-primary w-8 h-8"/> Your Custom Interview Checklist</h2>
                          
                          <div className="space-y-6 relative z-10">
                              {questions.map((q, idx) => (
                                  <motion.div 
                                      initial={{ opacity: 0, y: 10 }}
                                      animate={{ opacity: 1, y: 0 }}
                                      transition={{ delay: idx * 0.1 }}
                                      key={idx} 
                                      className="flex gap-6 p-6 rounded-2xl bg-surface border border-white/5 hover:border-primary/30 hover:shadow-[0_0_20px_rgba(59,130,246,0.1)] transition-all group"
                                  >
                                      <div className="bg-primary/20 text-primary font-bold text-xl w-14 h-14 rounded-full flex items-center justify-center flex-shrink-0 group-hover:scale-110 transition-transform border border-primary/20 shadow-[0_0_10px_rgba(59,130,246,0.2)]">
                                          {idx + 1}
                                      </div>
                                      <div className="flex flex-col pt-1 w-full">
                                          <div className="text-white font-medium text-lg leading-relaxed mb-4">
                                              <ReactMarkdown components={{
                                                  strong: ({node, ...props}) => <span className="font-bold text-white" {...props} />,
                                                  p: ({node, ...props}) => <span {...props} />,
                                                  em: ({node, ...props}) => <em className="italic text-primary" {...props} />
                                              }}>
                                                  {typeof q === 'string' ? q : q.question}
                                              </ReactMarkdown>
                                          </div>
                                          {typeof q === 'object' && q.solution && (
                                              <div className="text-sm text-gray-300 bg-white/5 p-5 rounded-xl border border-white/10 font-light leading-relaxed">
                                                  <div className="font-bold text-primary mb-3 flex items-center gap-2">💡 How to reply:</div>
                                                  <ReactMarkdown components={{
                                                      strong: ({node, ...props}) => <span className="font-semibold text-white" {...props} />,
                                                      p: ({node, ...props}) => <p className="mb-3 last:mb-0" {...props} />,
                                                      ul: ({node, ...props}) => <ul className="list-disc pl-5 my-3 space-y-2 text-gray-300" {...props} />,
                                                      ol: ({node, ...props}) => <ol className="list-decimal pl-5 my-3 space-y-2 text-gray-300" {...props} />,
                                                      li: ({node, ...props}) => <li className="text-gray-300" {...props} />
                                                  }}>
                                                      {q.solution}
                                                  </ReactMarkdown>
                                              </div>
                                          )}
                                      </div>
                                  </motion.div>
                              ))}
                          </div>
                      </div>
                 </div>
             )}
        </div>
    );
};

export default HRInterview;
