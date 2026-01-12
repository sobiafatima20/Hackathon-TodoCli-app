// T061: Task detail page with edit mode and delete confirmation

'use client';

import React, { useState, useEffect } from 'react';
import { useRouter, useParams } from 'next/navigation';
import { useAuth } from '@/context/AuthContext';
import { getTask } from '@/lib/api/tasks';
import { useTasks } from '@/lib/hooks/useTasks';
import { TaskForm } from '@/components/tasks/TaskForm';
import { Modal } from '@/components/ui/Modal';
import { Task, TaskUpdateRequest } from '@/types/tasks';

export default function TaskDetailPage() {
  const router = useRouter();
  const params = useParams();
  const taskId = params.taskId as string;
  const { user } = useAuth();
  const { updateTask, deleteTask } = useTasks();

  const [task, setTask] = useState<Task | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [showDeleteModal, setShowDeleteModal] = useState(false);
  const [isDeleting, setIsDeleting] = useState(false);

  useEffect(() => {
    const fetchTask = async () => {
      if (!user || !taskId) return;

      try {
        setLoading(true);
        const taskData = await getTask(user.id, taskId);
        setTask(taskData);
      } catch (err: any) {
        // Check if it's a 404 error (task not found) or 403 (forbidden)
        if (err.response?.status === 404) {
          setError('Task not found or has been deleted');
        } else if (err.response?.status === 403) {
          setError('You do not have permission to access this task');
        } else {
          setError(err.message || 'Failed to load task');
        }
      } finally {
        setLoading(false);
      }
    };

    fetchTask();
  }, [user, taskId]);

  const handleSubmit = async (data: TaskUpdateRequest) => {
    if (!taskId) return;

    setIsSubmitting(true);
    try {
      await updateTask(taskId, data);
      router.push('/tasks');
    } catch (error) {
      console.error('Failed to update task:', error);
      setIsSubmitting(false);
      throw error;
    }
  };

  const handleDelete = async () => {
    if (!taskId) return;

    setIsDeleting(true);
    try {
      await deleteTask(taskId);
      router.push('/tasks');
    } catch (error: any) {
      console.error('Failed to delete task:', error);
      setError(error.message || 'Failed to delete task');
      setIsDeleting(false);
      setShowDeleteModal(false);
    }
  };

  const handleCancel = () => {
    router.push('/tasks');
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center py-12">
        <div className="flex flex-col items-center gap-4">
          <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-500" />
          <p className="text-gray-400 text-lg">Loading task...</p>
        </div>
      </div>
    );
  }

  if (error || !task) {
    return (
      <div className="max-w-2xl mx-auto">
        <div className="bg-gradient-to-br from-red-900/30 to-red-950/30 rounded-3xl border border-red-700/50 backdrop-blur-sm p-8">
          <p className="font-semibold text-lg text-red-400 mb-2">Error loading task</p>
          <p className="text-gray-400 text-base mb-6">{error || 'Task not found'}</p>
          <button
            onClick={() => router.push('/tasks')}
            className="px-4 py-2 rounded-lg bg-gray-800/50 hover:bg-gray-700/50 text-white font-medium transition-all duration-200 hover:scale-105 border border-gray-700 hover:border-gray-600"
          >
            ← Back to Tasks
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="max-w-2xl mx-auto">
      <div className="mb-10 flex items-center justify-between">
        <div>
          <h2 className="text-4xl font-bold text-white mb-2">Edit Task</h2>
          <p className="text-gray-400 text-base">
            Update the task details or delete it.
          </p>
        </div>
        <button
          onClick={() => setShowDeleteModal(true)}
          className="px-4 py-2 rounded-lg bg-gradient-to-r from-red-600/20 to-red-700/20 hover:from-red-600/30 hover:to-red-700/30 text-red-400 font-medium transition-all duration-200 hover:scale-105 border border-red-600/30 hover:border-red-500/50"
        >
          Delete Task
        </button>
      </div>

      <div className="bg-gradient-to-br from-gray-900/70 to-gray-950/70 rounded-3xl border border-gray-700/50 backdrop-blur-sm p-6 shadow-2xl shadow-blue-500/10">
        <TaskForm
          mode="edit"
          initialData={task}
          onSubmit={handleSubmit}
          onCancel={handleCancel}
          isSubmitting={isSubmitting}
        />
      </div>

      {/* Delete confirmation modal */}
      <Modal
        isOpen={showDeleteModal}
        title="Delete Task?"
        onClose={() => setShowDeleteModal(false)}
        actions={
          <>
            <button
              onClick={() => setShowDeleteModal(false)}
              disabled={isDeleting}
              className="px-4 py-2 rounded-lg bg-gray-800/50 hover:bg-gray-700/50 text-white font-medium transition-all duration-200 hover:scale-105 border border-gray-700 hover:border-gray-600 disabled:opacity-50"
            >
              Cancel
            </button>
            <button
              onClick={handleDelete}
              disabled={isDeleting}
              className="px-4 py-2 rounded-lg bg-gradient-to-r from-red-600 to-red-700 hover:from-red-500 hover:to-red-600 text-white font-medium transition-all duration-200 hover:scale-105 disabled:opacity-50"
            >
              {isDeleting ? 'Deleting...' : 'Delete'}
            </button>
          </>
        }
      >
        <p className="text-sm text-gray-300">
          Are you sure you want to delete this task? This action cannot be undone.
        </p>
        <div className="mt-3 bg-gray-800/50 p-4 rounded-xl border border-gray-700/50">
          <p className="font-medium text-white">{task.title}</p>
          {task.description && (
            <p className="text-sm text-gray-400 mt-1">{task.description}</p>
          )}
        </div>
      </Modal>
    </div>
  );
}
