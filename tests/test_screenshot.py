from utils.screenshot import Screenshot


def test_take_screenshot(driver):

    driver.get("https://www.google.com")

    Screenshot.capture(driver, "GoogleHome")

    assert True