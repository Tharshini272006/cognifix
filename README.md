# Cognifix

Cognifix is a command-line debugging agent that automatically detects programming errors, applies corrective fixes, and re-executes programs to validate successful execution.

The tool introduces a self-correcting execution pipeline that reduces the time developers spend identifying and fixing repetitive runtime errors.

---

# Overview

Debugging is one of the most time-consuming tasks in software development. Developers often encounter common issues such as:

* Syntax errors
* Runtime exceptions
* Undefined variables
* Logical mistakes
* Incorrect calculations

Cognifix automates this process by executing code, capturing failures, and applying automated fixes until the program runs successfully.

---

# Key Features

### Automatic Language Detection

Cognifix detects the programming language of the provided source file.

### Execution Engine

Each language is executed through a dedicated runtime engine.

### QuickFix Mode

Applies immediate fixes for common errors to restore execution quickly.

### DeepFix Mode

Performs deeper analysis of runtime errors and applies structured fixes.

### Self-Correcting Execution Loop

After each fix, Cognifix automatically re-runs the program until it executes successfully or reaches the retry limit.

### Modular Architecture

The system is designed to support additional languages and debugging strategies with minimal changes.

---

# Architecture

Cognifix follows a modular debugging pipeline.

```
Source Code
    │
    ▼
Language Detector
    │
    ▼
Execution Engine
    │
    ▼
Error Capture
    │
    ▼
Repair Strategy
(QuickFix / DeepFix)
    │
    ▼
Re-Execution
```

Each component is independent, making the system easier to extend and maintain.

---

# Project Structure

```
cognifix
│
├── main.py
│   CLI entry point
│
├── agent.py
│   Core debugging pipeline
│
├── language_detector.py
│   Language identification logic
│
├── engines
│   ├── python_engine.py
│   ├── javascript_engine.py
│   └── c_engine.py
│
├── modes
│   ├── quickfix.py
│   └── deepfix.py
│
├── test_programs
│   ├── test_code.py
│   ├── calculator_program.py
│   ├── grading_system.py
│   └── pi_program.py
│
└── README.md
```

---

# Installation

Clone the repository.

```
git clone https://github.com/Tharshini272006/cognifix.git
cd cognifix
```

Ensure the following runtimes are installed:

* Python
* Node.js (for JavaScript execution)
* GCC (for C programs)

---

# Usage

Run Cognifix from the command line.

## QuickFix Mode

```
python main.py test_programs/test_code.py --mode quickfix
```

## DeepFix Mode

```
python main.py test_programs/test_code.py --mode deepfix
```

---

# Example Execution

```
Starting Cognifix...

Detected language: python

Error detected:
ZeroDivisionError: division by zero

Applying QuickFix...

Program executed successfully
```

---

# Design Principles

**Modularity**

Execution engines and repair strategies are implemented as separate modules.

**Extensibility**

New languages and debugging strategies can be integrated without changing the core pipeline.

**Fault Tolerance**

Programs are executed multiple times until a fix succeeds or the retry limit is reached.

---

# Extending Cognifix

### Adding a New Language

1. Create a new engine inside `engines/`
2. Implement a runner function
3. Register the engine inside `agent.py`

Example:

```
engines/java_engine.py
```

---

### Adding a New Repair Strategy

Create a new debugging strategy inside the `modes/` directory and integrate it into the debugging loop.

---

# Future Improvements

* AI-assisted debugging using LLMs
* IDE integrations (VS Code extension)
* Static code analysis
* GitHub pull request auto-repair bot
* Support for additional programming languages

---

# Author

Tharshini
GitHub: https://github.com/Tharshini272006

---

# License

This project is released under the MIT License.

