from pages.base_page import BasePage
from pages.elements_page import TextBoxPage
import time

def test(driver):
    page = TextBoxPage(driver, 'https://demoqa.com/text-box')
    page.open()
    page.fill_all_fields()
    time.sleep(3)
    time.sleep(3)