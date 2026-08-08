def test_browser_tabs(driver):

    driver.get("https://www.google.com")

    print("Parent:", driver.title)

    parent = driver.current_window_handle

    driver.switch_to.new_window("tab")

    driver.get("https://practicetestautomation.com")

    print("Child:", driver.title)

    child = driver.current_window_handle

    print("Parent ID:", parent)

    print("Child ID:", child)

    driver.close()

    driver.switch_to.window(parent)

    print("Back To:", driver.title)