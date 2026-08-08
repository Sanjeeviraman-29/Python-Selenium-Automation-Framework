from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.hover_locators import HoverLocators


class HoverPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 10)

        self.actions = ActionChains(driver)

    def open(self):

        self.driver.get(
            "https://the-internet.herokuapp.com/hovers"
        )

    def hover_first_image(self):

        image = self.wait.until(
            EC.visibility_of_element_located(
                HoverLocators.IMAGE1
            )
        )

        self.actions.move_to_element(image).perform()

        print("Mouse Hover Performed")

    def get_user_text(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                HoverLocators.USER_TEXT
            )
        ).text

    def click_profile(self):

        self.wait.until(
            EC.element_to_be_clickable(
                HoverLocators.PROFILE_LINK
            )
        ).click()