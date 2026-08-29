import allure
import pytest
import os

from pages.cart_page import CartPage
from pages.contact_us_page import ContactUsPage
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.register_login_page import RegisterLoginPage

browser_info = {}


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {**browser_type_launch_args, "args": ["--start-maximized"]}


@pytest.fixture(scope="function", autouse=True)
def setup_page_class(request, browser):
    context = browser.new_context(no_viewport=True, accept_downloads=True)
    page = context.new_page()
    page.on("dialog", lambda dialog: dialog.accept())

    # תפיסת מידע על הדפדפן (לדוח environment)
    browser_info["browser"] = browser.browser_type.name
    browser_info["version"] = browser.version

    page.route(
        "**/*",
        lambda route: route.abort()
        if "googlesyndication" in route.request.url
           or "doubleclick" in route.request.url
           or "googleads" in route.request.url
        else route.continue_()
    )

    page.goto("https://automationexercise.com/")
    page.keyboard.press("Escape")
    if page.locator(".red-hover").count() > 0:
        page.locator(".red-hover").click()

    request.cls.page = page
    request.cls.register_login_page = RegisterLoginPage(page)
    request.cls.home_page = HomePage(page)
    request.cls.contact_us_page = ContactUsPage(page)
    request.cls.products_page = ProductsPage(page)
    request.cls.cart_page = CartPage(page)

    yield

    page.close()
    context.close()

# צילום מסך אוטומטי כשטסט נכשל
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = getattr(item.instance, "page", None)
        if page:
            allure.attach(
                page.screenshot(),
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG
            )


# כתיבת מידע הסביבה לדוח (בסוף הריצה)
def pytest_sessionfinish():
    if browser_info:
        allure_env_path = os.path.join("allure-results", "environment.properties")
        with open(allure_env_path, "w") as f:
            data = "\n".join([f"{key}={value}" for key, value in browser_info.items()])
            f.write(data)


