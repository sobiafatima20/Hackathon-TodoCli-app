import type { Config } from 'tailwindcss'

const config: Config = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        // Modern Dark Theme Colors
        background: {
          dark: '#121212',
          darker: '#0a0a0a',
          card: '#1e1e1e',
          hover: '#2a2a2a',
        },
        primary: {
          50: '#f3e9ff',
          100: '#e6d3ff',
          200: '#d9bdff',
          300: '#cc9cff',
          400: '#bb86fc',
          500: '#9d4edd',
          600: '#801fb3',
          700: '#631588',
          800: '#460d5d',
          900: '#290533',
        },
        secondary: {
          50: '#e0f9f6',
          100: '#c0f3ed',
          200: '#a0ede4',
          300: '#80e7db',
          400: '#60e1d2',
          500: '#03dac6',
          600: '#01b4a7',
          700: '#018e83',
          800: '#01685f',
          900: '#00423b',
        },
        danger: {
          400: '#f87171',
          500: '#cf6679',
          600: '#b94a5e',
          700: '#9c3043',
        },
        success: {
          400: '#a5d6a7',
          500: '#66bb6a',
          600: '#4caf50',
          700: '#388e3c',
        },
        warning: {
          400: '#ffe082',
          500: '#ffca28',
          600: '#ffb300',
          700: '#ffa000',
        },
        gray: {
          850: '#1f1f1f',
          950: '#0f0f0f',
        },
      },
      screens: {
        'sm': '640px',
        'md': '768px',
        'lg': '1024px',
        'xl': '1280px',
        '2xl': '1536px',
      },
      boxShadow: {
        'glow-primary': '0 0 20px rgba(14, 165, 233, 0.3)',
        'glow-accent': '0 0 20px rgba(168, 85, 247, 0.3)',
        'card': '0 4px 6px -1px rgba(0, 0, 0, 0.3), 0 2px 4px -1px rgba(0, 0, 0, 0.2)',
      },
      borderRadius: {
        'xl': '1rem',
        '2xl': '1.5rem',
      },
    },
  },
  plugins: [],
}

export default config
