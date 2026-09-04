# Task Tracker CLI

A simple command-line task manager built with Python.
This project was created as a beginner Python project to practice working with the command line, files, JSON, functions, and Git.

## Features

- Add new tasks
- Update existing tasks
- Delete tasks
- Mark tasks as in progress
- Mark tasks as done
- List all tasks
- Filter tasks by status
- Automatically reuse deleted task IDs
- Store tasks in a JSON file

## Installation

Clone the repository and navigate to the project directory:

```bash
git clone <repository-url>
cd task-tracker-cli
```

Install the project:

```bash
pip install -e .
```

After installation, the `task-cli` command can be used from the terminal.

## Usage

### Add a task

```bash
task-cli add "Learn Python"
```

### Update a task

```bash
task-cli update 1 "Learn Python functions"
```

### Delete a task

```bash
task-cli delete 1
```

### Mark a task as in progress

```bash
task-cli mark-in-progress 1
```

### Mark a task as done

```bash
task-cli mark-done 1
```

### List all tasks

```bash
task-cli list
```

### List completed tasks

```bash
task-cli list-done
```

### List pending tasks

```bash
task-cli list-to-do
```

### List tasks in progress

```bash
task-cli list-in-progress
```

### Show help

```bash
task-cli help
```

## Technologies

- Python
- JSON
- Git & GitHub

## Project Structure

```text
task-tracker-cli/
├── main.py
├── pyproject.toml
├── README.md
└── .gitignore
```

## Status

This project is complete as a beginner Python CLI project.

## Project URL

https://roadmap.sh/projects/task-tracker
