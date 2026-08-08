from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.radio_locators import RadioLocators


class RadioPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 10)

    def open(self):

        self.driver.get(
            "https://practice.expandtesting.com/radio-buttons"
        )

    def click_blue(self):

        self.wait.until(
            EC.element_to_be_clickable(
                RadioLocators.BLUE
            )
        ).click()

    def click_red(self):

        self.wait.until(
            EC.element_to_be_clickable(
                RadioLocators.RED
            )
        ).click()

    def is_blue_selected(self):

        return self.driver.find_element(
            *RadioLocators.BLUE
        ).is_selected()

    def is_red_selected(self):

        return self.driver.find_element(
            *RadioLocators.RED
        ).is_selected()

    def is_yellow_enabled(self):

        return self.driver.find_element(
            *RadioLocators.YELLOW
        ).is_enabled()

    