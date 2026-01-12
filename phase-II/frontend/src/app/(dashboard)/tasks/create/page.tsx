// T052: Create task page with TaskForm

'use client';

import React, { useState } from 'react';
import { useRouter } from 'next/navigation';
import { useTasks } from '@/lib/hooks/useTasks';
import { TaskForm } from '@/components/tasks/TaskForm';
import { TaskCreateRequest } from '@/types/tasks';

export default function CreateTaskPage() {
  const router = useRouter();
  const { createTask } = useTasks();
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleSubmit = async (data: TaskCreateRequest) => {
    setIsSubmitting(true);
    try {
      await createTask({
        title: data.title,
        description: data.description || null,
      });
      router.push('/tasks');
    } catch (error) {
      console.error('Failed to create task:', error);
      setIsSubmitting(false);
      throw error;
    }
  };

  const handleCancel = () => {
    router.push('/tasks');
  };

  return (
    <div className="max-w-2xl mx-auto">
      <div className="mb-10">
        <h2 className="text-4xl font-bold text-white mb-2">Create New Task</h2>
        <p className="text-gray-400 text-base">
          Add a new task to your list. Fill in the title and optionally add a description.
        </p>
      </div>

      <div className="bg-gradient-to-br from-gray-900/70 to-gray-950/70 rounded-3xl border border-gray-700/50 backdrop-blur-sm p-8 shadow-2xl shadow-blue-500/10">
        <TaskForm
          mode="create"
          onSubmit={handleSubmit}
          onCancel={handleCancel}
          isSubmitting={isSubmitting}
        />
      </div>
    </div>
  );
}
