// T036: TaskCard component with task display and actions

'use client';

import React from 'react';
import { Task } from '@/types/tasks';

interface TaskCardProps {
  task: Task;
  onToggleComplete: () => void;
  onEdit: () => void;
  onDelete: () => void;
}

export function TaskCard({ task, onToggleComplete, onEdit, onDelete }: TaskCardProps) {
  return (
    <div className={`
      bg-gradient-to-br from-background-card to-background-hover
      border border-gray-700/50 rounded-2xl p-6
      hover:shadow-xl hover:shadow-primary-500/10 transition-all duration-300
      hover:-translate-y-1 hover:border-primary-500/30
      ${task.is_completed ? 'opacity-80 bg-gray-900/50' : 'shadow-lg'}
      backdrop-blur-sm
    `}>
      <div className="flex items-start gap-4">
        <div className="pt-1">
          <button
            onClick={onToggleComplete}
            className={`
              relative w-6 h-6 rounded-lg border-2 flex items-center justify-center
              transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-primary-500/50
              ${task.is_completed
                ? 'bg-gradient-to-r from-primary-500 to-primary-600 border-primary-500'
                : 'border-gray-600 hover:border-primary-500 hover:bg-primary-500/10'
              }
            `}
            aria-label={`Mark "${task.title}" as ${task.is_completed ? 'incomplete' : 'complete'}`}
          >
            {task.is_completed && (
              <svg
                className="w-4 h-4 text-white"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={3}
                  d="M5 13l4 4L19 7"
                />
              </svg>
            )}
          </button>
        </div>

        <div className="flex-1 min-w-0">
          <div className="flex items-start justify-between gap-3">
            <h3
              className={`
                text-lg font-semibold leading-tight
                ${task.is_completed
                  ? 'line-through text-gray-500'
                  : 'text-gray-100 hover:text-primary-400 transition-colors'
                }
              `}
            >
              {task.title}
            </h3>
            {task.is_completed && (
              <span className={`
                inline-flex items-center px-3 py-1 rounded-full text-xs font-medium
                bg-gradient-to-r from-green-500/20 to-green-600/20
                text-green-400 border border-green-500/30
                shadow-lg shadow-green-500/10
              `}>
                <svg className="w-3 h-3 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                </svg>
                Completed
              </span>
            )}
          </div>

          {task.description && (
            <p className={`
              mt-2 text-sm
              ${task.is_completed ? 'text-gray-500' : 'text-gray-400'}
              line-clamp-2 leading-relaxed
            `}>
              {task.description}
            </p>
          )}

          <div className="mt-4 flex items-center justify-between">
            <div className="flex items-center gap-3 text-xs text-gray-500">
              <div className="flex items-center gap-1">
                <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                </svg>
                <span>{new Date(task.created_at).toLocaleDateString()}</span>
              </div>

              {!task.is_completed && (
                <div className="flex items-center gap-1">
                  <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                  <span>Pending</span>
                </div>
              )}
            </div>

            <div className="flex items-center gap-2">
              <button
                onClick={onEdit}
                className={`
                  px-3 py-1.5 rounded-lg text-sm font-medium transition-all duration-200
                  hover:scale-105 hover:shadow-lg
                  bg-blue-600/20 hover:bg-blue-600/30
                  text-blue-400 hover:text-blue-300
                  border border-blue-600/30 hover:border-blue-500/50
                `}
              >
                <svg className="w-4 h-4 inline mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                </svg>
                Edit
              </button>
              <button
                onClick={onDelete}
                className={`
                  px-3 py-1.5 rounded-lg text-sm font-medium transition-all duration-200
                  hover:scale-105 hover:shadow-lg
                  bg-red-600/20 hover:bg-red-600/30
                  text-red-400 hover:text-red-300
                  border border-red-600/30 hover:border-red-500/50
                `}
              >
                <svg className="w-4 h-4 inline mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                </svg>
                Delete
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
