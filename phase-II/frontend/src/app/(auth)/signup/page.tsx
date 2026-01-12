// T029: Sign up page with SignUpForm and navigation links

import React from 'react';
import Link from 'next/link';
import { SignUpForm } from '@/components/auth/SignUpForm';

export default function SignUpPage() {
  return (
    <div className="space-y-8">
      <div className="text-center">
        <h2 className="text-3xl font-bold text-white mb-2">Create Account</h2>
        <p className="text-gray-400">
          Join us to start managing your tasks efficiently.
        </p>
      </div>

      <SignUpForm />

      <div className="text-center text-sm">
        <span className="text-gray-400">Already have an account? </span>
        <Link
          href="/signin"
          className="font-medium bg-gradient-to-r from-blue-400 to-purple-400 bg-clip-text text-transparent hover:underline transition-all"
        >
          Sign in
        </Link>
      </div>
    </div>
  );
}
