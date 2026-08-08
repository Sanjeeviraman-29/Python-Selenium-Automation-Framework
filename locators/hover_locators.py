from selenium.webdriver.common.by import By


class HoverLocators:

    IMAGE1 = (
        By.XPATH,
        "(//div[@class='figure'])[1]"
    )

    PROFILE_LINK = (
        By.LINK_TEXT,
        "View profile"
    )

    USER_TEXT = (
        By.TAG_NAME,
        "h5"
    )