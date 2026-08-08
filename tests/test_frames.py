from pages.frame_page import FramePage


def test_iframe(driver):

    frame = FramePage(driver)

    frame.open()

    frame.switch_to_frame()

    text = frame.get_heading_text()

    print("Frame Text:", text)

    assert text == "This is a sample page"

    frame.switch_to_default()