from selenium.webdriver.common.by import By

class TextBoxPageLocators:
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[id='submit']")



    CREATED_FULL_NAME= (By.CSS_SELECTOR, '#output #name')
    CREATED_EMAIL = (By.CSS_SELECTOR, '#output #email')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#output #currentAddress')
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#output #permanentAddress')


class CheckBoxPageLocators:
    CHECK_BOX_HOME = (By.CSS_SELECTOR, "span.rc-tree-checkbox")
    SWITCHER_HOME=(By.CSS_SELECTOR, '.rc-tree-switcher_close')

    CHECK_BOX_DESKTOP=(By.CSS_SELECTOR, '[title="Desktop"]')
    SWITCHER_DESKTOP=(By.CSS_SELECTOR, '.rc-tree-switcher.rc-tree-switcher_close')

    CHECK_BOX_DOCUMENTS=(By.CSS_SELECTOR, '[title="Documents"]')
    CHECK_BOX_DOWNLOADS=(By.CSS_SELECTOR, '[title="Downloads"]')
    NOTES=(By.CSS_SELECTOR, '[title=Notes]')
    COMMANDS=(By.CSS_SELECTOR, '[title=Commands]')


    CHECK_BOX_HOME_RESULT = (By.CSS_SELECTOR, '#result')
    
