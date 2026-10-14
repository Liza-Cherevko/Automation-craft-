from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
import time

@pytest.fixture(scope='function')
def driver():
    driver= webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()