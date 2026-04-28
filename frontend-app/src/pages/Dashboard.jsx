import React from 'react';
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, CartesianGrid } from 'recharts';
import { Target, TrendingUp, CheckCircle, BrainCircuit, Activity } from 'lucide-react';

const mockData = [
  { name: 'DBMS', score: 85 },
  { name: 'OS', score: 65 },
  { name: 'System Design', score: 45 },
  { name: 'HR', score: 90 },
];

export default function Dashboard() {
  return (
    <div className="space-y-8 animate-fade-in">
      <header className="mb-8">
        <h1 className="text-3xl font-display font-bold text-white">Dashboard Overview</h1>
        <p className="text-gray-400 mt-2">Track your placement prep progress and analytics.</p>
      </header>

      {/* Stats Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <StatCard icon={<Target />} title="Overall ATS Score" value="75%" trend="+5%" />
        <StatCard icon={<CheckCircle />} title="Interviews Given" value="12" />
        <StatCard icon={<TrendingUp />} title="Avg Score" value="7.8 / 10" trend="+0.5" />
        <StatCard icon={<BrainCircuit />} title="Weakest Subject" value="System Design" />
      </div>

      {/* Main Charts & Tasks */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        
        {/* Chart */}
        <div className="lg:col-span-2 glass-card p-6 border-t-2 border-t-primary">
          <div className="flex items-center justify-between mb-6">
             <h2 className="text-xl font-bold font-display">Performance by Topic</h2>
             <button className="text-sm text-primary hover:text-white transition">View All</button>
          </div>
          <div className="h-72 w-full">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={mockData}>
                <CartesianGrid strokeDasharray="3 3" stroke="#334155" vertical={false} />
                <XAxis dataKey="name" stroke="#94A3B8" />
                <YAxis stroke="#94A3B8" />
                <Tooltip cursor={{fill: 'rgba(255,255,255,0.05)'}} contentStyle={{ backgroundColor: '#1E293B', borderColor: '#334155', borderRadius: '8px' }} />
                <Bar dataKey="score" fill="#3B82F6" radius={[4, 4, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* Daily Missions */}
        <div className="glass-card p-6 border-t-2 border-t-accent">
          <div className="flex items-center gap-3 mb-6">
             <Activity className="text-accent" />
             <h2 className="text-xl font-bold font-display">Daily Missions</h2>
          </div>
          <div className="space-y-4">
            <Mission text="Revise OS Paging Concepts" completed={true} />
            <Mission text="Take 1 HR Mock Interview" completed={false} />
            <Mission text="Fix resume action verbs" completed={false} />
          </div>
          <button className="btn-primary w-full mt-6 flex items-center justify-center gap-2">
            Auto-Generate Tasks
          </button>
        </div>

      </div>

      {/* AI Recommendation */}
      <div className="p-1 rounded-2xl bg-gradient-to-r from-primary via-secondary to-accent">
         <div className="bg-background rounded-xl p-6 h-full w-full flex items-center gap-6">
           <div className="p-4 bg-white/5 rounded-full">
              <BrainCircuit size={32} className="text-white" />
           </div>
           <div>
              <h3 className="font-bold text-lg">AI Recommendation</h3>
              <p className="text-gray-300 mt-1">Based on your recent tests, you struggle with <strong>Database Scaling</strong>. We recommend starting the Last-Day Revision mode for DBMS immediately.</p>
           </div>
           <button className="btn-secondary ml-auto block">Review DBMS</button>
         </div>
      </div>
    </div>
  );
}

function StatCard({ icon, title, value, trend }) {
  return (
    <div className="glass-card p-6 flex flex-col hover:-translate-y-1 transition duration-300">
      <div className="flex items-start justify-between">
        <div className="p-3 bg-white/5 rounded-lg text-primary">{icon}</div>
        {trend && <span className={`text-sm font-bold ${trend.startsWith('+') ? 'text-accent' : 'text-red-400'}`}>{trend}</span>}
      </div>
      <h3 className="text-gray-400 mt-4 text-sm font-medium">{title}</h3>
      <p className="text-2xl font-bold text-white mt-1 font-display">{value}</p>
    </div>
  )
}

function Mission({ text, completed }) {
  return (
    <div className={`p-4 rounded-xl border flex items-center gap-4 transition-colors ${completed ? 'bg-accent/10 border-accent/20' : 'bg-white/5 border-white/10 hover:bg-white/10'}`}>
       <div className={`w-6 h-6 rounded-full border-2 flex items-center justify-center ${completed ? 'border-accent bg-accent' : 'border-gray-500'}`}>
         {completed && <CheckCircle size={14} className="text-background" />}
       </div>
       <span className={completed ? 'line-through text-gray-500 font-medium' : 'text-gray-200 font-medium'}>{text}</span>
    </div>
  )
}
