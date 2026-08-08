# 🚀 Selenium Automation Framework

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-brightgreen?logo=selenium)
![PyTest](https://img.shields.io/badge/PyTest-Testing-orange?logo=pytest)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Completed-success)

A **Python Selenium Automation Framework** developed using **PyTest** and the **Page Object Model (POM)** design pattern.

The framework demonstrates real-world automation techniques including:

- Cross Browser Testing
- Data Driven Testing using Excel
- Logging
- HTML Reports
- Screenshots
- JavaScript Executor
- Window Handling
- Frames
- Alerts
- Action Chains
- Drag & Drop
- Broken Image Detection

---

# 📑 Table of Contents

- Features
- Tech Stack
- Project Structure
- Installation
- Running Tests
- Framework Architecture
- Test Scenarios Covered
- Reports
- Screenshots
- Future Enhancements
- Author
- License

---

# ✨ Features

✔ Page Object Model (POM)

✔ Cross Browser Testing

✔ Excel Data Driven Framework

✔ HTML Reports

✔ Logging

✔ Screenshot Capture

✔ JavaScript Executor

✔ Explicit Waits

✔ Window Handling

✔ Frame Handling

✔ Alert Handling

✔ Drag and Drop

✔ Dropdown Handling

✔ Checkbox Handling

✔ Radio Button Handling

✔ Broken Image Detection

✔ Action Chains

✔ Context Click

---

# 🛠 Tech Stack

| Technology | Used |
|------------|------|
| Python | ✅ |
| Selenium WebDriver | ✅ |
| PyTest | ✅ |
| OpenPyXL | ✅ |
| Logging | ✅ |
| HTML Reports | ✅ |
| Page Object Model | ✅ |
| Git | ✅ |
| GitHub | ✅ |

---

# 📂 Project Structure

```text
SeleniumAutomationFramework/
│
├── locators/
│
├── logs/
│
├── pages/
│
├── reports/
│
├── resources/
│   └── data/
│
├── screenshots/
│
├── tests/
│
├── utils/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/SeleniumAutomationFramework.git
```

Move into the project

```bash
cd SeleniumAutomationFramework
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running Tests

Run all tests

```bash
pytest
```

Run with HTML report

```bash
pytest --html=reports/report.html
```

Run Chrome

```bash
pytest --browser chrome
```

Run Edge

```bash
pytest --browser edge
```

Run Firefox

```bash
pytest --browser firefox
```

---

# 🏗 Framework Architecture

```
Test

↓

Page Object

↓

Locators

↓

Selenium WebDriver

↓

Browser
```

---

# ✅ Test Scenarios Covered

| Scenario | Status |
|----------|--------|
| Login Automation | ✅ |
| Data Driven Login | ✅ |
| Excel Reader | ✅ |
| Cross Browser | ✅ |
| HTML Reports | ✅ |
| Logging | ✅ |
| Screenshots | ✅ |
| Explicit Wait | ✅ |
| Navigation | ✅ |
| Browser Tabs | ✅ |
| Alerts | ✅ |
| Frames | ✅ |
| Dropdown | ✅ |
| Checkbox | ✅ |
| Radio Button | ✅ |
| JavaScript Executor | ✅ |
| Drag and Drop | ✅ |
| Context Click | ✅ |
| Broken Images | ✅ |

---

# 📊 Reports

The framework automatically generates:

- HTML Reports
- Logs
- Screenshots

Example

```
reports/
    report.html

logs/
    automation.log

screenshots/
    Login_20260808.png
```

---

# 📸 Screenshots

## Login Automation

> *(Add your Login Success screenshot here)*

```
screenshots/login-success.png
```

---

## HTML Report

> *(Add your report screenshot here)*

```
screenshots/html-report.png
```

---

## Drag and Drop

> *(Add Drag & Drop screenshot here)*

```
screenshots/drag-drop.png
```

---

## Context Menu

> *(Add Context Click screenshot here)*

```
screenshots/context-click.png
```

---

## Window Handling

> *(Add Window Handling screenshot here)*

```
screenshots/window-handling.png
```

---

# 📌 Future Enhancements

- Jenkins Integration
- Docker Support
- Parallel Execution
- Allure Reports
- GitHub Actions CI/CD
- API Automation
- Database Validation
- BDD using Behave
- Cloud Execution (BrowserStack / Sauce Labs)

---

# 👨‍💻 Author

**Sanjeevi raman N**

Computer Science Engineering Student

Python | Selenium | Java | SQL | Automation Testing

GitHub:
https://github.com/Sanjeeviraman-29

LinkedIn:
https://www.linkedin.com/in/sanjeevi-raman/

---

# 📄 License

This project is licensed under the MIT License.