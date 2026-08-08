from locators.login_locators import LoginLocators


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(
            "https://practicetestautomation.com/practice-test-login/"
        )

    def enter_username(self, username):
        self.driver.find_element(*LoginLocators.USERNAME).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*LoginLocators.PASSWORD).send_keys(password)

    def click_login(self):
        self.driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

    def get_success_message(self):
        return self.driver.find_element(
            *LoginLocators.SUCCESS_MESSAGE
        ).text

    def logout(self):

        self.driver.find_element(
            *LoginLocators.LOGOUT_BUTTON
        ).click()