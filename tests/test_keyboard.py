from pages.keyboard_page import KeyboardPage


def test_keyboard_actions(driver):

    keyboard = KeyboardPage(driver)

    keyboard.open()

    keyboard.enter_username("Vijay")

    keyboard.press_tab()

    keyboard.enter_password("Password123")

    keyboard.ctrl_a()

    keyboard.press_enter()

    print("Current URL:", keyboard.get_current_url())

    assert "submitted-form" in keyboard.get_current_url()

    print("Keyboard Actions Completed Successfully")