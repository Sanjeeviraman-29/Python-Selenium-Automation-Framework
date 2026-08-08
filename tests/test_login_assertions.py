from pages.login_page import LoginPage
from utils.excel_reader import ExcelReader


def test_login_assertions(driver):

    login = LoginPage(driver)

    reader = ExcelReader(
        "resources/data/LoginData.xlsx",
        "LoginData"
    )

    data = reader.get_all_data()

    for username, password in data:

        print(f"\nTesting {username}")

        login.open()

        login.enter_username(username)

        login.enter_password(password)

        login.click_login()

        if username == "student" and password == "Password123":

            assert "logged-in-successfully" in driver.current_url

            print("Login Successful")

            login.logout()

        else:

            assert "practice-test-login" in driver.current_url

            print("Invalid Login Verified")