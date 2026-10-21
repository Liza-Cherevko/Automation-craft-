from pages.base_page import BasePage
from pages.elements_page import CheckBoxPage, TextBoxPage
import time

class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            page.open()
            page.fill_all_fields()
            output_name, output_email, output_current_address, output_permanent_address = page.check_filled_fields()
            full_name, email, current_address, permanent_address = page.check_filled_fields()
            assert full_name == output_name
            assert email==output_email
            assert current_address==output_current_address
            assert permanent_address==output_permanent_address

class TestCheckBox:
    def test_check_box(self, driver):
        check_box_page= CheckBoxPage(driver, 'https://demoqa.com/checkbox')
        check_box_page.open()
        result= check_box_page.click_on_check_box_home()
        assert check_box_page.element_is_visible(check_box_page.locators.CHECK_BOX_DESKTOP)
        assert check_box_page.element_is_visible(check_box_page.locators.CHECK_BOX_DOCUMENTS)
        assert check_box_page.element_is_visible(check_box_page.locators.CHECK_BOX_DOWNLOADS)
        assert check_box_page.element_is_visible(check_box_page.locators.NOTES)
        assert check_box_page.element_is_visible(check_box_page.locators.COMMANDS)
        time.sleep(5)
        assert 'home' in result