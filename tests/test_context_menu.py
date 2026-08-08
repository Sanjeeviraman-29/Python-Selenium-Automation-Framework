from pages.context_menu_page import ContextMenuPage


def test_context_menu(driver):

    context = ContextMenuPage(driver)

    context.open()

    context.right_click_box()

    message = context.get_alert_text()

    print("Alert Message:", message)

    assert "context menu" in message.lower()

    context.accept_alert()