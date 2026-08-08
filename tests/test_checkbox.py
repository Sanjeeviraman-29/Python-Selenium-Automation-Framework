from pages.checkbox_page import CheckboxPage


def test_checkbox(driver):

    checkbox = CheckboxPage(driver)

    checkbox.open()

    print("Checkbox1 Initially:",
          checkbox.is_checkbox1_selected())

    print("Checkbox2 Initially:",
          checkbox.is_checkbox2_selected())

    # Select Checkbox 1
    if not checkbox.is_checkbox1_selected():

        checkbox.click_checkbox1()

    # Unselect Checkbox 2
    if checkbox.is_checkbox2_selected():

        checkbox.click_checkbox2()

    print("Checkbox1 After:",
          checkbox.is_checkbox1_selected())

    print("Checkbox2 After:",
          checkbox.is_checkbox2_selected())

    assert checkbox.is_checkbox1_selected()

    assert not checkbox.is_checkbox2_selected()