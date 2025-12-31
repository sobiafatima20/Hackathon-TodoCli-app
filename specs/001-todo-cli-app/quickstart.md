# Quickstart Guide: The Evolution of Todo – Phase I (In-Memory Python Console Application)

**Date**: 2025-12-28
**Feature**: The Evolution of Todo – Phase I (In-Memory Python Console Application)
**Branch**: 001-todo-cli-app

## Getting Started

### Prerequisites
- Python 3.13+
- UV package manager (for environment management)

### Setup
1. Clone the repository
2. Navigate to the project directory
3. Set up the virtual environment:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
4. Install dependencies (if any beyond standard library)

### Running the Application
```bash
cd src/cli
python main.py --help
```

### Basic Usage Examples

**Add a new task:**
```bash
python main.py add --title "Buy groceries" --description "Milk, eggs, bread"
```

**View all tasks:**
```bash
python main.py view
```

**Mark a task as complete:**
```bash
python main.py complete 1
```

**Mark a task as incomplete:**
```bash
python main.py incomplete 1
```

**Update a task:**
```bash
python main.py update 1 --title "Buy groceries and cook dinner"
```

**Delete a task:**
```bash
python main.py delete 1
```

## Project Structure
```
src/
├── models/
│   └── task.py              # Task data model
├── services/
│   └── task_manager.py      # Task management logic
└── cli/
    └── main.py              # Command-line interface
```

## Development
- All code follows PEP 8 conventions
- Run tests with: `python -m unittest discover tests/`
- The application stores all data in memory only (no persistence)