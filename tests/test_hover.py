from pages.hover_page import HoverPage


def test_mouse_hover(driver):

    hover = HoverPage(driver)

    hover.open()

    hover.hover_first_image()

    print(hover.get_user_text())

    assert "name: user1" in hover.get_user_text().lower()

    hover.click_profile()

    print("Current URL:", driver.current_url)

    assert "users/1" in driver.current_url