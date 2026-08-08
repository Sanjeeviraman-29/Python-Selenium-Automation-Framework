from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from locators.dropdown_locators import DropdownLocators


class DropdownPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://demoqa.com/select-menu")

    def get_dropdown(self):
        element = self.wait.until(
            EC.visibility_of_element_located(
                DropdownLocators.OLD_STYLE_MENU
            )
        )
        return Select(element)

    def select_by_text(self, text):
        self.get_dropdown().select_by_visible_text(text)

    def select_by_value(self, value):
        self.get_dropdown().select_by_value(value)

    def select_by_index(self, index):
        self.get_dropdown().select_by_index(index)

    def get_selected_option(self):
        return self.get_dropdown().first_selected_option.text