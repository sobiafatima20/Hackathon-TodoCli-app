// T028: Sign in page with SignInForm and navigation links

import React from 'react';
import Link from 'next/link';
import { SignInForm } from '@/components/auth/SignInForm';

export default function SignInPage() {
  return (
    <div className="space-y-8">
      <div className="text-center">
        <h2 className="text-3xl font-bold text-white mb-2">Welcome Back</h2>
        <p className="text-gray-400">
          Sign in to continue managing your tasks.
        </p>
      </div>

      <SignInForm />

      <div className="text-center text-sm">
        <span className="text-gray-400">Don't have an account? </span>
        <Link
          href="/signup"
          className="font-medium bg-gradient-to-r from-blue-400 to-purple-400 bg-clip-text text-transparent hover:underline transition-all"
        >
          Sign up
        </Link>
      </div>
    </div>
  );
}
