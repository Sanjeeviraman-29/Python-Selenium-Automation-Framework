from pages.login_page import LoginPage


def test_valid_login(driver):

    login = LoginPage(driver)

    login.open()

    login.enter_username("student")

    login.enter_password("Password123")

    login.click_login()

    assert "Logged In Successfully" in login.get_success_message()