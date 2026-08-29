from playwright.sync_api import Page
import time

class BasePage:
    def __init__(self, page:Page):
        self.__page = page


    def fill_text(self, locator, text):
        self.__page.locator(locator).wait_for(state="visible")
        self.__page.locator(locator).fill(text)

    def click(self, locator):
        element = self.__page.locator(locator)
        element.wait_for(state="visible")
        element.click()

    def select_option(self, locator, value):
        self.__page.locator(locator).highlight()
        self.__page.select_option(locator, value)

    def press_enter(self):
        time.sleep(1)
        self.__page.keyboard.press("Enter")

    def press_enter_on(self, locator):
        self.__page.locator(locator).press("Enter")

    def del_text(self):
        self.wait_time(1)
        self.__page.keyboard.press("Control+A")
        self.__page.keyboard.press("Backspace")

    def get_text(self, locator):
        return self.__page.locator(locator).inner_text()

    def hover(self, locator):
        self.__page.locator(locator).wait_for(state="visible")
        self.__page.locator(locator).hover()

    def get_value(self, locator):
        return self.__page.locator(locator).input_value()

    def esc_btn(self):
        time.sleep(1)
        self.__page.keyboard.press("Escape")

    def dbl_click(self, locator):
        self.__page.locator(locator).dblclick()

    def fill_iframe(self, iframe_locator, text):
        self.__page.frame_locator(iframe_locator).locator("body").fill(text)

    def get_iframe(self, iframe_locator):
        return self.__page.frame_locator(iframe_locator).locator("body").inner_text()

    def press_type(self, text):
        self.__page.keyboard.type(text)

    def click_by_text(self, locator, text):
        self.__page.locator(locator, has_text=text).first.click()

    def count_elements(self, locator):
        return self.__page.locator(locator).count()

    def wait_time(self, seconds):
        time.sleep(seconds)

    def get_locator(self, locator):
        return self.__page.locator(locator)


    def click_force(self, locator):
        self.__page.locator(locator).click(force=True)

    def get_text_when_visible(self, locator):
        element = self.__page.locator(locator)
        element.wait_for(state="visible")
        return element.inner_text()

    def first_click(self, locator):
        self.__page.locator(locator).first.click()

    def wait_time_visible(self, locator):
        self.__page.locator(locator).first.wait_for(state="visible")

    def get_attribute(self, locator, attribute_name):
        return self.__page.locator(locator).get_attribute(attribute_name)


    def first_hover(self, locator):
        self.__page.locator(locator).first.hover()

    def upload_file(self, locator, file_path):
        self.__page.locator(locator).set_input_files(file_path)

    def hover_by_index(self, locator, index):
        self.__page.locator(locator).nth(index).hover()

    def click_by_index(self, locator, index):
        self.__page.locator(locator).nth(index).click()

    def get_all_texts(self, locator):
        return self.__page.locator(locator).all_inner_texts()

    def scroll_to_bottom(self):
        self.__page.keyboard.press("End")

    def scroll_to_top(self):
        self.__page.keyboard.press("Home")

    def click_by_index_force(self, locator, index):
        self.__page.locator(locator).nth(index).click(force=True)