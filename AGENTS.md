# AGENTS.md

## Cursor Cloud specific instructions

This is a minimal Python repository containing merge sort algorithm implementations (`merge_sort.py` and `merge_sort2.py`). There are no external dependencies, no build system, and no package manager.

- **Runtime**: Python 3.6+ (only standard library used).
- **Run scripts**: `python3 merge_sort.py` or `python3 merge_sort2.py` — each runs built-in test cases and prints results.
- **Lint**: No linter configured. You may run `python3 -m py_compile merge_sort.py` to syntax-check.
- **Tests**: No test framework. The `if __name__ == "__main__"` block in each file serves as the test suite.
- **No services to start**: This repo has no servers, databases, or background processes.
