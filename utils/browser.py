from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Browser:

    @staticmethod
    def get_driver(browser_name):

        print("Creating Chrome Driver...")

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )

        print("Chrome Opened")

        driver.maximize_window()

        driver.implicitly_wait(10)

        return driver