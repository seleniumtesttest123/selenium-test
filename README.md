# Selenium Automation Projects – README
**Author:** Vinay J L

---
## 🚀 Overview
This repository is a **collection of Selenium‑based automation projects** created during my learning journey. Each folder represents a different test module, experiment, or practice task using **Selenium WebDriver**, **Python**, and **pytest**.

The goal of this repository is to demonstrate strong fundamentals in automation testing, including:
- Writing clean, stable Selenium scripts
- Using pytest fixtures and parameterization
- Building modular test structures
- Capturing logs & screenshots
- Automating real‑world sites like Amazon

Interviewers visiting this repository will get a clear understanding of my learning progress, testing approach, and hands‑on automation skills.

> **Note:** This POM-based Yatra flight booking automation project is not yet part of this repository, but it will be added.

In addition, I have also **implemented the Page Object Model (POM) for automating the Yatra website flight booking process**, showcasing structured automation design and scalability.

---
## 📁 Repository Structure
```
selenium-test/
├── selenium_pytest/         # Selenium scripts using pytest
├── seleniumtest/            # Additional Selenium practice tests
├── pytest/                  # pytest-based structured tests
├── tuesday_test/            # Weekly practice tasks / experiments
└── README.md                # Project documentation
```
Each folder contains independent learning modules or test suites.

---
## 🛠 Tools & Technologies Used
- **Python** – Main scripting language
- **Selenium WebDriver** – Browser automation
- **pytest** – Testing framework
- **WebDriver Manager (optional)** – Driver handling automation
- **Logging (Python logging module)** – Detailed runtime logs
- **Chrome / Edge WebDriver** – Browser drivers
- **Git & GitHub** – Version control and project hosting

---
## 📌 Highlight: `test_amazon_search` Project
A major project in this repository is **Amazon Search Automation**.

### 🔍 What It Does
- Opens **Amazon.in**
- Searches multiple product categories
- Waits for results using explicit waits
- Validates product listings
- Extracts product titles & prices
- Logs everything to `test_amazon.log`
- Captures screenshots on failure

### 🔧 Concepts Demonstrated
- Parameterized pytest tests
- Custom logging setup
- WebDriverWait & expected_conditions
- Screenshot capture for failures
- Clean fixture-based test structure

---
## 📦 Requirements (requirements.txt)
```
selenium
pytest
webdriver-manager
pytest-html
```
These dependencies support browser automation, reporting, and driver management.

---
## ▶️ How to Run the Tests
### 1️⃣ Clone the repository
```bash
git clone https://github.com/seleniumtesttest123/selenium-test.git
cd selenium-test
```
### 2️⃣ Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate   # Windows
```
### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Run pytest
```bash
pytest -v -s
```
### 5️⃣ View logs & screenshots
- Logs: `logs/test_amazon.log`
- Screenshots: auto-saved on test failure

---
## 🌟 Why This Repository Stands Out
- Shows multiple Selenium approaches
- Demonstrates Amazon real-world automation
- Includes detailed error handling
- Uses waits, fixtures, and structured design
- Demonstrates strong logging practices

This reflects my ability to solve **real-world automation problems** cleanly and professionally.

---
## 📚 Future Enhancements
- Add Page Object Model (POM)
- Add HTML reporting (pytest-html / Allure)
- Add GitHub Actions (CI/CD)
- Add data-driven testing (CSV/JSON)
- Add more site automation examples

---
## 🙏 Thank You
Thank you for taking time to explore my automation work.
I continuously improve and expand this repository as I learn new tools and concepts.

**— Vinay J L**
