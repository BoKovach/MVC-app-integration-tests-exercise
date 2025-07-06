from abc import abstractmethod, ABC
from selenium.webdriver.common.by import By


class BasePage(ABC):
    def __init__(self, driver):
        self.driver = driver

    @abstractmethod
    def page_url(self):
        pass

    def open(self):
        self.driver.get(self.page_url)

    def is_currently_open(self):
        return self.driver.current_url == self.page_url
    
    @property
    def link_home_page(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'body > header > a:nth-child(1)')

    @property
    def link_view_students_page(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'body > header > a:nth-child(3)')
    
    @property
    def link_view_add_student_page(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'body > header > a:nth-child(5)')
    
    @property
    def element_text_heading(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'body > header > a:nth-child(7)')

    def go_to_home_page(self):
        self.link_home_page.click()

    def go_to_view_students_page(self):
        self.link_view_add_student_page.click()

    def go_to_add_students_page(self):
        self.link_view_students_page.click()

    def get_page_title(self):
        return self.driver.title

    def get_page_heading(self):
        return self.element_text_heading.text
