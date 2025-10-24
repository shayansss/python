## **Basics of Testing and Coverage**

### Run All Unit Tests

```bash
python -m unittest discover -v
```

**Options:**

* `-v` — Verbose output (shows each test name and result)
* `-s tests` — Specify the test directory if not automatically discovered
* `-p '*_test.py'` — Pattern for test filenames

**Example:**

```bash
python -m unittest discover -s tests -p '*_test.py' -v
```

---

### Run a Specific Test Class or Method

```bash
python -m unittest tests.ClassTest
python -m unittest tests.ClassTest.test_method
```

*(Tip: Use the full import path relative to your repository root.)*

---

### Run Tests Inside a Jupyter Notebook

```python
import unittest
from tests import ClassTest

suite = unittest.TestLoader().loadTestsFromTestCase(ClassTest)
unittest.TextTestRunner(verbosity=2).run(suite)
```

---

### Measure Code Coverage

Install the `coverage` library (if not already installed):

```bash
pip install coverage
```

Run coverage on the entire project:

```bash
coverage run -m unittest discover -v
```

Generate a terminal report:

```bash
coverage report -m
```

Or generate an HTML report:

```bash
coverage html
```

Open the resulting report (Linux):

```bash
xdg-open htmlcov/index.html
```

*(On Windows, use `start htmlcov/index.html`; on macOS, use `open htmlcov/index.html`.)*

---

### Limit Coverage to a Specific Module

To focus coverage analysis on a specific file or package:

```bash
coverage run --source=module/file.py -m unittest discover
coverage report -m
```

Or from Python:

```python
import warnings
from coverage import Coverage
from coverage.exceptions import CoverageWarning

# Suppress include/source overlap warnings
warnings.filterwarnings("ignore", category=CoverageWarning)

cov = Coverage(source=['caemate/calcs/modalanalysis/twinwrappers/viadottoparchi.py'])
cov.start()

# Run your tests here
unittest.TextTestRunner(verbosity=2).run(suite)

cov.stop()
cov.save()
cov.report(show_missing=True)
```

---

### Combine Coverage from Multiple Runs

When tests are distributed across different environments (e.g., unit and integration layers):

```bash
coverage combine
coverage report -m
```

This merges all `.coverage.*` data files into a single combined result.

<!--

### Suggested Documentation Note

> **Testing and Coverage**
>
> To ensure consistent quality, run all tests using:
>
> ```bash
> python -m unittest discover -v
> ```
>
> To measure code coverage:
>
> ```bash
> coverage run -m unittest discover && coverage report -m
> ```
>
> For detailed per-line results, open the generated HTML report:
>
> ```bash
> coverage html && xdg-open htmlcov/index.html
> ```


Excellent question — since you’re building a **public GitHub knowledge base** (for yourself and others), it’s worth organizing your testing and coverage documentation into **progressive, modular chapters** that cover everything from fundamentals to advanced automation.

Here’s a well-structured outline I’d recommend, tailored to your technical level and CAEmate’s engineering environment.

---

## 🧭 Suggested Chapters for a Public “Testing & Coverage” Guide

### **Chapter 2 – Intermediate Testing and Mocking**

Focus: robust, isolated, deterministic tests.

* Difference between **unit**, **integration**, and **system** tests
* Using `unittest.mock` (`patch`, `Mock`, `MagicMock`, `call`, `side_effect`)
* Mocking external dependencies (files, network, logger, hardware sensors)
* Asserting mock calls (`assert_called_once_with`, etc.)
* Avoiding flaky tests (randomness, time-based values)
* Example: testing an OMA pipeline with mocked `advancedOma`

---

### **Chapter 3 – Coverage Analysis and Reporting**

Focus: deeper control and interpretation.

* Understanding “missed lines” and branches
* Excluding lines from coverage (`# pragma: no cover`)
* Merging coverage from CI pipelines
* Generating detailed HTML and XML reports
* Interpreting coverage metrics (statements, branches, partials)
* Best practices for meaningful coverage (quality > quantity)

---

### **Chapter 4 – Advanced Testing Patterns**

Focus: scaling and structuring larger projects.

* Organizing test suites by module hierarchy
* Using test parameterization (`subTest`, `parameterized`, `pytest.mark.parametrize`)
* Reusable base test classes (e.g., for twin wrappers)
* Temporary files and cleanup (`tempfile`, `tearDown`)
* Parallel or distributed testing (`pytest-xdist`, multiprocessing)
* Memory-safe teardown and resource cleanup (`destroy()`)

---

### **Chapter 5 – Continuous Integration (CI) and Badges**

Focus: automating tests and coverage in pipelines.

* Example GitHub Actions YAML for `unittest + coverage`
* Enforcing minimum coverage thresholds
* Uploading reports to Codecov or Coveralls
* Generating badges for README (build + coverage status)
* Nightly test runs and artifact storage

---

### **Chapter 6 – Debugging and Profiling Tests**

Focus: test diagnosis and performance.

* Increasing verbosity and traceback depth
* Selective test reruns (`-k` filters)
* Profiling slow tests (`cProfile`, `pytest-profiling`)
* Measuring test memory usage
* Detecting test pollution and side-effects

---

### **Other Possible topics**

You could later extend the documentation with:

* **Testing numerical algorithms:** tolerances, floating-point precision, deterministic seeds.
* **Data validation testing:** ensuring schema consistency for sensor/OMA datasets.
* **Regression testing:** baseline comparisons between versions.
* **Visualization testing:** verifying Matplotlib output structure (not appearance).

-->
