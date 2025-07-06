import json

from selenium.webdriver.common.by import By

from tests.pages.base_page import BasePage


class ViewStudentsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def page_url(self):
        return "http://localhost:8080/students"

    def get_students_list(self):
        ul_elements = self.driver.find_element(By.CSS_SELECTOR, 'body > ul')
        return ul_elements.find_elements(By.TAG_NAME, 'li')
