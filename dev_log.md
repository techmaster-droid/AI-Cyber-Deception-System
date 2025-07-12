# Development Log - AI-Driven Cyber Deception System

---

## Day 1 - July 9, 2025

**Planned for Today:**
* Understand project goals.
* Install Miniconda.
* Install VS Code.
* Set up Git and create GitHub repo.
* Clone repo locally.
* Make first commit/push.
* Create dev_log.md.

**Accomplished:**
* Successfully installed Miniconda (verified with `conda --version` and `python --version` in Anaconda Prompt).
* Installed Visual Studio Code with Python extension.
* Installed Git for Windows.
* Configured Git user name and email.
* Created `AI-Cyber-Deception-System` public repository on GitHub with `README.md` and Python `.gitignore`.
* Cloned the repo to `D:\MyCodingProjects\AI-Cyber-Deception-System`.
* Created `day1_test.py` and successfully performed first `git add .`, `git commit`, and `git push origin main`. Verified on GitHub.
* Created `dev_log.md` file.

**New Concepts/Tools Learned:**
* **Miniconda:** Lightweight `conda` distribution, basic installation.
* **VS Code:** Basic installation, opening folders.
* **Git:** Installation, global configuration (`user.name`, `user.email`).
* **GitHub:** Account creation, new repository setup (public, `README`, `.gitignore`).
* **Git Commands:** `git clone`, `git status`, `git add .`, `git commit -m`, `git push origin main`.
* **Command Line Navigation (Windows):** `D:` to switch drives, `cd /D D:\path` or `D:` then `cd path` to navigate across drives.

**Challenges/Roadblocks:**
* Initial `git config` error: `'git' is not recognized...` - **Resolved by closing and reopening Anaconda Prompt** after Git installation to refresh PATH.
* `cd D:\path` not changing drive: **Resolved by first typing `D:` to switch drives**, then `cd path` within the D: drive.
* Getting used to the Git authentication prompt via browser during `git push`.

**Questions/Thoughts:**
* Need to review Python basics more thoroughly tomorrow.
* Excited to start with Conda environments and project structure.
* Need to plan for future storage expansion (external drive) as VMs and data will consume significant space.

**Next Steps (for Day 2 - July 10, 2025):**
* Review Python basics (data types, control flow, functions, basic OOP).
* Create and activate a specific Conda environment for the project within the project folder.
* Practice running simple Python scripts in VS Code using the new environment.

---

## Day 2 - July 10, 2025

**Planned for Today:**
* Refresh Python basics (data types, operators, control flow, functions, basic OOP).
* Understand and create a Conda virtual environment (`cyber_ai_env`).
* Activate/deactivate the environment.
* Integrate environment with VS Code.
* Update dev_log and commit.

**Accomplished:**
* Refreshed Python basics by creating and running `python_refresher.py` (data types, operators, control flow, functions, basic OOP).
* Understood the purpose of virtual environments for dependency management.
* Successfully created `cyber_ai_env` with Python 3.9 using `conda create`.
* Activated `cyber_ai_env` and verified it with `python --version` and `conda list`.
* Successfully selected `cyber_ai_env` as the interpreter in VS Code.

**New Concepts/Tools Learned:**
* **Python Refresher:** Re-familiarized with core Python syntax and concepts.
* **Virtual Environments:** Concept of isolated environments for projects.
* **Conda Commands:** `conda create -n env_name python=X.X`, `conda activate env_name`, `conda deactivate`, `conda list`.
* **VS Code Interpreter Selection:** How to link VS Code to a specific Conda environment.
* **Logical `and` operator:** Clarified behavior (true only if both are true).
* **`__init__` method:** Understood its role as constructor and that its name is fixed.

**Challenges/Roadblocks:**
* Initial confusion with the `condition1 and condition2` output, which was clarified.
* Questioned fixed name of `__init__`, which was also clarified.
* *(Add any other small issues you faced or concepts you found challenging today)*

**Questions/Thoughts:**
* Excited to start installing actual project libraries in the `cyber_ai_env` tomorrow.
* Good to have the Python basics refreshed.

**Next Steps (for Day 3 - July 11, 2025):**
* Begin installing initial project dependencies (e.g., NumPy, Pandas) into `cyber_ai_env`.
* Start structuring the project folders for code and data.
* Begin foundational coding for the project.

---

## Day 3 - July 12, 2025

**Planned for Today:**
* Review Day 2 dev_log.
* Create standard project folder structure (src, data, notebooks, models, config, tests, logs).
* Install initial core Python libraries (numpy, pandas) into cyber_ai_env.
* Create requirements.txt to manage dependencies.
* Start writing basic utility functions in utils.py.
* Set up basic logging for the project.
* Update dev_log and commit.

**Accomplished:**
* Reviewed Day 2 summary.
* Created core project directories: `src/`, `data/` (with `raw/`, `processed/`, `simulated/`), `notebooks/`, `models/`, `config/`, `tests/`.
* Successfully installed `numpy` and `pandas` into `cyber_ai_env` using `pip install`.
* Generated `requirements.txt` using `pip freeze > requirements.txt`, capturing installed dependencies.
* Created `src/utils.py` with a `setup_logging` function.
* Successfully tested the `setup_logging` function, verifying console output and creation of a `logs/` directory with a log file inside.

**New Concepts/Tools Learned:**
* **Project Structure:** Standard layout for AI/data science projects (`src/`, `data/`, `logs/`, etc.).
* **`pip install`**: Installing packages into a Conda environment.
* **`pip freeze > requirements.txt`**: Generating a dependency list.
* **Python `logging` module**: Basic setup for application logging (INFO, DEBUG, WARNING, ERROR, CRITICAL).
* **`os` module**: Using `os.path.join`, `os.path.abspath`, `os.path.dirname`, `os.makedirs` for path and directory manipulation.
* **Debugging:** Identifying and fixing a typo in code that affected output. (Very important learning!)

**Challenges/Roadblocks:**
* Initial feeling of forgetting basic concepts, which was addressed with a quick Conda refresher.
* Clarifying the specific "forgetting" (Conda vs. Git/Python).
* **Debugging a typo in the `utils.py` logging print statement that caused the DEBUG messages not to appear initially – successfully resolved!**

**Questions/Thoughts:**
* Feeling more confident after the debugging experience and active learning.
* Ready to use these new utilities in more complex code.

**Next Steps (for Day 4 - July 13, 2025):**
* Develop a data acquisition utility (e.g., placeholder for reading initial data).
* Start defining core components of the deception system (e.g., initial `deception_module.py`).
* Continue integrating logging and project structure.

