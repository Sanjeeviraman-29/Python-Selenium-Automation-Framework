from selenium.webdriver.common.by import By


class WindowLocators:

    CLICK_HERE = (
        By.LINK_TEXT,
        "Click Here"
    )

    HEADER = (
        By.TAG_NAME,
        "h3"
    )