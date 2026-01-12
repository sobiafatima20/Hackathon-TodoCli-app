// T027: Auth layout with centered card

import React from 'react';

export default function AuthLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 via-gray-950 to-black relative overflow-hidden flex flex-col justify-center py-12 sm:px-6 lg:px-8">
      {/* Animated background */}
      <div className="absolute inset-0 bg-gradient-to-br from-gray-900/20 via-blue-900/10 to-purple-900/10" />
      <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-blue-900/5 via-transparent to-black" />

      {/* Floating particles */}
      {[...Array(10)].map((_, i) => (
        <div
          key={i}
          className="absolute rounded-full bg-blue-500/20 animate-pulse"
          style={{
            top: `${Math.random() * 100}%`,
            left: `${Math.random() * 100}%`,
            width: `${Math.random() * 6 + 2}px`,
            height: `${Math.random() * 6 + 2}px`,
            animationDelay: `${Math.random() * 5}s`,
            animationDuration: `${Math.random() * 4 + 3}s`
          }}
        />
      ))}

      <div className="relative z-10 sm:mx-auto sm:w-full sm:max-w-md">
        <h1 className="text-center text-3xl font-bold bg-gradient-to-r from-blue-400 via-purple-400 to-cyan-400 bg-clip-text text-transparent mb-8">
          Todo App
        </h1>
      </div>

      <div className="relative z-10 sm:mx-auto sm:w-full sm:max-w-md">
        <div className="bg-gradient-to-br from-gray-900/70 to-gray-950/70 p-10 rounded-3xl border border-gray-700/50 backdrop-blur-sm shadow-2xl shadow-blue-500/10">
          {children}
        </div>
      </div>
    </div>
  );
}
