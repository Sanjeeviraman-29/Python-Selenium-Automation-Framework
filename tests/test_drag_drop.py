from pages.drag_drop_page import DragDropPage


def test_drag_drop(driver):

    page = DragDropPage(driver)

    page.open()

    print("Before Drag:")

    print("Column A:", page.get_header_a())

    print("Column B:", page.get_header_b())

    page.drag_a_to_b()

    print("\nAfter Drag:")

    print("Column A:", page.get_header_a())

    print("Column B:", page.get_header_b())

    assert page.get_header_a() == "B"

    assert page.get_header_b() == "A"