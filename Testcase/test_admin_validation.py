import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Project.Pageobject.admin_validate import AdminPage

@pytest.fixture
def setup():
    service = Service(executable_path="C:\\Users\\Nandhu\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    yield driver
    driver.quit()


def  test_TC_PIM_03(setup):
     obj = AdminPage(setup)
     obj.valid_login("Admin","admin123")
     obj.admin_search()
def test_TC_Pim_03(setup):
    obj1 = AdminPage(setup)
    obj1.valid_login("Admin","admin123")
    obj1.main_menu()


