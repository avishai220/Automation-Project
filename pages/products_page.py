from pages.base_page import BasePage
from playwright.sync_api import Page
import pytest


class ProductsPage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)


    __PRODUCTS_BTN = '[href="/products"]'
    __PRODUCT_LIST = ".product-image-wrapper"
    __VIEW_PRODUCT = '[href="/product_details/1"]'
    __PRODUCT_INFORMATION = ".product-information"
    __SEARCH_FIELD = '[name="search"]'
    __SEARCH_BTN = '[type="button"]'
    __PRODUCT_NAME = ".single-products"
    __PRODUCT_CARD = ".product-image-wrapper"
    __ADD_TO_CART_BTN = ".product-overlay .add-to-cart"
    __CONTINUE_SHOPPING = ".btn.btn-success.close-modal.btn-block"
    __CART_BTN = ".shop-menu a[href='/view_cart']"
    __BRANDS_LIST_NAME = ".brands-name"
    __BTN_BRAND_POLO = '[href="/brand_products/Polo"]'
    __POLO_TITLE_PAGE = ".title.text-center"
    __VIEW_PRODUCT_BUTTON = '[href="/product_details/41"]'
    __NAME_FIELD = "#name"
    __EMAIL_FIELD = "#email"
    __ADD_REVIEW_FIELD = '[name="review"]'
    __REVIEW_BUTTON = "#button-review"
    __GET_REVIEW_TITLE = "#review-section .alert-success span"




    def click_products_btn(self):
        self.click(self.__PRODUCTS_BTN)

    def count_products(self):
        products = self.count_elements(self.__PRODUCT_LIST)
        print(f"products found: {products}")
        return products

    def click_view_product_btn(self):
        self.click(self.__VIEW_PRODUCT)
        return self.get_text(self.__PRODUCT_INFORMATION)

    def check_details_products(self, *fields):
        text = self.get_text_when_visible(self.__PRODUCT_INFORMATION)
        print(f"actual: {repr(text)}")
        return all(field.upper() in text.upper() for field in fields)

    def search_product(self, text, product_name):
        self.fill_text(self.__SEARCH_FIELD,text)
        self.click(self.__SEARCH_BTN)
        product = self.get_text(self.__PRODUCT_NAME)
        return product_name in product

    def add_product_by_index(self, index):
        self.hover_by_index(self.__PRODUCT_CARD, index)
        self.wait_time(2)
        self.click_by_index_force(self.__ADD_TO_CART_BTN, index)
        self.wait_time_visible(self.__CONTINUE_SHOPPING)

    def continue_shopping(self):
        self.click(self.__CONTINUE_SHOPPING)

    def cart_btn(self):
        self.click(self.__CART_BTN)

    def view_brand_page(self, *brand_name):
        brands = self.get_text(self.__BRANDS_LIST_NAME)
        print(f"actual: {repr(brands)}")
        return all(brand in brands for brand in brand_name)

    def choose_brand(self, polo_title):
        self.click(self.__BTN_BRAND_POLO)
        title = self.get_text(self.__POLO_TITLE_PAGE)
        return polo_title in title

    def product_button(self, text):
        self.click(self.__VIEW_PRODUCT_BUTTON)
        product_name = self.get_text(self.__PRODUCT_INFORMATION)
        return text in product_name

    def fill_info_feed_back(self,name,email,review,title):
        self.fill_text(self.__NAME_FIELD, name)
        self.fill_text(self.__EMAIL_FIELD, email)
        self.fill_text(self.__ADD_REVIEW_FIELD, review)
        self.click(self.__REVIEW_BUTTON)
        title_message = self.get_text(self.__GET_REVIEW_TITLE)
        return title in title_message














