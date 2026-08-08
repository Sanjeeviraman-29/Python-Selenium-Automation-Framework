from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.context_menu_locators import ContextMenuLocators


class ContextMenuPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 10)

        self.actions = ActionChains(driver)

    def open(self):

        self.driver.get(
            "https://the-internet.herokuapp.com/context_menu"
        )

    def right_click_box(self):

        box = self.wait.until(
            EC.visibility_of_element_located(
                ContextMenuLocators.HOTSPOT
            )
        )

        self.actions.context_click(box).perform()

        print("Right Click Performed")

    def get_alert_text(self):

        alert = self.wait.until(
            EC.alert_is_present()
        )

        return alert.text

    def accept_alert(self):

        self.driver.switch_to.alert.accept()

        print("Alert Accepted")