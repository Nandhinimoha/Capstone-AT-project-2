from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminPage():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.maximize_window()
        self.username_Name = "username"
        self.password_Name = "password"
        self.login_btn = "button[type='submit']"  # CSS selector
    def valid_login(self, username, password):
        try:
            username_field = self.wait.until(EC.presence_of_element_located((By.NAME, self.username_Name)))
            username_field.send_keys(username)

            pswrd_field = self.wait.until(EC.presence_of_element_located((By.NAME, self.password_Name)))
            pswrd_field.send_keys(password)

            button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.login_btn)))
            button.click()
        except TimeoutException as e:
            print(e)
    def admin_page(self):
        try:
            admin = self.wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a")))
            admin.click()
            actual_title = self.driver.title
            expected_title = "OrangeHRM"
            if actual_title == expected_title:
                print("---------------------Header Validation!!-----------------------")

            ad = self.wait.until(EC.visibility_of_element_located((By.XPATH,"//nav[@aria-label='Topbar Menu']//ul")))
            li_elements = ad.find_elements(By.TAG_NAME,"li")
            print(len(li_elements))
            expected_options = ["User Management", "Job", "Organization", "Qualifications","Nationalities", "Corporate Branding", "Configuration"]
            for expected_option in expected_options:
                for option_element in li_elements:
                    if expected_option in option_element.text:
                        print(f"{expected_option} option is displayed.")

            # for list_element in li_elements:
            #     print(list_element.text + " is displayed")
            # print("Options are displayed in admin page")

        except TimeoutException as e:
            print(e)

    def admin_page_validation(self):
        admin = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a")))
        admin.click()
        actual_title = self.driver.title
        expected_title = "OrangeHRM"
        if actual_title == expected_title:
            print("---------------------Header Validation!!-----------------------")
        User_Management = self.wait.until(EC.visibility_of_element_located((By.XPATH,"//li[@class='oxd-topbar-body-nav-tab --parent --visited']")))
        if User_Management.is_displayed():
            print("User Management is Displayed!!")
        Job = self.wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]")))
        if Job.is_displayed():
            print("Job is Displayed!!")
        Organization = self.wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]")))
        if Organization.is_displayed():
            print("Organization is Displayed!!")
        Qualifications = self.wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[4]")))
        if Qualifications.is_displayed():
            print("Qualifications is Displayed!!")
        Nationalities = self.wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[5]")))
        if Nationalities.is_displayed():
            print("Nationalities is Displayed!!")
        Corporate_Branding = self.wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[6]")))
        if Corporate_Branding.is_displayed():
            print("Corporate Branding is Displayed!!")
        Configuration = self.wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[7]")))
        if Configuration.is_displayed():
            print("Configuration is Displayed!!")
        print("All the options are validated and displayed!!")