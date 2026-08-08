from pages.window_page import WindowPage


def test_window_handling(driver):

    window = WindowPage(driver)

    window.open()

    print("Parent Title:", driver.title)

    window.click_here()

    window.switch_to_new_window()

    print("Child Title:", driver.title)

    print("Heading:", window.get_heading())

    assert "New Window" in window.get_heading()

    window.close_child()

    window.switch_to_parent()

    print("Current Title:", driver.title)

    assert "The Internet" in driver.title