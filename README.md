# LeetCode Python Practice

A repository for practicing LeetCode problems using Python, managed with Poetry.

## Project Structure

```
leetcode-python-practice/
├── solutions/          # Solution files organized by difficulty
│   ├── easy/
│   ├── medium/
│   └── hard/
├── tests/             # Test files for solutions
└── utils/             # Utility functions and helper classes
```

## Setup

1. Make sure you have Poetry installed:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Install dependencies:
   ```bash
   poetry install
   ```

3. Activate the virtual environment:
   ```bash
   poetry shell
   ```

## Usage

### Solution Organization

Each LeetCode solution is organized in its own directory under the appropriate difficulty level with the following structure:

```
solutions/
└── [difficulty]/
    └── [problem-number]-[problem-name]/
        ├── README.md           # Problem description, approach, and complexity analysis
        ├── solution.py         # Solution implementation
        └── test_solution.py    # Test cases
```

### Adding a New Solution

1. Copy the template from `solutions/problem_template/` to create a new solution:
   ```bash
   cp -r solutions/problem_template solutions/[difficulty]/[name]_[number]
   ```
2. Fill in the problem details in README.md
3. Implement your solution in solution.py
4. Add test cases in test_solution.py
5. Run tests:
   ```bash
   poetry run pytest solutions/[difficulty]/[name]_[number]/test_solution.py
   ```

### Code Formatting

This project uses Black for code formatting and isort for import sorting:

```bash
poetry run black .
poetry run isort .
```

### Linting

Run Flake8 for code linting:

```bash
poetry run flake8
```

## Dependencies

- Python 3.9+
- pytest for testing
- black for code formatting
- isort for import sorting
- flake8 for linting

