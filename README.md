## Test Automation 01

Automated end-to-end workflow validation using Selenium, pytest, and the Page Object Model (POM) design pattern. This project includes parameterized login tests and subsequent workflow automation with assertions to confirm correct behavior.

# Overview

This repository demonstrates a test automation framework built around:

**Parameterized login testing:** The login credentials or login scenarios are driven by input data (e.g. via pytest.mark.parametrize).

**Workflow automation:** After login, the tests automate a sequence of actions on the web application.

**Verification via pytest assertions:** At key points, the tests assert expected states or outputs to confirm that the workflow was executed correctly.

It uses the **Page Object Model (POM)** to encapsulate page-specific elements and actions, making maintenance easier and reducing duplication.

# Technologies & Tools

1.Python

2.Selenium WebDriver — for automating browser interactions

3.pytest — test execution, parameterization, fixtures, assertions

4.Page Object Model (POM) — to separate page locators / interactions from test logic


