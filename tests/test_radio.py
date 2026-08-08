from pages.radio_page import RadioPage


def test_radio_button(driver):

    radio = RadioPage(driver)

    radio.open()

    radio.click_blue()

    print("Blue Selected:", radio.is_blue_selected())

    assert radio.is_blue_selected()

    radio.click_red()

    print("Red Selected:", radio.is_red_selected())

    assert radio.is_red_selected()

    print("Yellow Enabled:", radio.is_yellow_enabled())

    assert radio.is_yellow_enabled()