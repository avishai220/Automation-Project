from tests.base_test import BaseTest
import allure
import os

from utlis.config import ConfigReader


class TestContactUs(BaseTest):

    @allure.description(
        "press on contact us btn and then fill the fields with information and uploading a file")
    @allure.title("contact support and press submit")
    def test_06_contact_us(self):
        email = ConfigReader.read_config("user", "email")
        password = ConfigReader.read_config("user", "password")

        self.register_login_page.signup_btn()
        self.register_login_page.login(email, password)
        self.contact_us_page.contact_us_btn("Get In Touch")
        self.contact_us_page.contact_us_fields("avishai", email,
                                               "hi my name is avishai and im testing my abilities")

        file_path = os.path.join(os.path.dirname(__file__), "..", "test_data", "test_upload.docx")
        self.contact_us_page.attach_file(file_path)
        assert self.contact_us_page.submit_btn("Success! Your details have been submitted successfully")





