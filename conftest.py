import os
import pytest

from utils.browser import Browser
from utils.screenshot import Screenshot


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser Name"
    )


@pytest.fixture
def driver(request):

    browser = request.config.getoption("--browser")

    driver = Browser.get_driver(browser)

    yield driver

    driver.quit()


# ----------------------------
# Hook: Capture Screenshot
# ----------------------------

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:

            Screenshot.capture(driver, item.name)