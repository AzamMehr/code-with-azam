# Python Tooling Cheatsheet for Java/Maven Developers

> **CodeWithAzam** — Video 00: Setup
> A side-by-side reference for developers who know Maven/Gradle and are learning Python tooling with **uv**.

---

## Section 1: Installation & Versions

| Task | Java | Python (uv) |
|---|---|---|
| Install a runtime | `sdk install java 21` (SDKMAN) | `uv python install 3.12` |
| Manage multiple versions | SDKMAN, jenv | `uv python install` (built-in to uv) |
| Check active version | `java --version` | `uv run python --version` |
| Pin version for a project | `.java-version` (jenv) | `uv python pin 3.12` → writes `.python-version` |
| List installed versions | `sdk list java` | `uv python list` |

---

## Section 2: Project Management

| Task | Java (Maven) | Python (uv) |
|---|---|---|
| Create a new project | `mvn archetype:generate` | `uv init my-project` |
| Configuration file | `pom.xml` | `pyproject.toml` |
| Add a dependency | Edit `pom.xml` + `mvn install` | `uv add requests` |
| Add a dev-only dependency | `<scope>test</scope>` in `pom.xml` | `uv add --dev pytest` |
| Remove a dependency | Edit `pom.xml` + `mvn install` | `uv remove requests` |
| Install all dependencies | `mvn install` (reads `pom.xml`) | `uv sync` (reads `uv.lock`) |
| Lock file (exact versions) | `pom.xml` with explicit versions | `uv.lock` (auto-generated — commit this) |
| Local dependency cache | `~/.m2/repository/` | `~/.cache/uv/` |
| Dependency tree | `mvn dependency:tree` | `uv tree` |
| Update all dependencies | `mvn versions:use-latest-releases` | `uv lock --upgrade` then `uv sync` |

---

## Section 3: Running Code

| Task | Java | Python (uv) |
|---|---|---|
| Run a file | `javac App.java && java App` | `uv run python app.py` |
| Run with arguments | `java App arg1 arg2` | `uv run python app.py arg1 arg2` |
| Interactive REPL | `jshell` | `uv run python` |
| Execute a one-liner | `java -e "..."` (Java 11+ source launcher, limited) | `uv run python -c "print('hello')"` |
| Run a module | `java -jar module.jar` | `uv run python -m module_name` |
| Run tests | `mvn test` | `uv run pytest` |
| Lint code | Checkstyle, SpotBugs (via Maven plugin) | `uv run ruff check .` |
| Format code | `mvn fmt:format` (google-java-format) | `uv run ruff format .` |
| Type check | Compiler (`-Xlint`), IDE inspections | `uv run mypy .` |

---

## Section 4: Project Structure Comparison

### Maven layout vs uv layout

```
Maven Project                       uv Project
-----------------------------       -----------------------------
my-app/                             my-app/
|-- pom.xml                         |-- pyproject.toml
|-- src/                            |-- uv.lock
|   |-- main/                       |-- .python-version
|   |   +-- java/                   |-- .venv/           (do not commit)
|   |       +-- com/example/        |-- src/
|   |           +-- App.java        |   +-- my_app/
|   +-- test/                       |       |-- __init__.py
|       +-- java/                   |       +-- main.py
|           +-- com/example/        +-- tests/
|               +-- AppTest.java        +-- test_main.py
+-- target/              (do not commit)
```

**Key observations:**

- `pom.xml` maps directly to `pyproject.toml`
- `uv.lock` maps to a fully-resolved `pom.xml` with exact versions — always commit it
- `.venv/` is like `target/` — auto-generated, never committed
- Python packages use snake_case directory names, not `com.example` reverse-DNS style
- `__init__.py` marks a directory as a Python package (like `package-info.java` but required)
- Tests live in `tests/` and files are prefixed with `test_` so pytest can discover them

---

## Section 5: Common uv Commands

Ten commands you will use every day:

| Command | What it does |
|---|---|
| `uv init my-project` | Creates a new project directory with `pyproject.toml`, `.venv`, and a sample `hello.py` |
| `uv python install 3.12` | Downloads and installs CPython 3.12 into uv's managed cache; does not touch system Python |
| `uv add requests` | Installs a package, adds it to `pyproject.toml`, and updates `uv.lock` |
| `uv add --dev pytest ruff mypy` | Installs dev-only tools (test runner, linter, type checker) not included in production builds |
| `uv remove requests` | Uninstalls a package and removes it from `pyproject.toml` and `uv.lock` |
| `uv sync` | Installs all dependencies from `uv.lock` — the first command to run on a cloned project |
| `uv run python script.py` | Runs a Python file using the project's virtual environment (no manual activation needed) |
| `uv run pytest` | Runs tests using the project's virtual environment |
| `uv lock --upgrade` | Re-resolves all dependencies to their latest compatible versions and rewrites `uv.lock` |
| `uv tree` | Prints the full dependency tree, including transitive dependencies |

---

## Section 6: Concepts Glossary

| Python concept | Java equivalent | Notes |
|---|---|---|
| Virtual environment (`.venv/`) | Classpath isolation / `target/` | An isolated Python interpreter + packages per project. Created by `uv sync`. Never commit it. |
| `pyproject.toml` | `pom.xml` / `build.gradle` | Declares project metadata, dependencies, Python version requirement, and build configuration. |
| `uv.lock` | Resolved `pom.xml` dependency tree / Gradle lock files | Auto-generated file with exact versions of every dependency (direct + transitive). Always commit this. |
| `__init__.py` | `package-info.java` (but required) | An empty or non-empty file that marks a directory as an importable Python package. Required in traditional packages. |
| `__pycache__/` | `.class` files in `target/` | Bytecode cache auto-generated by the Python interpreter. Add to `.gitignore`; never commit. |
| `site-packages/` | `~/.m2/repository/` jars on classpath | The directory inside `.venv/` where installed packages live. You rarely interact with it directly. |
| PyPI (pypi.org) | Maven Central (search.maven.org) | The official public package registry for Python. `uv add` downloads from here by default. |
| Wheel (`.whl`) | JAR file | A pre-built binary distribution format for Python packages. uv prefers wheels for fast installs. |
| pip | `mvn dependency:get` (low-level) | The original Python package installer. uv replaces pip for most workflows but pip remains the underlying standard. |
| REPL (`python`) | `jshell` (Java 9+) | An interactive interpreter session. Type Python expressions and see results immediately. Great for exploration. |

---

## Links

- **uv documentation:** [docs.astral.sh/uv](https://docs.astral.sh/uv/)
- **Video 00 on YouTube:** [CodeWithAzam](https://youtube.com/@CodeWithAzam)
- **Full series repo:** [github.com/AzamMehr/code-with-azam](https://github.com/AzamMehr/code-with-azam)
- **Next:** [Video 01 — Python Syntax Crash Course](../video-01-syntax-basics/README.md)
