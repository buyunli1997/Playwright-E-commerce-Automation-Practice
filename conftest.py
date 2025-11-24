import os
import shutil
import pytest
import subprocess
from datetime import datetime
from playwright.sync_api import sync_playwright

# Global import for Allure hooks (for robustness)
# Import allure once to ensure stable access for all hooks and robust reporting
try:
    import allure

    HAS_ALLURE = True
except ImportError:
    HAS_ALLURE = False

# Force Pytest to discover and load BDD step module
pytest_plugins = "tests.common_steps"


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chromium",
        help="Browser to run tests: chromium, firefox, webkit, chrome, msedge"
    )


# Clean up the old Allure results directory at session start
def pytest_sessionstart(session):
    """Cleans up the allure-results directory before the test session starts."""
    base_results = os.path.join("reports", "allure-results")
    if os.path.exists(base_results):
        try:
            # Recursively delete the directory and its contents
            shutil.rmtree(base_results)
            print(f"\n[Allure Cleanup] Successfully removed old results: {base_results}")
        except OSError as e:
            # Print a warning but allow the program to continue
            print(f"\n[Allure Cleanup] Warning: Could not remove directory {base_results}: {e}")

    # Recreate the directory for the current test run
    os.makedirs(base_results, exist_ok=True)


# Playwright Fixtures
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
            # Use channel="chrome" for locally installed Chrome
            browser = p.chromium.launch(channel="chrome", headless=False)
        elif browser_name == "msedge":
            # Use channel="msedge" for locally installed Edge
            browser = p.chromium.launch(channel="msedge", headless=False)
        else:
            raise ValueError(f"Unknown browser: {browser_name}")

        yield browser
        browser.close()


@pytest.fixture()
def page(browser):
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    yield page
    page.close()


# Store timestamp for later (Allure configuration)
def pytest_configure(config):
    # Store timestamp for the report folder
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config._allure_timestamp = timestamp


# Screenshot on failure
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
        # Optimization: use nodeid as a unique identifier for the test
        test_name = item.nodeid.replace("::", "_").replace("/", "_").replace("\\", "_")
        screenshot_path = os.path.join(
            screenshots_dir,
            f"{test_name}_{timestamp}.png"
        )

        page.screenshot(path=screenshot_path)

        # Optimization: Attach to Allure only if import was successful
        if HAS_ALLURE:
            allure.attach.file(
                screenshot_path,
                name=f"Screenshot-{test_name}",
                attachment_type=allure.attachment_type.PNG,
            )


# Generate timestamped report at end
def pytest_sessionfinish(session, exitstatus):
    timestamp = getattr(session.config, "_allure_timestamp", None)

    # Default pytest output folder (this already has JSON files)
    base_results = os.path.join("reports", "allure-results")

    # Verify JSON result files exist
    # Must first confirm the directory exists
    if not os.path.exists(base_results):
        print("No allure-results folder found. Nothing to report.")
        return

    # Allure result files usually end with '-result.json'
    json_files = [f for f in os.listdir(base_results) if f.endswith('-result.json')]

    if not json_files:
        # If no result files are found, the pytest-allure plugin failed to work
        print(f"\n[Allure ERROR] No Allure result files (ending with '-result.json') were found in {base_results}.")
        print("Please confirm 'pytest-bdd' and 'allure-pytest' are correctly installed and tests ran successfully.")
        return

    print(f"Found {len(json_files)} Allure result files to process.")

    # Make a timestamped copy to preserve history
    archive_results = os.path.join(
        "reports",
        f"allure-results-{timestamp}"
    )
    # Ensure only files from this run are copied
    shutil.copytree(base_results, archive_results, dirs_exist_ok=True)

    # Report output folder
    report_dir = os.path.join(
        "reports",
        f"allure-report-{timestamp}"
    )
    os.makedirs(report_dir, exist_ok=True)

    # Use the absolute path provided by the user
    ALLURE = r"C:\allure-2.35.1\bin\allure.bat"

    # Generate the HTML report
    cmd_generate = f'"{ALLURE}" generate "{archive_results}" -o "{report_dir}" --clean'
    print(f"\n[Allure Generate] Command: {cmd_generate}")
    ret = subprocess.run(cmd_generate, shell=True)

    if ret.returncode != 0:
        print("[Allure ERROR] Allure report generation failed.")
        return

    print(f"\n[Allure SUCCESS] Allure report generated at: {report_dir}")

    # --- Key Hint: Prompt user to manually view the latest report ---
    print(f"\n--- Report Access Tip ---")
    print(f"Allure Server may cache old reports.")
    print(f"Please manually open the 'index.html' file at the following path to view the LATEST report ({timestamp}):")
    print(f"Path: {report_dir}\\index.html")
    print("--------------------")