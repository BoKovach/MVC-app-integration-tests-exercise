import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()

    # options.add_argument('--headless')

    driver = webdriver.Chrome(options=options, service=service)
    yield driver
    driver.quit()
