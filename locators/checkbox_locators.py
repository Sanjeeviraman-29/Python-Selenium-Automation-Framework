from selenium.webdriver.common.by import By


class CheckboxLocators:

    CHECKBOX1 = (
        By.XPATH,
        "(//input[@type='checkbox'])[1]"
    )

    CHECKBOX2 = (
        By.XPATH,
        "(//input[@type='checkbox'])[2]"
    )