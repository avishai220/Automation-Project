from tests.base_test import BaseTest
import allure
import os

from utlis.config import ConfigReader


class TestCheckOut(BaseTest):
    @allure.description(
        "test end to end choose products then login and then checkout and get title success")
    @allure.title("end to end test from login and checkout")
    def test_14_buy_products(self):
        email = ConfigReader.read_config("user", "email")
        password = ConfigReader.read_config("user", "password")
        self.products_page.click_products_btn()
        self.products_page.add_product_by_index(0)
        self.products_page.continue_shopping()
        self.home_page.wait_time(2)
        self.products_page.add_product_by_index(1)
        self.products_page.continue_shopping()
        self.home_page.wait_time(2)
        self.products_page.add_product_by_index(1)
        self.products_page.continue_shopping()
        self.home_page.wait_time(2)
        self.home_page.cart_btn()
        self.cart_page.check_out_btn()
        self.cart_page.register_btn()
        self.cart_page.wait_time(1)
        self.register_login_page.login(email, password)
        assert self.register_login_page.get_user_title
        self.home_page.cart_btn()
        self.cart_page.check_out_btn()
        assert self.cart_page.check_delivery_address(
            "avishai tal", "klil horesh", "nahariya", "Israel", "0549107716")
        self.cart_page.description("i love to write a code")
        self.cart_page.check_out_btn()
        self.cart_page.wait_time(2)
        self.cart_page.fill_payment("visa","4580343456432345","373","08","2027")
        assert self.cart_page.check_title("Congratulations! Your order has been confirmed!")

    @allure.description(
        "first login and then choose products and buy them and checkout")
    @allure.title("login and checkout after choose products")
    def test_15_login_and_buy_products(self):
        user_email = ConfigReader.read_config("user", "email")
        user_password = ConfigReader.read_config("user", "password")
        self.register_login_page.signup_btn()
        self.register_login_page.login(user_email, user_password)
        assert self.register_login_page.get_user_title
        self.products_page.click_products_btn()
        self.products_page.add_product_by_index(0)
        self.products_page.continue_shopping()
        self.home_page.wait_time(2)
        self.products_page.add_product_by_index(1)
        self.products_page.continue_shopping()
        self.home_page.wait_time(2)
        self.products_page.add_product_by_index(1)
        self.products_page.continue_shopping()
        self.home_page.wait_time(2)
        self.home_page.cart_btn()
        self.cart_page.check_out_btn()
        self.cart_page.wait_time(1)
        self.home_page.cart_btn()
        self.cart_page.check_out_btn()
        assert self.cart_page.check_delivery_address(
            "avishai tal", "klil horesh", "nahariya", "Israel", "0549107716")
        self.cart_page.description("i love to write a code")
        self.cart_page.check_out_btn()
        self.cart_page.wait_time(2)
        self.cart_page.fill_payment("visa","4580343456432345","373","08","2027")
        assert self.cart_page.check_title("Congratulations! Your order has been confirmed!")




