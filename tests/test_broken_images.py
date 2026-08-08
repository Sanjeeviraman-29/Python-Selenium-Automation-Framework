from selenium.webdriver.common.by import By

from utils.image_checker import ImageChecker


def test_broken_images(driver):

    driver.get(
        "https://practice.expandtesting.com/"
    )

    images = driver.find_elements(
        By.TAG_NAME,
        "img"
    )

    print(f"\nTotal Images Found : {len(images)}\n")

    broken = 0

    working = 0

    for image in images:

        src = image.get_attribute("src")

        if not src:

            continue

        status = ImageChecker.check_image(src)

        if status == 200:

            print(f"✓ Working : {src}")

            working += 1

        else:

            print(f"✗ Broken : {src}")

            broken += 1

    print("\n-------------------------")

    print(f"Working Images : {working}")

    print(f"Broken Images  : {broken}")

    print("-------------------------")

    assert broken == 0