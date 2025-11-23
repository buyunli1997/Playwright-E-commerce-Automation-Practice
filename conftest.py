import os
import shutil
import pytest
import subprocess
from datetime import datetime
from playwright.sync_api import sync_playwright


pytest_plugins = "tests.common_steps"


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chromium",
        help="Browser to run tests: chromium, firefox, webkit, chrome, msedge"
    )
# ---------- Playwright Fixtures ----------
@pytest.fixture(scope="session")
def browser(request):
    browser_name = request.config.getoption("--browser")
    with sync_playwright() as p:
        if browser_name == "chromium":
            browser = p.chromium.launch(headless=False)
        elif browser_name == "firefox":
            browser = p.firefox.launch(headless=False)
        elif browser_name == "webkit":
            browser = p.webkit.launch(headless=False)
        elif browser_name == "chrome":
            browser = p.chromium.launch(channel="chrome", headless=False)
        elif browser_name == "msedge":
            browser = p.chromium.launch(channel="msedge", headless=False)
        else:
            raise ValueError(f"Unknown browser: {browser_name}")

        yield browser
        browser.close()

# def browser():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         yield browser
#         browser.close()


@pytest.fixture()
def page(browser):
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    yield page
    page.close()


# Store timestamp for the report folder
def pytest_configure(config):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config._allure_timestamp = timestamp


# Take a screenshot on failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page", None)
        if not page:
            return

        # pytest always writes to this folder
        base_results_dir = os.path.join("reports", "allure-results")

        screenshots_dir = os.path.join(base_results_dir, "screenshots")
        os.makedirs(screenshots_dir, exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        test_name = item.name.replace("/", "_").replace("\\", "_")
        screenshot_path = os.path.join(
            screenshots_dir,
            f"{test_name}_{timestamp}.png"
        )

        page.screenshot(path=screenshot_path)

        try:
            import allure
            allure.attach.file(
                screenshot_path,
                name=f"Screenshot-{test_name}",
                attachment_type=allure.attachment_type.PNG,
            )
        except ImportError:
            pass


# Generate timestamped report at end
def pytest_sessionfinish(session, exitstatus):
    timestamp = getattr(session.config, "_allure_timestamp", None)

    # Default pytest output folder (this already has JSON files)
    base_results = os.path.join("reports", "allure-results")

    if not os.path.exists(base_results):
        print("No allure-results folder found. Nothing to report.")
        return

    # Make a timestamped copy to preserve history
    archive_results = os.path.join(
        "reports",
        f"allure-results-{timestamp}"
    )
    shutil.copytree(base_results, archive_results, dirs_exist_ok=True)

    # Report output folder
    report_dir = os.path.join(
        "reports",
        f"allure-report-{timestamp}"
    )
    os.makedirs(report_dir, exist_ok=True)

    ALLURE = r"C:\allure-2.35.1\bin\allure.bat"

    # Generate the HTML report
    cmd_generate = f'"{ALLURE}" generate "{archive_results}" -o "{report_dir}" --clean'
    print(f"Generating Allure report: {cmd_generate}")
    ret = subprocess.run(cmd_generate, shell=True)

    if ret.returncode != 0:
        print("Allure report generation failed.")
        return

    print(f"Allure report generated at: {report_dir}")

    # Open report automatically
    cmd_open = f'"{ALLURE}" open "{report_dir}"'
    print(f"Launching Allure server: {cmd_open}")
    subprocess.Popen(cmd_open, shell=True)
