// T041: Tasks page with TaskList and create button

'use client';

import React, { useState } from 'react';
import { useRouter } from 'next/navigation';
import { useTasks } from '@/lib/hooks/useTasks';
import { TaskList } from '@/components/tasks/TaskList';

export default function TasksPage() {
  const router = useRouter();
  const {
    tasks,
    loading,
    error,
    pagination,
    toggleComplete,
    deleteTask: handleDeleteTask,
    goToPage,
  } = useTasks();

  const [deletingTaskId, setDeletingTaskId] = useState<string | null>(null);

  const handleDelete = async (taskId: string) => {
    if (confirm('Are you sure you want to delete this task?')) {
      try {
        setDeletingTaskId(taskId);
        await handleDeleteTask(taskId);
      } catch (error) {
        console.error('Failed to delete task:', error);
      } finally {
        setDeletingTaskId(null);
      }
    }
  };

  return (
    <div className="max-w-6xl mx-auto">
      {/* Header */}
      <div className="flex items-center justify-between mb-10">
        <div>
          <h2 className="text-4xl font-bold text-white mb-2">My Tasks</h2>
          <p className="text-gray-400 text-base">Manage and organize your tasks efficiently</p>
        </div>
        <button
          onClick={() => router.push('/tasks/create')}
          className="px-6 py-3 rounded-xl bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-500 hover:to-purple-500 text-white font-semibold transition-all duration-300 hover:shadow-lg hover:scale-105"
        >
          <span className="mr-2">➕</span> Create Task
        </button>
      </div>

      {/* Task list */}
      <div className="bg-gradient-to-br from-gray-900/50 to-gray-950/50 rounded-3xl border border-gray-700/50 backdrop-blur-sm p-6">
        <TaskList
          tasks={tasks}
          loading={loading}
          error={error}
          pagination={{
            ...pagination,
            pageSize: 10,
            totalItems: pagination.totalTasks,
            canGoBack: pagination.hasPrevPage,
            canGoForward: pagination.hasNextPage
          }}
          onPageChange={goToPage}
          onToggleComplete={toggleComplete}
          onEdit={(taskId) => router.push(`/tasks/${taskId}`)}
          onDelete={handleDelete}
          onCreateTask={() => router.push('/tasks/create')}
        />
      </div>
    </div>
  );
}
