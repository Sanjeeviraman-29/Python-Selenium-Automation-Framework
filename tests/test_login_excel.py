from pages.login_page import LoginPage
from utils.excel_reader import ExcelReader
from utils.logger import Logger
from utils.screenshot import Screenshot

def test_login_using_excel(driver):

    login = LoginPage(driver)
    logger = Logger.get_logger()
    logger.info("========== Test Started ==========")

    reader = ExcelReader(
        "resources/data/LoginData.xlsx",
        "LoginData"
    )

    test_data = reader.get_all_data()

    for data in test_data:

        username = data["username"]
        password = data["password"]
        expected = data["expected"]

        logger.info(f"Testing: {username}")

        login.open()

        login.enter_username(username)

        login.enter_password(password)

        login.click_login()

        if expected == "Success":

            try:

                assert "logged-in-successfully" in driver.current_url

                logger.info("Login Successful")

                login.logout()

            except AssertionError:

                Screenshot.capture(driver, "Valid_Login_Failure")

                raise

        else:

            try:

                assert "practice-test-login" in driver.current_url

                logger.warning("Invalid Login Verified")

            except AssertionError:

                Screenshot.capture(driver, "Invalid_Login_Failure")

                raise

    logger.info("========== Test Finished ==========")