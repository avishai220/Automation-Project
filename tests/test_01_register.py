import pytest


from tests.base_test import BaseTest
import allure




class TestRegisterPage(BaseTest):

    @allure.description(
        "fill information in register page")
    @allure.title("fill information in register page")
    def test_01_register_page(self):
        self.register_login_page.signup("avishai","avishai220@walla.com")
        self.register_login_page.fill_account_info("asd12345","12", "May", "1986","avishai","tal"
             ,"klil horesh","Israel","north","nahariya","2221218","0549107716")
        assert self.register_login_page.check_title("ACCOUNT CREATED")

    @allure.description(
        "test the login page with correct username and password")
    @allure.title("login in login page")
    def test_02_login(self):
        self.register_login_page.signup_btn()
        self.register_login_page.login("avishai220@walla.com","asd12345")
        assert self.register_login_page.get_user_title("Logged in as")

    @allure.description(
        "test the login page with incorrect username and password")
    @allure.title("login in login page with incorrect username and password")
    def test_03_incorrect_login(self):
        self.register_login_page.signup_btn()
        self.register_login_page.login("avishai220@wall.com", "asd1234")
        assert self.register_login_page.get_login_error_message("Your email or password is incorrect")

    @allure.description(
        "test the login page with the exiting email ")
    @allure.title("login in login page with exiting email")
    def test_04_fill_exiting_email_reg_page(self):
        self.register_login_page.signup("yosi","avishai220@walla.com")
        assert self.register_login_page.get_error_msg_exiting_email("Email Address already exist!")

    @allure.description(
        "deleting account and checking if the account is deleted")
    @allure.title("deleting account")
    @pytest.mark.skip(reason="Deletes the shared account used by other tests")
    def test_05_delete_account(self):
        self.register_login_page.signup_btn()
        self.register_login_page.login("avishai220@walla.com", "asd12345")
        assert self.register_login_page.delete_account("ACCOUNT DELETED!")




