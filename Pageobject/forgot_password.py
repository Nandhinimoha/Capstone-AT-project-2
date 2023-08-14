from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Forgot_password:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.actions = ActionChains(self.driver)
    def login_page(self,username):
        before_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/requestPasswordResetCode"
        forgot_pass = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']")))
        forgot_pass.click()

        username_textbox = self.wait.until(EC.visibility_of_element_located((By.NAME, "username")))
        username_textbox.send_keys(username)

        reset_btn = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        reset_btn.click()
        after_url = self.driver.current_url

        try:

            if before_url != after_url:
                print("Reset Password link sent successfully")
            elif before_url == after_url:
                print("Username Required!!")
           # success_message = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/div/h6"))) # Validate the success message
           # if success_message.is_displayed():

           #     print("Reset Password link sent successfully")
           # elif self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT,"Required"))).is_displayed():
           #     print("Invalid username!!!")
        except TimeoutException as e:
            print(e)