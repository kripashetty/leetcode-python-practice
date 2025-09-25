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

### Adding a New Solution

1. Create a new Python file in the appropriate difficulty folder under `solutions/`
2. Add corresponding test file in `tests/`
3. Run tests:
   ```bash
   poetry run pytest tests/
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

## License

This project is open source and available under the MIT License.
