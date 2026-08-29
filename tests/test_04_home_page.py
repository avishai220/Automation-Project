

from tests.base_test import BaseTest
import allure

from utlis.config import ConfigReader


class TestHomePage(BaseTest):

    @allure.description(
        "test the logout btn and check if user move to login page")
    @allure.title("test the logout btn")
    def test_12_log_out(self):
        email = ConfigReader.read_config("user", "email")
        password = ConfigReader.read_config("user", "password")
        self.register_login_page.signup_btn()
        self.register_login_page.login(email, password)
        self.home_page.logout_btn()
        assert self.home_page.get_logout_title("Login to your account")

    @allure.description(
        "test the subscribe field and if you get success message")
    @allure.title("test the subscribe field and button")
    def test_13_subscribe(self):
        assert self.home_page.subscribe("ggg@gmail.com", "You have been successfully subscribed!")

    @allure.description(
        "test if title in bottom is visible and scroll down and scroll up again and test if top title is visible")
    @allure.title("scroll up and down and check the titles")
    def test_scroll_up_down(self):
        self.home_page.scroll_to_bottom()
        assert self.home_page.get_footer_title("SUBSCRIPTION")
        self.home_page.scroll_to_top()
        assert self.home_page.get_top_title("Full-Fledged")


