from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.drag_drop_locators import DragDropLocators


class DragDropPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 10)

        self.actions = ActionChains(driver)

    def open(self):

        self.driver.get(
            "https://the-internet.herokuapp.com/drag_and_drop"
        )

    def drag_a_to_b(self):

        source = self.wait.until(
            EC.visibility_of_element_located(
                DragDropLocators.COLUMN_A
            )
        )

        target = self.wait.until(
            EC.visibility_of_element_located(
                DragDropLocators.COLUMN_B
            )
        )

        self.actions.drag_and_drop(
            source,
            target
        ).perform()

        print("Drag And Drop Performed")

    def get_header_a(self):

        return self.driver.find_element(
            *DragDropLocators.HEADER_A
        ).text

    def get_header_b(self):

        return self.driver.find_element(
            *DragDropLocators.HEADER_B
        ).text