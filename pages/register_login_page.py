from typing import cast

from pages.base_page import BasePage
from playwright.sync_api import Page
import pytest


class RegisterLoginPage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)


    __SignUpBtn = 'a[href="/login"]'
    __EMAIL_LOGIN_FIELD = '[data-qa="login-email"]'
    __PASSWORD_LOGIN_FIELD = '[data-qa="login-password"]'
    __NAME_REG_FIELD = '[data-qa="signup-name"]'
    __EMAIL_REG_FIELD = '[data-qa="signup-email"]'
    __SIGN_UP_BTN = '[data-qa="signup-button"]'
    __CHOOSE_GENDER = "#id_gender1"
    __PASSWORD_FIELD = "#password"
    __BIRTH_DATE_DAY = "#days"
    __BIRTH_DATE_MONTH = "#months"
    __BIRTH_DATE_YEAR = "#years"
    __FIRST_NAME_FIELD = "#first_name"
    __LAST_NAME_FIELD = "#last_name"
    __ADDRESS_FIELD = "#address1"
    __STAT_FIELD = "#state"
    __CITY_FIELD = "#city"
    __ZIP_CODE_FIELD = "#zipcode"
    __PHONE_FIELD = "#mobile_number"
    __COUNTRY_DROP_DOWN = "#country"
    __CREATE_ACCOUNT_BTN = '[data-qa="create-account"]'
    __GET_TITLE = ".title.text-center"
    __GET_HOME_PAGE_TITLE = ".nav.navbar-nav"
    __LOGIN_BTN = '[data-qa="login-button"]'
    __LOGIN_ERROR_MSG = "form[action='/login'] p"
    __GET_ERROR_EXITS_EMAIL = '[style="color: red;"]'
    __DELETE_ACCOUNT = '[href="/delete_account"]'
    __TITLE_ACCOUNT_DELETED = '[data-qa="account-deleted"]'
    __CLOSE_CAMPAIGN = "#dismiss-button-element"


    def signup_btn(self):
        self.click(self.__SignUpBtn)

    def signup(self,name, email):
        self.click(self.__SignUpBtn)
        self.fill_text(self.__NAME_REG_FIELD, name)
        self.fill_text(self.__EMAIL_REG_FIELD, email)
        self.click(self.__SIGN_UP_BTN)

    def fill_account_info(self,password,birth_day,month_day,year_day,first_name,last_name,address,country_drop,stat,city,zipcode,phone_number):
        self.click(self.__CHOOSE_GENDER)
        self.fill_text(self.__PASSWORD_FIELD, password)
        self.select_option(self.__BIRTH_DATE_DAY, birth_day)
        self.select_option(self.__BIRTH_DATE_MONTH, month_day)
        self.select_option(self.__BIRTH_DATE_YEAR, year_day)
        self.fill_text(self.__FIRST_NAME_FIELD, first_name)
        self.fill_text(self.__LAST_NAME_FIELD, last_name)
        self.fill_text(self.__ADDRESS_FIELD, address)
        self.select_option(self.__COUNTRY_DROP_DOWN,country_drop)
        self.fill_text(self.__STAT_FIELD, stat)
        self.fill_text(self.__CITY_FIELD, city)
        self.fill_text(self.__ZIP_CODE_FIELD, zipcode)
        self.fill_text(self.__PHONE_FIELD, phone_number)
        self.click(self.__CREATE_ACCOUNT_BTN)



    def check_title(self, text):
        title = self.get_text(self.__GET_TITLE)
        return text in title

    def login(self,email_name,password):
        self.fill_text(self.__EMAIL_LOGIN_FIELD, email_name)
        self.fill_text(self.__PASSWORD_LOGIN_FIELD, password)
        self.click(self.__LOGIN_BTN)

    def get_user_title(self, text):
        title = self.get_text(self.__GET_HOME_PAGE_TITLE)
        return text in title

    def get_login_error_message(self, text):
        error_message = self.get_text(self.__LOGIN_ERROR_MSG)
        return text in error_message

    def get_error_msg_exiting_email(self, text):
        error_message = self.get_text(self.__GET_ERROR_EXITS_EMAIL)
        return text in error_message

    def delete_account(self, text):
        self.click(self.__DELETE_ACCOUNT)
        account_deleted_message = self.get_text(self.__TITLE_ACCOUNT_DELETED)
        return text in account_deleted_message







