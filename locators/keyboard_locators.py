from selenium.webdriver.common.by import By


class KeyboardLocators:

    TEXTBOX = (
        By.NAME,
        "my-text"
    )

    PASSWORD = (
        By.NAME,
        "my-password"
    )

    SUBMIT = (
        By.CSS_SELECTOR,
        "button"
    )