from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.keyboard_locators import KeyboardLocators


class KeyboardPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 10)

        self.actions = ActionChains(driver)

    def open(self):

        self.driver.get(
            "https://www.selenium.dev/selenium/web/web-form.html"
        )

    def enter_username(self, username):

        textbox = self.wait.until(
            EC.visibility_of_element_located(
                KeyboardLocators.TEXTBOX
            )
        )

        textbox.send_keys(username)

        print("Username Entered")

    def press_tab(self):

        textbox = self.driver.find_element(
            *KeyboardLocators.TEXTBOX
        )

        textbox.send_keys(Keys.TAB)

        print("TAB Pressed")

    def enter_password(self, pwd):

        password_box = self.wait.until(
            EC.visibility_of_element_located(
                KeyboardLocators.PASSWORD
            )
        )

        password_box.send_keys(pwd)

        print("Password Entered")

    def ctrl_a(self):

        textbox = self.driver.find_element(
            *KeyboardLocators.TEXTBOX
        )

        self.actions.click(textbox)\
            .key_down(Keys.CONTROL)\
            .send_keys("a")\
            .key_up(Keys.CONTROL)\
            .perform()

        print("CTRL + A Executed")

    def press_enter(self):

        button = self.driver.find_element(
            *KeyboardLocators.SUBMIT
        )

        button.send_keys(Keys.ENTER)

        print("ENTER Pressed")

    def get_current_url(self):

        return self.driver.current_url