class JavaScriptHelper:

    def __init__(self, driver):

        self.driver = driver

    def scroll_down(self):

        self.driver.execute_script(

            "window.scrollBy(0,500);"

        )

    def scroll_up(self):

        self.driver.execute_script(

            "window.scrollBy(0,-500);"

        )

    def scroll_to_bottom(self):

        self.driver.execute_script(

            "window.scrollTo(0, document.body.scrollHeight);"

        )

    def scroll_to_top(self):

        self.driver.execute_script(

            "window.scrollTo(0,0);"

        )

    def scroll_into_view(self, element):

        self.driver.execute_script(

            "arguments[0].scrollIntoView({block:'center'});",

            element

        )

    def click_by_js(self, element):

        self.driver.execute_script(

            "arguments[0].click();",

            element

        )