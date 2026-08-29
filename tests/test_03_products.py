from tests.base_test import BaseTest
import allure

from utlis.config import ConfigReader


class TestRegisterPage(BaseTest):

    @allure.description(
        "count products and view first product detail")
    @allure.title("check the products page information")
    def test_07_view_products(self):
        self.register_login_page.signup_btn()
        self.register_login_page.login("avishai220@walla.com", "asd12345")
        self.products_page.click_products_btn()
        assert self.products_page.count_products()>10
        self.products_page.click_view_product_btn()
        assert self.products_page.check_details_products("Category", "Rs.", "Availability", "Condition", "Brand")

    @allure.description(
        "search product by name and valid is name in the view page of products page")
    @allure.title("valid the product name in product view after search")
    def test_08_search_products(self):
        email = ConfigReader.read_config("user", "email")
        password = ConfigReader.read_config("user", "password")
        self.register_login_page.signup_btn()
        self.register_login_page.login(email, password)
        self.products_page.click_products_btn()
        assert self.products_page.search_product("Sleeveless Dress", "Sleeveless Dress")

    @allure.description(
        "add products to cart and check the products by name in cart")
    @allure.title("add products to cart")
    def test_09_add_to_cart(self):
        self.products_page.add_product_by_index(0)
        self.products_page.continue_shopping()
        self.products_page.add_product_by_index(1)
        self.products_page.continue_shopping()
        self.products_page.cart_btn()
        names = self.cart_page.get_cart_product_names()
        assert "Blue Top" in names
        assert "Men Tshirt" in names

    @allure.description(
        "view category products in page and check the title")
    @allure.title("view category products in page")
    def test_10_category_products(self):
        assert self.home_page.select_category_women("DRESS PRODUCTS")
        assert self.home_page.select_category_men("JEANS PRODUCTS")

    @allure.description(
        "go to brand product page and view the list of brands list")
    @allure.title("go to brand page")
    def test_11_view_brand_products(self):
        self.products_page.click_products_btn()
        assert self.products_page.view_brand_page(
            "POLO", "H&M", "MADAME", "MAST & HARBOUR",
            "BABYHUG", "ALLEN SOLLY JUNIOR", "KOOKIE KIDS", "BIBA"
        )
        assert self.products_page.choose_brand("POLO PRODUCTS")


    def test_19_add_review_on_product(self):
        self.products_page.click_products_btn()
        assert self.products_page.product_button("Beautiful Peacock Blue Cotton Linen")
        assert self.products_page.fill_info_feed_back("avishai","avishai220@walla.com","i love to write automation", "Thank you for your review.")




