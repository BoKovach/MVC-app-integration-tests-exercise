from selenium.webdriver.common.by import By

from tests.pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def page_url(self):
        return "http://localhost:8080/"

    def get_students_count(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'body > p > b')
