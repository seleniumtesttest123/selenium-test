from selenium import webdriver
import pytest
from selenium.webdriver.edge.options import Options
from datetime import datetime
from pathlib import Path
import os

# Global WebDriver instance
_driver = None

Baseurl = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"


def pytest_configure(config):
    # Create a timestamp for the seleniumtest run
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Create reports directory in the conftest folder
    report_dir = Path(__file__).parent / "reports" / f"report_{timestamp}"
    report_dir.mkdir(parents=True, exist_ok=True)

    # Configure HTML report
    html_report = report_dir / f"test_report_{timestamp}.html"
    config.option.htmlpath = html_report
    config.option.self_contained_html = True

    # Create screenshots directory
    screenshot_dir = report_dir / "screenshots"
    screenshot_dir.mkdir(exist_ok=True)

    # Store paths in config for later use
    config._screenshot_dir = str(screenshot_dir)
    config._report_dir = str(report_dir)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" or report.when == "setup":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # Ensure screenshot directory exists
            screenshot_dir = Path(item.config._screenshot_dir)
            screenshot_dir.mkdir(parents=True, exist_ok=True)

            # Create a safe filename from the seleniumtest node ID
            safe_nodeid = (
                report.nodeid.replace("::", "_").replace("/", "_").replace("\\", "_")
            )
            screenshot_path = str(screenshot_dir / f"{safe_nodeid}.png")

            # Get the browser instance and take screenshot
            _driver = item.funcargs.get("browser")
            if _driver is not None:
                try:
                    # Take the screenshot
                    _driver.save_screenshot(screenshot_path)

                    # Get the screenshot filename
                    screenshot_filename = os.path.basename(screenshot_path)

                    # Add screenshot to the report using the full path
                    # The HTML report will be in the same directory as the screenshots folder
                    html = f"""
                    <div>
                        <h4>Failure Screenshot</h4>
                        <div style="text-align: center;">
                            <a href="screenshots/{screenshot_filename}" target="_blank">
                                <img src="screenshots/{screenshot_filename}" 
                                     alt="screenshot" 
                                     style="max-width:100%;
                                            max-height:500px;
                                            margin:10px 0;
                                            border:1px solid #ddd;
                                            box-shadow:2px 2px 5px rgba(0,0,0,0.1);"/>
                                <div>Click to view full size</div>
                            </a>
                        </div>
                    </div>"""
                    extra.append(pytest_html.extras.html(html))
                except Exception as e:
                    print(f"Failed to take screenshot: {str(e)}")

        report.extra = extra


def pytest_html_report_title(report):
    report.title = "Selenium Test Automation Report"


@pytest.fixture(scope="session", autouse=True)
def browser(request):
    global _driver
    if _driver is None:
        options = Options()
        options.add_experimental_option("detach", True)
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-extensions")

        _driver = webdriver.Edge(options=options)
        _driver.implicitly_wait(10)

        # Store the driver in the request object for cleanup
        def close_browser():
            global _driver
            if _driver is not None:
                _driver.quit()
                _driver = None

        request.addfinalizer(close_browser)

    return _driver


def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend(
        [
            f"<p>Test run completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>"
        ]
    )


# python -m pytest selenium_pytest/conftest/ -v
