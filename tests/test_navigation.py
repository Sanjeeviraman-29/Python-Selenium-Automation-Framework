from selenium.webdriver.common.by import By


def test_navigation(driver):

    driver.get("https://practicetestautomation.com/practice-test-login/")

    print("Title:", driver.title)

    print("URL:", driver.current_url)

    driver.get("https://practicetestautomation.com/")

    print("Current:", driver.current_url)

    driver.back()

    print("After Back:", driver.current_url)

    driver.forward()

    print("After Forward:", driver.current_url)

    driver.refresh()

    print("Page Refreshed")