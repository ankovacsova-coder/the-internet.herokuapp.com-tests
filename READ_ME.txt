# The Internet - Playwright Test Suite

Automated test suite for [the-internet.herokuapp.com](https://the-internet.herokuapp.com)
built with **Python** and **Playwright**.

---

## 📋 Prerequisites

Before you begin, make sure you have the following installed:

- [Python 3.8+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)
- A terminal / command prompt

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/the-internet-tests.git
cd the-internet-tests
```

### 2. Create and activate a virtual environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Playwright browsers

```bash
playwright install
```

### 5. Configure environment variables

Copy the example environment file and add your credentials:

**Windows (PowerShell):**
```powershell
Copy-Item enviroment.env.example.py enviroment.env
```

**macOS / Linux:**
```bash
cp enviroment.env.example.py enviroment.env
```

Then open `enviroment.env` and update with actual credentials:

```python
# Basic Authentication Credentials
BASIC_AUTH_USERNAME=*****
BASIC_AUTH_PASSWORD=*****
```

> ⚠️ **Important:** Never commit `enviroment.env` to version control!


### 6. Configure the project (Optional)

Open `config.py` and adjust settings to your preference:

```python
BASE_URL = "https://the-internet.herokuapp.com"
BROWSER = "chromium"   # Options: "chromium", "firefox", "webkit"
HEADLESS = False       # False = see the browser, True = run in background
SLOW_MO = 500          # Milliseconds between actions (0 = fastest)
```

---

## ▶️ Running the Tests

> ⚠️ **Important:** Always run tests from the **root** of the project using the terminal
> with your virtual environment activated. Do **not** use the PyCharm Run button directly,
> as it may bypass `conftest.py` and `pytest.ini`.

### Run all tests:
```bash
pytest
```

### Run a specific test file:
```bash
pytest tests/test_checkboxes.py
pytest test_basic_auth.py
```

### Run a specific test function:
```bash
pytest tests/test_checkboxes.py::test_check_checkbox
pytest test_basic_auth.py::test_basic_auth_success
```

### Run with detailed output:
```bash
pytest -v
```

---

## 👁️ Running Tests Visually (Headed Mode)

By default, the browser window is **visible** during test execution.
To control this behaviour, open `config.py` and set:

```python
HEADLESS = False   # Browser window is visible – great for debugging
HEADLESS = True    # Browser runs in background – great for CI/CD
```

You can also slow down the test execution to follow what is happening:

```python
SLOW_MO = 500   # 500ms pause between each action
SLOW_MO = 0     # No pause – runs at full speed
```

**Example of a successful visual test run in the terminal:**
```
platform win32 -- Python 3.14.3, pytest-9.1.1
collected 2 items

tests/test_add_remove_elements.py::test_add_element    PASSED
tests/test_add_remove_elements.py::test_remove_element PASSED

2 passed in 8.52s
```

---

## 🔐 Security & Credentials

This project uses environment variables to manage sensitive credentials:

- **`enviroment.env.example.py`** - Template file (committed to Git)
- **`enviroment.env`** - Your actual credentials (NOT committed, in `.gitignore`)

**Best practices:**
- Never commit actual credentials to version control
- Each team member should have their own `enviroment.env` file
- Update `enviroment.env.example.py` when adding new environment variables
- Keep credentials secure and don't share them in chat or email

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| [Python](https://www.python.org/) | Programming language |
| [Playwright](https://playwright.dev/python/) | Browser automation |
| [pytest](https://pytest.org/) | Test framework |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Environment variable management |

---

## ❓ Troubleshooting

**Tests fail immediately without opening a browser?**
→ Make sure you ran `playwright install` in step 4.

**`ModuleNotFoundError: No module named 'playwright'`?**
→ Make sure your virtual environment is activated (step 2).

**`ModuleNotFoundError: No module named 'config'`?**
→ Make sure you are running pytest from the **root** of the project, not from inside the `tests/` folder.

**`ModuleNotFoundError: No module named 'dotenv'`?**
→ Install python-dotenv: `pip install python-dotenv`

**Browser opens but tests fail?**
→ The-internet.herokuapp.com may be temporarily down. Try visiting the site manually first.

**Tests run but no browser window appears?**
→ Check that `HEADLESS = False` is set in `config.py`.

**Basic auth tests fail?**
→ Make sure you've created `enviroment.env` from the example file and added credentials.

---

## 📄 License

This project is for educational purposes only.