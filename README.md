# Advanced QA Automation Framework: E-Commerce End-to-End Testing

This repository contains a robust, scalable Test Automation Framework built on **Python** and **PyTest**. It is engineered to validate critical end-to-end (E2E) workflows of a simulated e-commerce application, demonstrating practical skills in framework development, CI/CD integration, and advanced reporting.

---

## Technology Stack & Key Libraries

This project uses the following industry-standard tools and libraries:

| Category | Component | Library/Tool | Purpose |
| :--- | :--- | :--- | :--- |
| **Core** | Scripting Language | **Python** | Foundation for all automation logic. |
| **Web Automation** | Browser Interaction | **Selenium WebDriver** | Manages web element interactions and browser sessions. |
| **Testing/Execution** | Test Runner | **PyTest** | Primary framework for test structure and execution. |
| **Parallel Execution** | Speed Optimization | **`pytest-xdist`** | Utilized to distribute tests across multiple CPU cores (`-n 2`), drastically reducing execution time. |
| **Reporting** | HTML Output | **`pytest-html`** | Generates detailed, professional HTML reports for tracking results. |

---

## Framework Features & Architecture

This framework is designed for maintainability and deep analytical reporting:

* **Page Object Model (POM):** All web elements and interactions are housed in dedicated classes (`/pages`), ensuring high code reusability and easy maintenance.
* **Data-Driven Testing (DDT):** Implements parameterized tests (e.g., login validation) using data sourced from an external **JSON file** within the `/data` directory.
* **Custom Reporting Hooks (`conftest.py`):**
    * **Browser Selection:** Custom logic in `conftest.py` uses PyTest's internal mechanisms to accept the browser (e.g., `chrome`) as a required command-line input, enabling **dynamic cross-browser testing**.
    * **Failure Evidence:** A custom hook ensures an automatic **screenshot function** is executed upon any test failure. This evidence is then embedded directly into the final HTML report.
* **Continuous Integration (CI/CD):** The framework is configured for seamless integration with **Jenkins**, triggering automated test runs via a repository webhook on every new push.

---

## Execution Guide

All execution commands must be run from the **`pytestpractice`** directory.

### 1. Setup

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/Ravindu99J/Test_Automation_01.git](https://github.com/Ravindu99J/Test_Automation_01.git)
    cd Test_Automation_01
    ```
2.  **Install Dependencies:** (Ensure your Python virtual environment is active)
    ```bash
    pip install -r requirements.txt
    ```

### 2. Full Parallel Test Run & Reporting

Execute the complete test suite using 2 parallel processes on the Chrome browser, and generate the final report:

```bash
cd pytestpractice
pytest -n 2 --browser_name chrome --html=reports/report.html
```
