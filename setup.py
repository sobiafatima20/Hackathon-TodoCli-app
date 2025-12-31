#!/usr/bin/env python
"""
Setup file for the Todo CLI Application.
This file is included for compatibility with older Python packaging tools.
"""

from setuptools import setup, find_packages

setup(
    name="todo-cli-app",
    version="0.1.0",
    description="A simple CLI todo application with in-memory storage",
    author="Todo App Team",
    author_email="todo@example.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "todo=src.cli.main:main",
        ],
    },
    python_requires=">=3.13",
    install_requires=[],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.13",
    ],
)