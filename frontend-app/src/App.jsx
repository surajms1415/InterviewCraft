import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/ui/Navbar';
import Footer from './components/ui/Footer';
import Home from './pages/Home';
import CSSubjects from './pages/CSSubjects';
import SubjectDetail from './pages/SubjectDetail';
import TopicDetail from './pages/TopicDetail';
import GDModule from './pages/GDModule';
import HRInterview from './pages/HRInterview';
import ChatbotPanel from './pages/ChatbotPanel';

const App = () => {
  const [chatbotMsgs, setChatbotMsgs] = useState([{role: 'model', text: 'Hi there! Ask me anything about your tech interviews. I am powered by Gemini API. Please provide your API key below.'}]);
  const [chatbotHistory, setChatbotHistory] = useState([]);

  return (
    <Router>
      <div className="min-h-screen text-gray-100 flex flex-col font-sans">
        <Navbar />
        <main className="flex-1 container mx-auto px-4 py-8">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/subjects" element={<CSSubjects />} />
            <Route path="/subjects/:id" element={<SubjectDetail />} />
            <Route path="/subjects/:id/:topicId" element={<TopicDetail />} />
            <Route path="/gd" element={<GDModule />} />
            <Route path="/hr" element={<HRInterview />} />
            <Route 
              path="/chatbot" 
              element={<ChatbotPanel 
                msgs={chatbotMsgs} 
                setMsgs={setChatbotMsgs} 
                history={chatbotHistory} 
                setHistory={setChatbotHistory} 
              />} 
            />
          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  );
};

export default App;

