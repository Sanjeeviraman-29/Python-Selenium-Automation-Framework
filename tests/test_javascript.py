from selenium.webdriver.common.by import By
import time

from utils.javascript_helper import JavaScriptHelper


def test_javascript_executor(driver):

    driver.get("https://practice.expandtesting.com/")

    js = JavaScriptHelper(driver)

    print("Scrolling Down")

    js.scroll_down()

    time.sleep(2)

    print("Scrolling Up")

    js.scroll_up()

    time.sleep(2)

    print("Scrolling to Bottom")

    js.scroll_to_bottom()

    time.sleep(2)

    print("Scrolling to Top")

    js.scroll_to_top()

    time.sleep(2)

    footer = driver.find_element(By.TAG_NAME, "footer")

    print("Scrolling to Footer")

    js.scroll_into_view(footer)

    time.sleep(2)

    print("JavaScript Executor Completed")