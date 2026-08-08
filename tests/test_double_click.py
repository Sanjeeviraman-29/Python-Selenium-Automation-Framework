from pages.button_page import ButtonPage


def test_double_click(driver):

    button = ButtonPage(driver)

    button.open()

    button.double_click()

    message = button.get_double_click_message()

    print(message)

    assert "double click" in message.lower()