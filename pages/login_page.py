from locators.login_locators import LoginLocators
from utils.wait_helper import WaitHelper

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitHelper(driver)

    def open(self):
        self.driver.get(
            "https://practicetestautomation.com/practice-test-login/"
        )

    def enter_username(self, username):
        self.wait.wait_for_element_visible(LoginLocators.USERNAME).send_keys(username)

    def enter_password(self, password):
        self.wait.wait_for_element_visible(LoginLocators.PASSWORD).send_keys(password)

    def click_login(self):
        self.wait.wait_for_element_clickable(LoginLocators.LOGIN_BUTTON).click()

    def get_success_message(self):
        return self.wait.wait_for_element_visible(LoginLocators.SUCCESS_MESSAGE).text

    def logout(self):

        self.wait.wait_for_element_clickable(
            LoginLocators.LOGOUT_BUTTON
        ).click()