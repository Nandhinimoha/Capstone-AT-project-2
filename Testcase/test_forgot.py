import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Project.Pageobject.forgot_password import Forgot_password



@pytest.fixture
def setup():
    service = Service(executable_path="C:\\Users\\Nandhu\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    yield driver
    driver.quit()

# Test case: TC_PIM_01
def test_forgot(setup):
    obj = Forgot_password(setup)
    obj.login_page("Admin")

def test_invalid_username(setup):
    obj1 = Forgot_password(setup)
    obj1.login_page("guvi@gmail.com")

def test_invalid_username_numbers(setup):
    obj2 = Forgot_password(setup)
    obj2.login_page("244544")

def test_invalid_special_chars(setup):
    obj3 = Forgot_password(setup)
    obj3.login_page("$##%&@@")

def test_invalid_credentials(setup):
    obj4 = Forgot_password(setup)
    obj4.login_page("Adghwe#2sdf ")

def test_negative_case(setup):
    obj5 = Forgot_password(setup)
    obj5.login_page(" ")
