import pytest
from utils.browser import Browser

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