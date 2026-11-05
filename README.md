# *Machine Learning Check-in 1*

<a href="https://github.com/Bad0dour/MachineLearningCheckin1/archive/refs/heads/main.zip">
   <img src="distribution/download-button.svg" alt="Download" height="60">
</a>

---
### Setup

1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/):

   **macOS / Linux**
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

   **Windows**
   ```powershell
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

2. In the project folder, run:
   ```bash
   uv run Main.py
   ```

uv automatically installs Python 3.13 and the packages listed in `pyproject.toml` into a local `.venv` the first time it runs. No manual venv activation needed.

### Other files

You can ignore everything else (they're just there to keep the project set up):
- `pyproject.toml`: project info and the list of packages it needs
- `uv.lock`: the exact package versions, so everyone gets the same setup
- `.python-version`: the Python version uv uses
- `.gitignore`: files git shouldn't upload
