from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.window_locators import WindowLocators


class WindowPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 10)

    def open(self):

        self.driver.get(
            "https://the-internet.herokuapp.com/windows"
        )

    def click_here(self):

        self.wait.until(
            EC.element_to_be_clickable(
                WindowLocators.CLICK_HERE
            )
        ).click()

    def switch_to_new_window(self):

        parent = self.driver.current_window_handle

        all_windows = self.driver.window_handles

        print("Parent Window:", parent)

        for window in all_windows:

            if window != parent:

                self.driver.switch_to.window(window)

                print("Switched to Child Window")

                break

    def get_heading(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                WindowLocators.HEADER
            )
        ).text

    def close_child(self):

        self.driver.close()

    def switch_to_parent(self):

        parent = self.driver.window_handles[0]

        self.driver.switch_to.window(parent)

        print("Back to Parent")