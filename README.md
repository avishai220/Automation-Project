# 🎯 E2E Automation Framework — automationexercise.com

### **Page Object Model · Playwright · Pytest · Allure**

[![Playwright](https://img.shields.io/badge/Playwright-1.62-2EAD33?logo=playwright&logoColor=white)](https://playwright.dev/python/)
[![Python](https://img.shields.io/badge/Python-3.14-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/Pytest-9.1-0A9EDC?logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![Allure](https://img.shields.io/badge/Allure_Report-2.16-FF7B2C?logo=qameta&logoColor=white)](https://allurereport.org/)
[![Tests](https://img.shields.io/badge/Tests-20_passing-success)](#-test-coverage)
[![Repo](https://img.shields.io/badge/GitHub-Automation--Project-181717?logo=github&logoColor=white)](https://github.com/avishai220/Automation-Project)

---

## 🌟 Overview

A complete end-to-end test suite for [automationexercise.com](https://automationexercise.com/),
covering the full customer journey: registration, product browsing, cart management,
checkout, and form handling.

The framework is built on the **Page Object Model**, with a generic `BasePage` that
wraps every Playwright interaction. Tests never touch locators directly — pages return
data, and tests decide what's correct.

---

## 🎯 Design Principles

* **Verify outcomes, not actions** — every test asserts what actually happened, not just that a click didn't throw.
* **Stable locators** — semantic attributes (`data-qa`, `href`) over styling classes or DOM position.
* **Clean state per test** — a fresh browser context on every run, with no shared state between tests.
* **Readable failures** — automatic screenshot attached to Allure whenever a test fails.

---

## 🛠️ Tech Stack

| Layer | Tool |
|---|---|
| Language | [Python 3.14](https://www.python.org/) |
| Browser automation | [Playwright](https://playwright.dev/python/) |
| Test runner | [Pytest](https://docs.pytest.org/) |
| Reporting | [Allure Report](https://allurereport.org/) |
| File validation | [openpyxl](https://openpyxl.readthedocs.io/) |
| Configuration | configparser (`config.ini`) |

---

## 🏗️ Folder Structure

```bash
MyProject/
├── pages/                      # Page Object Model
│   ├── base_page.py            # Generic Playwright actions
│   ├── home_page.py
│   ├── register_login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   └── contact_us_page.py
├── tests/                      # Test suites
│   ├── conftest.py             # Fixtures, screenshots, environment data
│   ├── base_test.py
│   ├── test_01_register.py
│   ├── test_02_contact_us.py
│   ├── test_03_products.py
│   ├── test_04_home_page.py
│   ├── test_05_checkout.py
│   └── test_06_cart.py
├── utlis/
│   └── config.py               # config.ini reader
├── test_data/                  # Static files used by tests
├── config.ini                  # URL and user credentials
├── pytest.ini                  # Pytest configuration
└── requirements.txt
```

---

## 📊 Test Coverage

**20 automated tests across 5 functional areas.**

| # | Area | Tests | Scope |
|---|---|---|---|
| 01 | Registration & Login | 5 | Sign up, valid login, invalid credentials, duplicate email, account deletion |
| 02 | Products & Search | 6 | Product count and details, search, add to cart, category filter, brand page, product review |
| 03 | Shopping Cart | 3 | Quantity verification, item removal, newsletter from cart |
| 04 | End-to-End Checkout | 2 | Product selection, login mid-flow, address verification, payment, order confirmation |
| 05 | Home Page & Forms | 4 | Contact form with file upload and browser dialog, logout, newsletter, scroll with title verification |

---

## 🧩 Notable Implementations

**File upload without the OS dialog**
`set_input_files` feeds the file directly to the input element, bypassing the native
file picker that automation cannot control.

**Browser dialog handling**
A `page.on("dialog")` listener accepts the confirmation popup that appears on form
submission — without it, Playwright dismisses it and the form is never sent.

**Ad request blocking**
`page.route` aborts requests to ad networks, which stabilizes load times and prevents
overlay iframes from intercepting clicks.

**Data-driven configuration**
Credentials and the base URL live in `config.ini`, so switching environments means
editing one file instead of hunting through the code.

---

## 🚀 Installation

```bash
git clone https://github.com/avishai220/Automation-Project.git
cd Automation-Project
```

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # macOS / Linux
```

```bash
pip install -r requirements.txt
playwright install
```

---

## ▶️ Running the Tests

Run the full suite:

```bash
pytest
```

Run a single file:

```bash
pytest tests/test_01_register.py
```

Run a single test with console output:

```bash
pytest tests/test_01_register.py::TestRegisterPage::test_02_login -s
```

---

## 📈 Allure Reports

Results are collected automatically on every run (configured in `pytest.ini`).
To open the report:

```bash
allure serve allure-results
```

Each test includes a title, description, step breakdown, environment details,
and a screenshot attached automatically on failure.

---

## ⚙️ Configuration

`config.ini` holds the environment data:

```ini
[general]
url = https://automationexercise.com/

[user]
email = your_email@example.com
password = your_password
```

---

## 📬 Contact

**Avishai Tal** — QA Automation Engineer

[![LinkedIn](https://img.shields.io/badge/LinkedIn-tal--avishai-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/tal-avishai)
[![Email](https://img.shields.io/badge/Email-avishai220@walla.com-EA4335?logo=gmail&logoColor=white)](mailto:avishai220@walla.com)
[![GitHub](https://img.shields.io/badge/GitHub-avishai220-181717?logo=github&logoColor=white)](https://github.com/avishai220)
