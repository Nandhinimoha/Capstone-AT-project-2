import time

from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver import Keys
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
            actual_title = self.driver.title
            expected_title = "OrangeHRM"
            if actual_title == expected_title:
                print("------------------Header Validation!!--------------------")
        except TimeoutException as e:
            print(e)
    # Test case: TC_PIM_03 (Main menu Validation)
    def admin_search(self):
       try:
           search = self.wait.until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Search']")))
           search.send_keys("admin")
           admin = self.wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li/a")))
           if admin.is_displayed():
               print("admin is displayed!!")

           search1 = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
           search1.send_keys(5*Keys.BACKSPACE)
           search1.send_keys("ADMIN")
           admin = self.wait.until(
               EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li/a")))
           if admin.is_displayed():
               print("ADMIN is displayed!!")

           search1 = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
           search1.send_keys(5 * Keys.BACKSPACE)
           search1.send_keys("pim")
           Pim = self.wait.until(
               EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li/a")))
           if Pim.is_displayed():
               print("pim is displayed!!")
           search1 = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
           search1.send_keys(5 * Keys.BACKSPACE)
           search1.send_keys("PIM")
           Pim = self.wait.until(
               EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li/a")))
           if Pim.is_displayed():
               print("PIM is displayed!!")

           search1 = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
           search1.send_keys(10 * Keys.BACKSPACE)
           search1.send_keys("leave")
           leave = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li/a")))
           if leave.is_displayed():
               print("leave is displayed!!")

           search1 = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
           search1.send_keys(10 * Keys.BACKSPACE)
           search1.send_keys("leave")
           leave = self.wait.until(
               EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li/a")))
           if leave.is_displayed():
               print("LEAVE is displayed!!")

           search1 = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
           search1.send_keys(10 * Keys.BACKSPACE)
           search1.send_keys("time")
           time = self.wait.until(
               EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li/a")))
           if time.is_displayed():
               print("time is displayed!!")

           search1 = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
           search1.send_keys(10 * Keys.BACKSPACE)
           search1.send_keys("TIME")
           time = self.wait.until(
               EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li/a")))
           if time.is_displayed():
               print("TIME is displayed!!")

           search1 = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
           search1.send_keys(20 * Keys.BACKSPACE)
           search1.send_keys("recruitment")
           recruitment = self.wait.until(
               EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li/a")))
           if recruitment.is_displayed():
               print("recruitment is displayed!!")

           search1 = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
           search1.send_keys(30 * Keys.BACKSPACE)
           search1.send_keys("RECRUITMENT")
           recruitment = self.wait.until(
               EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li/a")))
           if recruitment.is_displayed():
               print("RECRUITMENT is displayed!!")


           search1 = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
           search1.send_keys(30 * Keys.BACKSPACE)
           search1.send_keys("my info")
           my_info = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li/a")))
           if my_info.is_displayed():
               print("my info is displayed!!")


           search1 = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
           search1.send_keys(10 * Keys.BACKSPACE)
           search1.send_keys("MY INFO")
           my_info = self.wait.until(
               EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li/a")))
           if my_info.is_displayed():
               print ("MY INFO is displayed!!")



           search1 = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
           search1.send_keys(20 * Keys.BACKSPACE)
           search1.send_keys("performance")
           performance = self.wait.until(
               EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li/a")))
           if performance.is_displayed():
               print("performance is displayed!!")



           search1 = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
           search1.send_keys(20 * Keys.BACKSPACE)
           search1.send_keys("PERFORMANCE")
           performance = self.wait.until(
               EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li/a")))
           if performance.is_displayed():
               print("PERFORMANCE is displayed!!")

           search1 = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
           search1.send_keys(20 * Keys.BACKSPACE)
           search1.send_keys("dashboard")
           dashboard = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li/a")))
           if dashboard.is_displayed():
               print("dashboard is displayed!!")

           search1 = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
           search1.send_keys(20 * Keys.BACKSPACE)
           search1.send_keys("DASHBOARD")
           dashboard = self.wait.until(
               EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li/a")))
           if dashboard.is_displayed():
               print("DASHBOARD is displayed!!")


           search1 = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
           search1.send_keys(20 * Keys.BACKSPACE)
           search1.send_keys("directory")
           directory = self.wait.until(
               EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li/a")))
           if directory.is_displayed():
               print("directory is displayed!!")



           search1 = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
           search1.send_keys(20 * Keys.BACKSPACE)
           search1.send_keys("DIRECTORY")
           directory= self.wait.until(
               EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li/a")))
           if directory.is_displayed():
               print("DIRECTORY is displayed!!")



           search1 = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
           search1.send_keys(20 * Keys.BACKSPACE)
           search1.send_keys("maintenance")
           maintenance = self.wait.until(
               EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li/a")))
           if maintenance.is_displayed():
               print("maintenance is displayed!!")

           search1 = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
           search1.send_keys(20 * Keys.BACKSPACE)
           search1.send_keys("MAINTENANCE")
           maintenance = self.wait.until(
               EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li/a")))
           if maintenance.is_displayed():
               print("MAINTENANCE is displayed!!")


           search1 = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
           search1.send_keys(15 * Keys.BACKSPACE)
           search1.send_keys("claim")
           claim = self.wait.until(
               EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li/a")))
           if claim.is_displayed():
               print("claim is displayed!!")

           search1 = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
           search1.send_keys(15 * Keys.BACKSPACE)
           search1.send_keys("CLAIM")
           claim = self.wait.until(
               EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li/a")))
           if claim.is_displayed():
               print("CLAIM is displayed!!")


           search1 = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
           search1.send_keys(15 * Keys.BACKSPACE)
           search1.send_keys("buzz")
           buzz = self.wait.until(
               EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li/a")))
           if buzz.is_displayed():
               print("buzz is displayed!!")

           search1 = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
           search1.send_keys(15 * Keys.BACKSPACE)
           search1.send_keys("BUZZ")
           buzz = self.wait.until(
               EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li/a")))
           if buzz.is_displayed():
               print("BUZZ is displayed!!")

           print(" All the main menu options are displayed")


       except TimeoutException as e:
           print(e)


    #Test case: TC_PIM_03 (Using for loop in validation)
    def main_menu(self):
        try:
            admin = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a")))
            admin.click()
            menu= self.wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul")))
            list_elements = menu.find_elements(By.TAG_NAME,"li")
            print(len(list_elements))
            expected_options =["Admin", "PIM","Leave","Time","Recruitment","My Info","Performance ","Dashboard" ,"Directory","Maintenance","Claim ","Buzz","Main menu"]
            for expected_option in expected_options:
                for option_element in list_elements:
                    if expected_option in option_element.text:
                        print(f"{expected_option} option is displayed.")

            print("All the main menu options are displayed!!")

            # for l in list_elements:
            #     print(l.text + " is displayed ")
            # print("Main menu options are displayed")
        except TimeoutException as e:
            print(e)