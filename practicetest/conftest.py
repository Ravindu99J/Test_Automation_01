import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )

@pytest.fixture(scope="function")
def browserInstance(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--headless=new")
        chrome_options.add_experimental_option(
            "prefs", {
                "profile.password_manager_enabled": False,
                "credentials_enable_service": False,
                "profile.password_manager_leak_detection": False,
            })
        driver = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get('https://rahulshettyacademy.com/loginpagePractise/')
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Take screenshot and embed into pytest-html report when test fails.
    """
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when in ("call", "setup"):
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # Ensure reports directory exists
            reports_dir = os.path.join(os.path.dirname(__file__), "reports")
            os.makedirs(reports_dir, exist_ok=True)

            # Sanitize file name
            safe_name = report.nodeid.replace("::", "_").replace("/", "_").replace("\\", "_").replace(":", "_")
            file_name = os.path.join(reports_dir, f"{safe_name}.png")

            print("Saving screenshot to:", file_name)
            _capture_screenshot(file_name)

            if os.path.exists(file_name):
                html = (
                    f'<div><img src="{file_name}" alt="screenshot" '
                    f'style="width:304px;height:228px;" '
                    f'onclick="window.open(this.src)" align="right"/></div>'
                )
                extra.append(pytest_html.extras.html(html))

        report.extra = extra


def _capture_screenshot(file_name):
    try:
        driver.get_screenshot_as_file(file_name)
    except Exception as e:
        print("Screenshot capture failed:", e)
#test3