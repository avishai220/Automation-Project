from pages.cart_page import CartPage
from pages.contact_us_page import ContactUsPage
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.register_login_page import RegisterLoginPage


class BaseTest:
    register_login_page:  RegisterLoginPage
    home_page: HomePage
    contact_us_page: ContactUsPage
    products_page: ProductsPage
    cart_page: CartPage
