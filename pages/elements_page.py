from locators.elements_page_locators import CheckBoxPageLocators, TextBoxPageLocators
from pages.base_page import BasePage
from generator.generator import generated_person

class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info= next(generated_person())
        full_name=person_info.full_name
        email=person_info.email
        current_address=person_info.current_address
        permanent_address=person_info.permanent_address

        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return full_name, email, current_address, permanent_address


    def check_filled_fields(self):
        output_name= self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1].strip()
        output_email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1].strip()
        output_current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1].strip()
        output_permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1].strip()
        return output_name, output_email, output_current_address, output_permanent_address


class CheckBoxPage(BasePage):
    locators= CheckBoxPageLocators()

    def click_on_check_box_home(self):
        self.element_is_visible(self.locators.CHECK_BOX_HOME).click()
        return self.element_is_visible(self.locators.CHECK_BOX_HOME_RESULT).text.split(':')[1].strip().split('\n')
         