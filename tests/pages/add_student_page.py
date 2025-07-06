from selenium.webdriver.common.by import By

from tests.pages.base_page import BasePage


class AddStudentPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        
    @property
    def page_url(self):
        return "http://localhost:8080/add-student"
    
    @property
    def field_student_name(self):
        return self.driver.get_element(By.CSS_SELECTOR, '#name')
    
    @property
    def field_student_email(self):
        return self.driver.get_element(By.CSS_SELECTOR, '#email')
    
    @property
    def button_add(self):
        return self.driver.get_element(By.CSS_SELECTOR, 'body > form > button')

    @property
    def element_error_msg(self):
        return self.driver.get_element(By.CSS_SELECTOR, '.err')

    def add_student(self, name, email):
        self.field_student_name.send_keys(name)
        self.field_student_email.send_keys(email)
        self.button_add.click()

    def get_error_msg(self):
        return self.element_error_msg.text
