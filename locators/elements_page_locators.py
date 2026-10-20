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
    #COLLAPSE_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Collapse all']")
    #CHECKBOXES = (By.CSS_SELECTOR, "span[class='rct-checkbox']")
    #CHECKED_CHECKBOXES = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    #TITLE_ITEM = (By.CSS_SELECTOR, "span[class='rct-title']")

    CHECK_BOX_HOME_RESULT = (By.CSS_SELECTOR, '#result')