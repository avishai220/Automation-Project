from pages.base_page import BasePage
from playwright.sync_api import Page


class CartPage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)

    __CART_BTN = ".shop-menu a[href='/view_cart']"
    __PRODUCTS_LIST = "#cart_info_table tbody .cart_description h4 a"
    __PRODUCTS_QUANTITY = ".cart_quantity"
    __CHECK_OUT_BTN = ".btn.btn-default.check_out"
    __register_login = ".text-center [href='/login']"
    __ADDRESS_DETAILS = ".address.item.box"
    __DESCRIPTION_FIELD = ".form-control"
    __PLACE_ORDER_BTN = ".btn.btn-default.check_out"
    __NAME_ON_CARD_FIELD = '[name="name_on_card"]'
    __CARD_NUMBER_FIELD = '[name="card_number"]'
    __CVC_FIELD = '[data-qa="cvc"]'
    __EXPIRATION_FIELD = '[name="expiry_month"]'
    __YEAR_FIELD = '[data-qa="expiry-year"]'
    __CONFIRM_ORDER = "#submit"
    __TITLE_ORDER = ".col-sm-9.col-sm-offset-1"
    __REMOVE_PRODUCT_BTN = ".fa.fa-times"
    __GET_EMPTY_CART_TITLE = "#empty_cart "

    def get_cart_product_names(self):
        return self.get_all_texts(self.__PRODUCTS_LIST)

    def get_quantity(self):
        quantity_number = self.get_all_texts(self.__PRODUCTS_QUANTITY)
        print(f"actual: {repr(quantity_number)}")
        return self.get_all_texts(self.__PRODUCTS_QUANTITY)

    def check_out_btn(self):
        self.click(self.__CHECK_OUT_BTN)

    def register_btn(self):
        self.click(self.__register_login)

    def check_delivery_address(self, *fields):
        address = self.get_text(self.__ADDRESS_DETAILS)
        print(f"actual: {repr(address)}")
        return all(field in address for field in fields)

    def description(self, field):
        self.fill_text(self.__DESCRIPTION_FIELD, field)

    def fill_payment(self, name_field, card_number,cvc,expiry_month,expiry_year):
        self.fill_text(self.__NAME_ON_CARD_FIELD, name_field)
        self.fill_text(self.__CARD_NUMBER_FIELD, card_number)
        self.fill_text(self.__CVC_FIELD, cvc)
        self.fill_text(self.__EXPIRATION_FIELD, expiry_month)
        self.fill_text(self.__YEAR_FIELD, expiry_year)
        self.click(self.__CONFIRM_ORDER)



    def check_title(self,title):
        title_order = self.get_text(self.__TITLE_ORDER)
        return title in title_order

    def remove_products(self, text):
        self.click(self.__REMOVE_PRODUCT_BTN)
        title = self.get_text(self.__GET_EMPTY_CART_TITLE)
        return text in title
