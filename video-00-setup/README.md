# Video 00: Python Setup for Java Developers — uv, Virtual Environments, and Jupyter

> **CodeWithAzam** | Python for Senior Java Developers
>
> This guide is self-contained. If you prefer reading to watching, everything you need to get a working Python environment is right here.

---

## Table of Contents

1. [Why uv? (The 30-Second Pitch for Java Developers)](#1-why-uv-the-30-second-pitch-for-java-developers)
2. [Install uv](#2-install-uv)
3. [Install Python via uv](#3-install-python-via-uv)
4. [Create Your First Project](#4-create-your-first-project)
5. [Add Dependencies](#5-add-dependencies)
6. [Run Your First Python File](#6-run-your-first-python-file)
7. [Virtual Environments Explained](#7-virtual-environments-explained)
8. [Install and Run Jupyter Notebook](#8-install-and-run-jupyter-notebook)
9. [Verify Your Setup](#9-verify-your-setup)
10. [Quick Reference — Java to Python Tooling](#10-quick-reference--java-to-python-tooling)
11. [Troubleshooting](#11-troubleshooting)

---

## 1. Why uv? (The 30-Second Pitch for Java Developers)

If you live in Maven or Gradle, you already understand the value of a single tool that handles dependency management, version pinning, and reproducible builds. Python historically spread these responsibilities across several tools (`pip`, `venv`, `pyenv`, `pipx`…), which confused newcomers.

**uv** is the tool that finally unifies the Python ecosystem:

| What you need | Maven/Gradle equivalent | uv command |
|---|---|---|
| Install a specific runtime | SDKMAN `sdk install java 21` | `uv python install 3.12` |
| Create a project | `mvn archetype:generate` | `uv init my-project` |
| Add a dependency | Edit `pom.xml` + `mvn install` | `uv add requests` |
| Remove a dependency | Edit `pom.xml` + `mvn install` | `uv remove requests` |
| Reproduce a build exactly | `pom.xml` + Maven wrapper | `uv sync` (uses `uv.lock`) |
| Run a script | `mvn exec:java` | `uv run python script.py` |

**Why is uv faster?** It is written in Rust and resolves dependencies in parallel. Installing a package that would take `pip` 30 seconds typically takes uv under 1 second.

Official docs: <https://docs.astral.sh/uv/>

---

## 2. Install uv

### macOS / Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Windows (PowerShell — run as normal user, no admin required)

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### After installation

Close and reopen your terminal (uv adds itself to `PATH` via your shell profile), then verify:

```bash
uv --version
# uv 0.5.x (or later)
```

> **Note:** If `uv` is not found after reopening the terminal, see [Troubleshooting](#11-troubleshooting).

---

## 3. Install Python via uv

```bash
uv python install 3.12
```

This downloads and installs CPython 3.12 into uv's managed cache. It does **not** touch your system Python — the same isolation guarantee you get from SDKMAN on the Java side.

Verify the install:

```bash
uv python list
# cpython-3.12.x-...  <path>  (installed)
```

> **SDKMAN comparison:**
> `sdk install java 21.0.3-tem` → `uv python install 3.12`
> `sdk use java 21.0.3-tem`     → `uv python pin 3.12` (pins version for current project)

You can install multiple versions and switch per-project:

```bash
uv python install 3.11
uv python install 3.13
```

---

## 4. Create Your First Project

```bash
uv init my-first-python-project
cd my-first-python-project
```

uv generates this structure:

```
my-first-python-project/
├── pyproject.toml   <-- the pom.xml of Python
├── hello.py
├── .python-version  <-- pins the Python version (like .java-version for jenv)
└── .venv/           <-- auto-created virtual environment (like target/, do not commit)
```

### pyproject.toml mapped to pom.xml

```toml
[project]
name = "my-first-python-project"      # <artifactId>
version = "0.1.0"                     # <version>
description = "Add your description"  # <description>
requires-python = ">=3.12"            # <java.version> in properties

dependencies = []                     # <dependencies> section
```

```toml
[build-system]
requires = ["hatchling"]              # <build> / <plugins> section
build-backend = "hatchling.build"
```

There is no `groupId` concept by default — PyPI packages are identified by name alone.

---

## 5. Add Dependencies

### Java (Maven)

```xml
<!-- 1. Edit pom.xml -->
<dependency>
    <groupId>com.google.code.gson</groupId>
    <artifactId>gson</artifactId>
    <version>2.10.1</version>
</dependency>

<!-- 2. Run: -->
<!-- mvn install -->
```

### Python (uv)

```bash
uv add requests
```

That single command:
1. Resolves the latest compatible version of `requests`
2. Downloads and installs it into `.venv/`
3. Adds it to `pyproject.toml` under `[project] dependencies`
4. Updates `uv.lock` with the exact resolved versions of all transitive dependencies

**Remove a dependency:**

```bash
uv remove requests
```

**Install everything from an existing project** (equivalent to `mvn install` on a cloned repo):

```bash
uv sync
```

---

## 6. Run Your First Python File

### Java

```bash
javac Hello.java      # compile
java Hello            # run
```

### Python with uv

```bash
uv run python hello.py
```

There is **no compile step**. `uv run` ensures the correct virtual environment is activated before running your script, so you never need to manually activate `.venv`.

**Pass arguments:**

```bash
uv run python hello.py --name Azam
```

**Run a one-liner (Python's equivalent of `java -e`):**

```bash
uv run python -c "print('Hello from the command line')"
```

**Start the interactive REPL (equivalent of `jshell`):**

```bash
uv run python
```

---

## 7. Virtual Environments Explained

A virtual environment (`.venv`) is an isolated copy of the Python interpreter plus its installed packages. It is Python's answer to the classpath isolation problem.

### ASCII diagram — two projects, two isolated environments

```
/home/azam/projects/
|
+-- project-alpha/
|   +-- pyproject.toml  (depends on requests==2.31)
|   +-- .venv/
|       +-- lib/
|           +-- requests-2.31/    <-- only project-alpha sees this
|
+-- project-beta/
    +-- pyproject.toml  (depends on requests==2.28)
    +-- .venv/
        +-- lib/
            +-- requests-2.28/    <-- only project-beta sees this
```

Without virtual environments, all packages would be installed globally and version conflicts would be inevitable — the same problem you face without a proper build tool on the Java side.

### Rules (same as Maven's `target/`)

- `.venv/` is **auto-created** by `uv sync` or `uv add`
- **Do not commit** `.venv/` — add it to `.gitignore`
- Anyone who clones the repo runs `uv sync` to recreate it
- `uv.lock` is the equivalent of a fully resolved `pom.xml` dependency tree — **commit this file**

### Manual activation (only needed if you are not using `uv run`)

```bash
# macOS / Linux
source .venv/bin/activate

# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1

# Windows (cmd.exe)
.\.venv\Scripts\activate.bat
```

Once activated, plain `python` and `pip` commands use the virtual environment automatically.

---

## 8. Install and Run Jupyter Notebook

Java has no direct equivalent to Jupyter. The closest analogy is a combination of a REPL, a scratchpad, and a document — all in one browser-based interface.

### Install Jupyter

```bash
uv add jupyter
```

### Launch the notebook server

```bash
uv run jupyter notebook
```

This opens your default browser at `http://localhost:8888`. If the browser does not open automatically, copy the URL (including the token) from the terminal output.

### Open the starter notebook

In the Jupyter file browser, navigate to `video-00-setup/` and open `hello_java_dev.ipynb`.

### Basic Jupyter keyboard shortcuts

| Action | Shortcut |
|---|---|
| Run current cell | `Shift + Enter` |
| Run cell, stay on same cell | `Ctrl + Enter` |
| Insert cell below | `B` (in command mode) |
| Insert cell above | `A` (in command mode) |
| Delete cell | `DD` (in command mode) |
| Switch to command mode | `Esc` |
| Switch to edit mode | `Enter` |
| Restart kernel | `00` (in command mode) |

### Stop the server

Press `Ctrl + C` in the terminal where `jupyter notebook` is running.

---

## 9. Verify Your Setup

Run the verification script to confirm everything is working:

```bash
uv run python verify_setup.py
```

Expected output (all items showing `[OK]`):

```
=== Python Environment ===
  Location : /path/to/.venv/bin/python
  Version  : 3.12.x
  [OK]   Python >= 3.10 (required for match/case in later videos) -- 3.12.x

=== Virtual Environment ===
  [OK]   Running inside a virtual environment

=== Standard Library Imports ===
  [OK]   import json
  [OK]   import os
  ...

=== Network Check ===
  [OK]   HTTP request to httpbin.org/get -- origin=x.x.x.x

=== Summary ===
  All 10/10 checks passed. You are ready for the series!
```

If any check shows `[FAIL]`, see [Troubleshooting](#11-troubleshooting) below.

---

## 10. Quick Reference — Java to Python Tooling

See [`cheatsheet.md`](./cheatsheet.md) for the full reference. Key mappings:

| Task | Java / Maven | Python / uv |
|---|---|---|
| Install runtime | SDKMAN `sdk install java 21` | `uv python install 3.12` |
| Create project | `mvn archetype:generate` | `uv init my-project` |
| Config file | `pom.xml` | `pyproject.toml` |
| Add dependency | Edit `pom.xml` + `mvn install` | `uv add requests` |
| Lock file | `pom.xml` (exact versions) | `uv.lock` |
| Local dep cache | `~/.m2/repository/` | `~/.cache/uv/` |
| Run code | `javac App.java && java App` | `uv run python app.py` |
| REPL | `jshell` | `uv run python` |
| Run tests | `mvn test` | `uv run pytest` |

---

## 11. Troubleshooting

### `uv: command not found` (macOS/Linux)

The install script adds uv to `~/.local/bin`. Make sure this is in your `PATH`:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Add that line to `~/.bashrc` or `~/.zshrc` to make it permanent, then run `source ~/.bashrc`.

### `uv: command not found` (Windows)

uv installs to `%USERPROFILE%\.local\bin`. If the installer did not update your `PATH` automatically:

1. Open **System Properties → Environment Variables**
2. Under **User variables**, edit `Path`
3. Add `%USERPROFILE%\.local\bin`
4. Restart your terminal

### `python: command not found` inside a project

You need to let uv manage the Python binary for you. Either:

```bash
uv run python        # preferred — no activation needed
# OR
source .venv/bin/activate && python   # manual activation
```

Plain `python` or `python3` refers to the system Python (or nothing, on Windows), not your project's Python.

### Jupyter does not open in the browser

Copy the full URL including the token from the terminal — it looks like:

```
http://127.0.0.1:8888/tree?token=abc123...
```

Paste it directly into your browser. Chrome and Firefox work best.

### Windows: execution policy error when activating `.venv`

If you see `cannot be loaded because running scripts is disabled on this system`:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

This is a one-time change scoped to your user account only. It does not affect system-wide policy.

### `sudo pip install` on macOS — permission errors

Never use `sudo pip install`. It installs packages into the system Python and can break macOS tools that depend on it. Always work inside a virtual environment via uv:

```bash
uv add <package>      # adds to .venv — no sudo, no system pollution
```

### `uv sync` fails with "no solution found"

This usually means your `requires-python` in `pyproject.toml` conflicts with the installed Python version. Check:

```bash
uv python list           # see what is installed
cat pyproject.toml       # check requires-python field
uv python install 3.12   # install the required version
uv sync                  # retry
```

---

## Ready? Let's code.

- **Next video:** [Video 01 — Python Syntax Crash Course](../video-01-syntax-basics/README.md)
- **Practice exercises:** [video-01-syntax-basics/practice.ipynb](../video-01-syntax-basics/practice.ipynb)
- **Full series:** [Main repo README](../README.md)
- **YouTube:** [CodeWithAzam](https://youtube.com/@CodeWithAzam)
- **uv docs:** [docs.astral.sh/uv](https://docs.astral.sh/uv/)
