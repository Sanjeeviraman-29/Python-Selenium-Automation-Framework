from selenium.webdriver.common.by import By


class LoginLocators:

    USERNAME = (By.ID, "username")

    PASSWORD = (By.ID, "password")

    LOGIN_BUTTON = (By.ID, "submit")

    SUCCESS_MESSAGE = (By.TAG_NAME, "h1")

    LOGOUT_BUTTON = (By.LINK_TEXT, "Log out")