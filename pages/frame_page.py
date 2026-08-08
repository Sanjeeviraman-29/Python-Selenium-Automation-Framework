from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.frame_locators import FrameLocators


class FramePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://demoqa.com/frames")

    def switch_to_frame(self):

        frame = self.wait.until(
            EC.presence_of_element_located(FrameLocators.FRAME1)
        )

        self.driver.switch_to.frame(frame)

        print("Successfully switched to Frame 1")

    def get_heading_text(self):

        heading = self.wait.until(
            EC.visibility_of_element_located(
                FrameLocators.FRAME_HEADING
            )
        )

        return heading.text

    def switch_to_default(self):

        self.driver.switch_to.default_content()

        print("Returned to Main Page")