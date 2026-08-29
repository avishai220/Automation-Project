from tests.base_test import BaseTest
import allure
import os




class TestCart(BaseTest):

    @allure.description("check if you can subscribe after you added some products")
    @allure.title("subscribe after you added some products")
    def test_16_subscribe(self):
        self.home_page.cart_btn()
        assert self.home_page.subscribe("ggg@gmail.com", "You have been successfully subscribed!")

    @allure.description("add some products and test the quantity in the cart")
    @allure.title("test the quantity in the cart")
    def test_17_verify_quantity(self):
        self.products_page.add_product_by_index(0)
        self.products_page.continue_shopping()
        self.products_page.add_product_by_index(1)
        self.products_page.continue_shopping()
        self.products_page.add_product_by_index(1)
        self.products_page.continue_shopping()
        self.home_page.cart_btn()
        assert self.cart_page.get_quantity()

    @allure.description("test if you can remove products and what the result")
    @allure.title("remove products from cart")
    def test_18_remove_products(self):
        self.products_page.click_products_btn()
        self.products_page.add_product_by_index(0)
        self.products_page.continue_shopping()
        self.home_page.cart_btn()
        assert self.cart_page.remove_products("Cart is empty")

