from selenium.webdriver.common.by import By


def test_simple_alert(driver):

    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    driver.find_element(
        By.XPATH,
        "//button[text()='Click for JS Alert']"
    ).click()

    alert = driver.switch_to.alert

    print("Alert Text:", alert.text)

    alert.accept()

    result = driver.find_element(By.ID, "result").text

    print(result)

    assert "successfully" in result.lower()

def test_confirmation_alert(driver):

    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    driver.find_element(
        By.XPATH,
        "//button[text()='Click for JS Confirm']"
    ).click()

    alert = driver.switch_to.alert

    print(alert.text)

    alert.dismiss()

    result = driver.find_element(By.ID, "result").text

    print(result)

    assert "Cancel" in result

def test_prompt_alert(driver):

    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    driver.find_element(
        By.XPATH,
        "//button[text()='Click for JS Prompt']"
    ).click()

    alert = driver.switch_to.alert

    alert.send_keys("Vijay")

    alert.accept()

    result = driver.find_element(By.ID, "result").text

    print(result)

    assert "Vijay" in result