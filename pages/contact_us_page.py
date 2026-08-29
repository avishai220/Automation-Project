from pages.base_page import BasePage
from playwright.sync_api import Page
import pytest


class ContactUsPage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)


    __CONTACT_US_BTN = ".fa.fa-envelope"
    __CONTACT_US_TITLE = ".col-sm-12>.title.text-center"
    __USERNAME_FIELD = '[data-qa="name"]'
    __EMAIL_FIELD = '[data-qa="email"]'
    __SUBJECT_FIELD = '[data-qa="subject"]'
    __UPLOAD_FILE_BTN = '[type="file"]'
    __SUBMIT_BTN = '[data-qa="submit-button"]'
    __SUCCESS_MSG = ".status.alert.alert-success"


    def contact_us_btn(self, text):
        self.click(self.__CONTACT_US_BTN)
        contact_us_title = self.get_text(self.__CONTACT_US_TITLE)
        return text in contact_us_title

    def contact_us_fields(self, username, email, subject_msg):
        self.fill_text(self.__USERNAME_FIELD, username)
        self.fill_text(self.__EMAIL_FIELD, email)
        self.fill_text(self.__SUBJECT_FIELD, subject_msg)

    def attach_file(self, file_path):
        self.upload_file(self.__UPLOAD_FILE_BTN, file_path)

    def submit_btn(self, text):
        self.click_force(self.__SUBMIT_BTN)
        success_title = self.get_text_when_visible(self.__SUCCESS_MSG)
        print(f"actual: {repr(success_title)}")
        return text in success_title
