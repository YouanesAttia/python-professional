# 🐍 Python Professional

A structured deep-dive into Python at the engineering level — not tutorials, not bootcamp syntax, but the internals and patterns that separate Python users from Python engineers.

Built as part of a deliberate 90-day technical preparation plan alongside C++ systems programming, data structures, and machine learning foundations.

---

## What This Is

Most Python resources teach you to use the language. This repo is about understanding it.

Every file here covers a concept from _Fluent Python_ (Luciano Ramalho) implemented from scratch — dunder methods, the data model, closures, decorators, generators, type hints — the things that make production Python codebases readable and maintainable.

---

## Structure

```
python-professional/
├── week5_python_core/
│   ├── day31_data_model.py         # FrenchDeck, Vector2D — dunder methods
│   ├── day32_sequences.py          # Comprehensions, generators, tuple unpacking
│   ├── day33_dicts_sets.py         # Counter, defaultdict, LRU cache from scratch
│   ├── day34_decorators.py         # @timer, @debug, @retry, @cache, @property
│   ├── day35_generators_context.py # Infinite generators, lazy file reader, context managers
│   └── day36_types_testing.py      # Type hints, mypy, pytest patterns
├── week6_data_science/             # NumPy, Pandas, Matplotlib, Seaborn (in progress)
├── week7_ml_foundations/           # Linear regression, logistic regression, trees (in progress)
├── week8_neural_nets/              # Backprop from scratch, MNIST, PyTorch (in progress)
└── projects/                       # Standalone projects built from these foundations
```

---

## Week 5 — Python Core Concepts

### Day 31 — The Python Data Model

Implementing `__len__`, `__getitem__`, `__repr__`, `__add__`, `__mul__`, `__bool__` on custom classes.

Key insight: implementing two dunder methods on `FrenchDeck` gives you iteration, slicing, sorting, and `in` operator support entirely for free — without inheriting from anything. That's Python's data model.

### Day 32 — Sequences

List comprehensions vs generator expressions — same syntax, completely different memory behavior. `sys.getsizeof()` benchmark showing 100x+ memory difference. Tuple unpacking with `*` operator. Pure slice-based card dealing.

### Day 33 — Dictionaries and Sets

Python's `dict` is a hash table — the same one you implemented in C++ in Month 1. Here: `collections.Counter`, `defaultdict`, `OrderedDict`. LRU Cache built manually before touching `functools.lru_cache`. Two-sum in one line using dict lookup.

### Day 34 — Decorators and Closures

Four decorators built from scratch:

- `@timer` — measures execution time of any function
- `@debug` — prints name, arguments, and return value on every call
- `@retry(n)` — retries up to n times on exception, with exponential backoff
- `@cache` — manual memoization using a dict (what `functools.lru_cache` does internally)
  Stacked decorator execution order traced explicitly. `@property` on a `Circle` class — `radius` settable, `area` and `circumference` computed.

---

## Background

This repo is Week 5 of a 90-day summer plan covering:

- **Month 1:** C++17, data structures from scratch, algorithms, Linux systems programming
- **Month 2:** Professional Python, data science, machine learning from first principles
- **Month 3:** Capstone projects, interview preparation, professor research outreach
  Parallel work: 100+ LeetCode problems, 4 deployed Flask applications, neural network implemented from scratch using only NumPy.

---

## Running the Code

```bash
git clone https://github.com/YouanesAttia/python-professional
cd python-professional
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Run any file directly:

```bash
python week5_python_core/day31_data_model.py
```

Run tests:

```bash
pytest week5_python_core/ -v
```

Type check:

```bash
mypy week5_python_core/day36_types_testing.py
```

---

## Resources

- _Fluent Python_ — Luciano Ramalho (primary reference)
- _Python for Data Analysis_ — Wes McKinney (Week 6)
- CS50P — Harvard's Python course (certificate earned)
- Corey Schafer Python tutorials — youtube.com/@coreyms

---

_Part of a larger 90-day engineering preparation plan. See also:_
_[summer-2026-dsa](https://github.com/YouanesAttia/summer_2026_dsa) — C++ DSA practice_
_[cli-task-manager](#) — Python CLI + Flask API (deployed)_
_[minilm-from-scratch](#) — Neural network from scratch (coming Week 8)_
