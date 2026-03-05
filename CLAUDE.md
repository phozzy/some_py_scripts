# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A collection of Python scripts implementing various algorithms, with emphasis on comparing different computational approaches (iterators, recursion, mathematical optimization, bit manipulation).

## Development Environment

This project uses Nix Flakes for reproducible development:
- Enter environment: `nix develop` or use direnv (auto-activates via `.envrc`)
- The shell hook automatically activates `.venv` and runs `uv sync`

Package management uses `uv` (fast Python package manager).

## Commands

**Run tests:**
```bash
pytest
```

**Run a single test:**
```bash
pytest test_fibonacci.py::TestGetNth::test_get_nth_0
```

**Run scripts directly:**
```bash
python fibonacci.py
python door_mat.py < input.txt
python benchmark_brackets.py
python memory_test.py
```

## Code Architecture

### Bracket Sequence Generators
Three different implementations for generating valid bracket sequences, useful for comparing algorithmic approaches:

- `brackets_generator.py` - Bit manipulation approach using binary representation
- `brackets_recursive.py` - Classic recursive backtracking
- `brackets_mathematical.py` - Catalan number-based direct access (can compute nth sequence without generating all previous)

### Core Utilities
- `fibonacci.py` - Dataclass-based infinite iterator with `get_nth()` and `fibonacci()` functions
- `door_mat.py` - ASCII pattern generator with enum-based character validation

### Benchmarking
- `benchmark_brackets.py` - Performance comparison of bracket generators
- `memory_test.py` - Memory profiling using tracemalloc

## Conventions

- Python 3.13+ required
- Uses conventional commits (`feat:`, `refactor:`, `chore:`, etc.)
- Cocogitto handles changelog generation and semantic versioning
- Type hints and docstrings expected in implementations
