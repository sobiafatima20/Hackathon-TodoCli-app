// T040: Dashboard layout with navigation bar and user menu

'use client';

import React from 'react';
import { useAuth } from '@/context/AuthContext';

export default function DashboardLayout({ children }: { children: React.ReactNode }) {
  const { user, signOut } = useAuth();

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 via-gray-950 to-black">
      {/* Navigation bar */}
      <nav className="bg-gradient-to-r from-gray-900/80 to-gray-950/80 backdrop-blur-md border-b border-gray-800/50 shadow-xl sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            <div className="flex items-center">
              <h1 className="text-xl font-bold bg-gradient-to-r from-blue-400 via-purple-400 to-cyan-400 bg-clip-text text-transparent">
                Todo App
              </h1>
            </div>

            <div className="flex items-center gap-4">
              {user && (
                <>
                  <div className="flex items-center gap-2 px-3 py-1.5 rounded-lg bg-gray-800/50 border border-gray-700/50">
                    <div className="w-2 h-2 bg-green-400 rounded-full animate-pulse"></div>
                    <span className="text-sm text-gray-300 truncate max-w-32">{user.email}</span>
                  </div>
                  <button
                    onClick={signOut}
                    className="px-4 py-2 rounded-lg bg-gradient-to-r from-red-600/20 to-red-700/20 hover:from-red-600/30 hover:to-red-700/30 text-red-400 font-medium transition-all duration-200 hover:scale-105 border border-red-600/30 hover:border-red-500/50"
                  >
                    Sign Out
                  </button>
                </>
              )}
            </div>
          </div>
        </div>
      </nav>

      {/* Main content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {children}
      </main>
    </div>
  );
}
