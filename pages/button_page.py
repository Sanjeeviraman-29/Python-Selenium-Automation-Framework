from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.button_locators import ButtonLocators


class ButtonPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 10)

        self.actions = ActionChains(driver)

    def open(self):

        self.driver.get(
            "https://demoqa.com/buttons"
        )

    def double_click(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                ButtonLocators.DOUBLE_CLICK
            )
        )

        self.actions.double_click(button).perform()

        print("Double Click Performed")

    def get_double_click_message(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                ButtonLocators.DOUBLE_CLICK_MESSAGE
            )
        ).text