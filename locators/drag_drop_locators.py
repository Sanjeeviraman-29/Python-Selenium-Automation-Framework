from selenium.webdriver.common.by import By


class DragDropLocators:

    COLUMN_A = (
        By.ID,
        "column-a"
    )

    COLUMN_B = (
        By.ID,
        "column-b"
    )

    HEADER_A = (
        By.CSS_SELECTOR,
        "#column-a header"
    )

    HEADER_B = (
        By.CSS_SELECTOR,
        "#column-b header"
    )