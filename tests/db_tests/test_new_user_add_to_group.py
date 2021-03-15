from pages.django_pages.base_page import BasePage
from pages.django_pages.main_page import MainPage
from time import sleep


def test_open_admin(browser):
    base_page = BasePage(browser)
    base_page.open_base_page()
    print('ok')
    sleep(5)
