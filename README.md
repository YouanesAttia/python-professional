# 🐍 Python Professional

A structured deep-dive into Python at the engineering level — not tutorials, not bootcamp syntax, but the internals and patterns that separate Python users from Python engineers.

Built as part of a deliberate 90-day technical preparation plan alongside C++ systems programming, data structures, and machine learning foundations.

---

## What This Is

Most Python resources teach you to use the language. This repo is about understanding it.

Week 5 covers Python internals from _Fluent Python_ (Luciano Ramalho) — implemented from scratch. Week 6 covers data science foundations using NumPy, Pandas, Matplotlib, and Seaborn on real datasets.

---

## Structure

```
python-professional/
├── week5_python_core/
│   ├── day31_data_model.py          # FrenchDeck, Vector2D — dunder methods
│   ├── day32_sequences.py           # Comprehensions, generators, tuple unpacking
│   ├── day33_dicts_sets.py          # Counter, defaultdict, LRU cache from scratch
│   ├── day34_decorators.py          # @timer, @debug, @retry, @cache, @property
│   ├── day35_generators_context.py  # Infinite generators, lazy file reader, context managers
│   └── day36_types_testing.py       # Type hints, mypy, pytest patterns
└── week6_data_science/
    ├── 01_numpy_basics.ipynb        # Array creation, broadcasting, vectorization, linear algebra
    ├── 02_pandas_basics.ipynb       # DataFrames, loc/iloc, missing data, filtering
    ├── 03_pandas_advanced.ipynb     # GroupBy, merge/join, pivot tables, apply
    └── 04_visualization.ipynb       # Matplotlib subplots, Seaborn statistical plots, EDA charts
```

---

## Week 5 — Python Core Concepts

### Day 31 — The Python Data Model

Implementing `__len__`, `__getitem__`, `__repr__`, `__add__`, `__mul__`, `__bool__` on custom classes.

Key insight: two dunder methods on `FrenchDeck` give you iteration, slicing, sorting, and `in` operator support for free — without inheriting from anything. That is Python's data model.

### Day 32 — Sequences

List comprehensions vs generator expressions — same syntax, completely different memory behavior. `sys.getsizeof()` benchmark showing the difference. Tuple unpacking with `*`. Pure slice-based card dealing with no loops.

### Day 33 — Dictionaries and Sets

`collections.Counter`, `defaultdict`, `OrderedDict`. LRU Cache built manually before touching `functools.lru_cache`. Two-sum in O(n) using dict lookup. Python's `dict` is a hash table — the same one implemented in C++ in Month 1 of the plan, now seen from a different angle.

### Day 34 — Decorators and Closures

Four decorators built from scratch:

- `@timer` — measures execution time of any function
- `@debug` — prints name, arguments, and return value on every call
- `@retry(n)` — retries up to n times on exception
- `@cache` — manual memoization using a dict (what `functools.lru_cache` does internally)

Stacked decorator execution order traced explicitly. `@property` on a `Circle` class.

### Day 35 — Generators, Iterators, Context Managers

- `fibonacci()` — infinite generator, never loads into memory
- `read_large_file()` — yields one line at a time from arbitrarily large files
- `integer_range()` — reimplementation of Python's `range()` as a generator
- `timer_context()` — context manager measuring time inside a `with` block
- `temp_directory()` — creates and cleans up temp directory even when exceptions occur

### Day 36 — Type Hints + Testing

Full type annotations with `mypy` static checking. `pytest` suite with `@pytest.mark.parametrize`. Pythonic rewrites of common C++ patterns.

---

## Week 6 — Data Science Foundations

### Day 38 — NumPy Basics (`01_numpy_basics.ipynb`)

Array creation, shape/dtype inspection, broadcasting rules, vectorization benchmark (Python loop vs `np.sum()` on 10M elements), boolean and fancy indexing, linear algebra operations (`np.dot`, `np.linalg.inv`, `np.linalg.eig`, `np.linalg.solve`).

### Day 39 — Pandas Basics (`02_pandas_basics.ipynb`)

Loading real datasets with `pd.read_csv()`. Deep dive into `.loc` vs `.iloc`. Boolean filtering with single and multiple conditions. Missing data — `isnull().sum()`, `fillna()`, `dropna()`. Sorting, adding/removing columns, renaming.

### Day 40 — Pandas Advanced (`03_pandas_advanced.ipynb`)

GroupBy — what it returns before aggregation (a lazy GroupBy object, not a DataFrame), single and multi-column grouping, multiple aggregations with `.agg()`, within-group normalization using `transform`. Merge — inner, left, right, outer joins. `pd.concat()`. Pivot tables. `apply()` — when to use it vs vectorized operations.

### Day 41 — Visualization (`04_visualization.ipynb`)

Matplotlib: 2×3 subplot grid covering line, bar, scatter, histogram, pie, and box plots — all labeled. Seaborn: `histplot` with KDE, `boxplot`, `heatmap(df.corr())`, `scatterplot` with hue and size encoding, `pairplot`. Insight-driven chart titles that state conclusions, not just topics.

---

## Background

This repo is part of a 90-day summer plan:

- **Month 1:** C++17, 8+ data structures from scratch, algorithms, Linux systems programming
- **Month 2 (current):** Professional Python, data science, machine learning from first principles
- **Month 3:** Capstone projects, interview preparation

Parallel work: 70+ LeetCode problems solved, 4 deployed projects, C++ DSA repo with 40+ consecutive daily commits.

---

## Running the Code

```bash
git clone https://github.com/YouanesAttia/python-professional
cd python-professional
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Run any Python file directly:

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

Open notebooks:

```bash
jupyter notebook week6_data_science/
```

---

## Resources

- _Fluent Python_ — Luciano Ramalho (Week 5 primary reference)
- _Python for Data Analysis_ — Wes McKinney (Week 6 primary reference)
- CS50P — Harvard's Python course (certificate earned)
- Corey Schafer Python tutorials — youtube.com/@coreyms

---

_See also:_
_[summer-2026-dsa](https://github.com/YouanesAttia/summer_2026_dsa) — C++ DSA practice_
_[cli-task-manager](https://github.com/YouanesAttia/cli-task-manager) — Python CLI + Flask API_
