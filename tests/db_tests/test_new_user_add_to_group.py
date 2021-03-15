from pages.django_pages.base_page import BasePage
from time import sleep


def test_open_admin(browser):
    base_page = BasePage(browser)
    base_page.open_base_page()
    sleep(5)
