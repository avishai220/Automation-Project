from pages.base_page import BasePage
from playwright.sync_api import Page
import pytest


class HomePage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)







    __LOG_OUT = '[href="/logout"]'
    __LOGOUT_TITLE = ".login-form"
    __SUBSCRIBE_EMAIL = "#susbscribe_email"
    __SUBSCRIBE_BTN = "#subscribe"
    __SUBSCRIBE_TITLE = ".single-widget"
    __TOP_TITLE = "#slider .carousel-inner h2:visible"
    __SUCCESS_SUBSCRIBE = "#success-subscribe"
    __PRODUCTS_BTN = '[href="/products"]'
    __CART_BTN = ".shop-menu a[href='/view_cart']"
    __CATEGORY_WOMEN = '[href="#Women"]'
    __DRESS_BTN = '[href="/category_products/1"]'
    __TITLE_WOMEN_CATEGORY = ".title.text-center"
    __CATEGORY_MEN = '[href="#Men"]'
    __JEANS_BTN = '[href="/category_products/6"]'
    __TITLE_MEN_CATEGORY = ".title.text-center"



    def logout_btn(self):
        self.click(self.__LOG_OUT)

    def get_logout_title(self, text):
        logout_title = self.get_text(self.__LOGOUT_TITLE)
        return text in logout_title

    def subscribe(self,email,text):
        self.fill_text(self.__SUBSCRIBE_EMAIL, email)
        self.click(self.__SUBSCRIBE_BTN)
        title = self.get_text(self.__SUCCESS_SUBSCRIBE)
        return text in title

    def cart_btn(self):
        self.click(self.__CART_BTN)

    def select_category_women(self, women_title):
        self.click(self.__CATEGORY_WOMEN)
        self.click(self.__DRESS_BTN)
        title = self.get_text(self.__TITLE_WOMEN_CATEGORY)
        print(f"actual: {repr(title)}")
        return women_title in title

    def select_category_men(self, men_title):
        self.click(self.__CATEGORY_MEN)
        self.click(self.__JEANS_BTN)
        title = self.get_text(self.__TITLE_MEN_CATEGORY)
        print(f"actual: {repr(title)}")
        return men_title in title

    def get_footer_title(self, text):
        title = self.get_text_when_visible(self.__SUBSCRIBE_TITLE)
        return text.upper() in title.upper()

    def get_top_title(self, top_title):
        title = self.get_text_when_visible(self.__TOP_TITLE)
        return top_title.upper() in title.upper()




