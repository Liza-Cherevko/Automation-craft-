from pages.base_page import BasePage
from pages.elements_page import TextBoxPage
import time

def test(driver):
    page = TextBoxPage(driver, 'https://demoqa.com/text-box')
    page.open()
    page.fill_all_fields()
    output_name, output_email, output_current_address, output_permanent_address = page.check_filled_fields()
    full_name, email, current_address, permanent_address = page.check_filled_fields()
    assert full_name == output_name
    assert email==output_email
    assert current_address==output_current_address
    assert permanent_address==output_permanent_address
    print(full_name)
    print(email)
    print(current_address)
    print(permanent_address)
    print(output_name)
    print(output_email)
    print(output_current_address)
    print(output_permanent_address)    