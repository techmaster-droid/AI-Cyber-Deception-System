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