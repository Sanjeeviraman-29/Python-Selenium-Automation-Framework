from pages.dropdown_page import DropdownPage


def test_dropdown(driver):

    dropdown = DropdownPage(driver)

    dropdown.open()

    dropdown.select_by_text("Purple")

    assert dropdown.get_selected_option() == "Purple"

    print("Selected:", dropdown.get_selected_option())

    dropdown.select_by_value("5")

    assert dropdown.get_selected_option() == "Black"

    print("Selected:", dropdown.get_selected_option())

    dropdown.select_by_index(2)

    print("Selected:", dropdown.get_selected_option())