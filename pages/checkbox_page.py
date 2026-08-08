from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.checkbox_locators import CheckboxLocators


class CheckboxPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 10)

    def open(self):

        self.driver.get(
            "https://the-internet.herokuapp.com/checkboxes"
        )

    def checkbox1(self):

        return self.wait.until(
            EC.presence_of_element_located(
                CheckboxLocators.CHECKBOX1
            )
        )

    def checkbox2(self):

        return self.wait.until(
            EC.presence_of_element_located(
                CheckboxLocators.CHECKBOX2
            )
        )

    def click_checkbox1(self):

        self.checkbox1().click()

    def click_checkbox2(self):

        self.checkbox2().click()

    def is_checkbox1_selected(self):

        return self.checkbox1().is_selected()

    def is_checkbox2_selected(self):

        return self.checkbox2().is_selected()