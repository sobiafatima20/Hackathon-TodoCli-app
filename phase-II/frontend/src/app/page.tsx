// T105: Landing page with branding and auth CTAs

import Link from 'next/link';

export default function LandingPage() {
  return (
    <div className="min-h-screen bg-black relative overflow-hidden">
      {/* Animated background */}
      <div className="absolute inset-0 bg-gradient-to-br from-gray-900/20 via-blue-900/10 to-purple-900/10" />
      <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-blue-900/5 via-transparent to-black" />

      {/* Floating particles */}
      {[...Array(15)].map((_, i) => (
        <div
          key={i}
          className="absolute rounded-full bg-blue-500/20 animate-pulse"
          style={{
            top: `${Math.random() * 100}%`,
            left: `${Math.random() * 100}%`,
            width: `${Math.random() * 8 + 2}px`,
            height: `${Math.random() * 8 + 2}px`,
            animationDelay: `${Math.random() * 5}s`,
            animationDuration: `${Math.random() * 4 + 3}s`
          }}
        />
      ))}

      <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Header */}
        <header className="py-6 flex items-center justify-between">
          <h1 className="text-3xl font-bold bg-gradient-to-r from-blue-400 via-purple-400 to-cyan-400 bg-clip-text text-transparent">
            Todo App
          </h1>
          <div className="flex items-center gap-4">
            <Link href="/signin">
              <div className="px-6 py-2.5 rounded-xl text-gray-300 hover:text-white transition-all duration-300 hover:bg-gray-800/60 border border-gray-700/50 hover:border-blue-500/50 font-medium">
                Sign In
              </div>
            </Link>
            <Link href="/signup">
              <div className="px-6 py-2.5 rounded-xl bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-500 hover:to-purple-500 text-white font-semibold transition-all duration-300 hover:shadow-2xl hover:shadow-blue-500/30 hover:scale-105 transform hover:-translate-y-0.5">
                SignUp
              </div>
            </Link>
          </div>
        </header>

        {/* Hero section */}
        <div className="py-24 md:py-36 text-center">
          <div className="inline-block mb-8 px-6 py-3 bg-gradient-to-r from-blue-500/10 to-purple-500/10 border border-blue-500/20 rounded-2xl backdrop-blur-sm">
            <span className="text-sm font-medium bg-gradient-to-r from-blue-400 to-purple-400 bg-clip-text text-transparent">
              📋 Your Personal Task Manager
            </span>
          </div>

          <h2 className="text-6xl md:text-8xl font-bold text-white mb-8 leading-tight">
            Simplify Your
            <br />
            <span className="bg-gradient-to-r from-blue-400 via-purple-400 to-cyan-400 bg-clip-text text-transparent">
              Daily Tasks
            </span>
          </h2>

          <p className="text-xl md:text-2xl text-gray-300 mb-12 max-w-3xl mx-auto leading-relaxed">
            Streamline your productivity with our intuitive task management platform.
            Create, organize, and track your tasks with ease to stay on top of your goals.
          </p>

          <div className="flex items-center justify-center gap-6 flex-wrap">
            <Link href="/signup">
              <div className="px-10 py-5 rounded-2xl bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-500 hover:to-purple-500 text-white font-bold text-lg transition-all duration-500 hover:shadow-2xl hover:shadow-blue-500/40 hover:scale-105 transform hover:-translate-y-2 shadow-lg">
                <span className="mr-3">📝</span>Get Started Today
              </div>
            </Link>
            <Link href="/signin">
              <div className="px-10 py-5 rounded-2xl bg-gray-800/60 hover:bg-gray-700/60 text-white font-bold text-lg border-2 border-gray-600 hover:border-blue-500/50 transition-all duration-300 hover:shadow-xl hover:scale-105 backdrop-blur-sm">
                Sign In <span className="ml-2">👉</span>
              </div>
            </Link>
          </div>
        </div>

        {/* Features */}
        <div className="py-20 grid grid-cols-1 md:grid-cols-3 gap-10 max-w-6xl mx-auto">
          <div className="group bg-gradient-to-br from-gray-900/70 to-gray-950/70 p-10 rounded-3xl border border-gray-700/50 backdrop-blur-sm hover:border-blue-500/40 transition-all duration-500 hover:-translate-y-3 hover:shadow-2xl hover:shadow-blue-500/15">
            <div className="w-20 h-20 bg-gradient-to-r from-blue-500/30 to-purple-500/30 rounded-2xl flex items-center justify-center mb-8 backdrop-blur-sm group-hover:scale-110 transition-transform duration-300">
              <svg
                className="w-10 h-10 text-blue-400"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"
                />
              </svg>
            </div>
            <h3 className="text-2xl font-bold text-white mb-4">
              Task Management Made Simple
            </h3>
            <p className="text-gray-400 leading-relaxed text-lg">
              Create, edit, and organize your tasks with our user-friendly interface.
              Mark tasks as complete and track your progress effortlessly.
            </p>
          </div>

          <div className="group bg-gradient-to-br from-gray-900/70 to-gray-950/70 p-10 rounded-3xl border border-gray-700/50 backdrop-blur-sm hover:border-purple-500/40 transition-all duration-500 hover:-translate-y-3 hover:shadow-2xl hover:shadow-purple-500/15">
            <div className="w-20 h-20 bg-gradient-to-r from-purple-500/30 to-cyan-500/30 rounded-2xl flex items-center justify-center mb-8 backdrop-blur-sm group-hover:scale-110 transition-transform duration-300">
              <svg
                className="w-10 h-10 text-purple-400"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M13 10V3L4 14h7v7l9-11h-7z"
                />
              </svg>
            </div>
            <h3 className="text-2xl font-bold text-white mb-4">
              Boost Your Productivity
            </h3>
            <p className="text-gray-400 leading-relaxed text-lg">
              Stay focused and productive by organizing your tasks by priority and deadline.
              Never miss an important task again.
            </p>
          </div>

          <div className="group bg-gradient-to-br from-gray-900/70 to-gray-950/70 p-10 rounded-3xl border border-gray-700/50 backdrop-blur-sm hover:border-cyan-500/40 transition-all duration-500 hover:-translate-y-3 hover:shadow-2xl hover:shadow-cyan-500/15">
            <div className="w-20 h-20 bg-gradient-to-r from-cyan-500/30 to-blue-500/30 rounded-2xl flex items-center justify-center mb-8 backdrop-blur-sm group-hover:scale-110 transition-transform duration-300">
              <svg
                className="w-10 h-10 text-cyan-400"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"
                />
              </svg>
            </div>
            <h3 className="text-2xl font-bold text-white mb-4">
              Secure & Reliable
            </h3>
            <p className="text-gray-400 leading-relaxed text-lg">
              Your tasks and data are protected with industry-standard security measures.
              Access your tasks anytime, anywhere with confidence.
            </p>
          </div>
        </div>

        {/* Final CTA */}
        <div className="py-20 text-center">
          <div className="max-w-4xl mx-auto bg-gradient-to-r from-gray-900/50 to-gray-950/50 p-12 rounded-3xl border border-gray-700/50 backdrop-blur-sm">
            <h3 className="text-4xl font-bold text-white mb-6">
              Ready to Transform Your Productivity?
            </h3>
            <p className="text-xl text-gray-300 mb-10 max-w-2xl mx-auto">
              Join thousands of users who have simplified their task management and achieved their goals.
            </p>
            <Link href="/signup">
              <div className="inline-block px-12 py-6 rounded-2xl bg-gradient-to-r from-blue-600 via-purple-600 to-cyan-600 hover:from-blue-500 hover:via-purple-500 hover:to-cyan-500 text-white font-bold text-xl transition-all duration-300 hover:shadow-2xl hover:shadow-blue-500/30 hover:scale-110 transform hover:-translate-y-2">
                Start Organizing Today
              </div>
            </Link>
          </div>
        </div>

        {/* Footer */}
        <footer className="py-10 text-center text-gray-500 border-t border-gray-800/50">
          <p className="text-lg">&copy; 2026 Todo App. Built with Next.js, FastAPI, and
          -PostgreSQL</p>
          <p className="text-sm mt-2">Simple, powerful, and effective task management.</p>
        </footer>
      </div>
    </div>
  );
}
