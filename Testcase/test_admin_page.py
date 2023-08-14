import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Project.Pageobject.admin_page import AdminPage

@pytest.fixture
def setup():
    service = Service(executable_path="C:\\Users\\Nandhu\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield driver
    driver.quit()

def  test_TC_PIM_02(setup):
     obj = AdminPage(setup)
     obj.valid_login("Admin","admin123")
     obj.admin_page()

def test_TC_Pim_02(setup):
    obj = AdminPage(setup)
    obj.valid_login("Admin", "admin123")
    obj.admin_page_validation()




