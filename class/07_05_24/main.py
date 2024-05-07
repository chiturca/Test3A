from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains

class Test_Sauce:
    # def initializeDriver(self):
        # driver = webdriver.Chrome()
        # driver.get("https://www.saucedemo.com/")
        # driver.maximize_window()
        # return driver
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()

    def test_invalid_login(self):
        # driver = self.initializeDriver()
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        username = self.driver.find_element(By.ID,"user-name")
        username.send_keys("1")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        password = self.driver.find_element(By.NAME,"password")
        password.send_keys("1")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        # sleep(5)
        # errorMessage = driver.find_element(By.CLASS_NAME, "error-button")
        # testResult = errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        # print(f"Test Sonucu: {testResult}") #Test Sonucu: False
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"Invalid Test Result:  {testResult}")
        # sleep(5)

    def test_valid_login(self):
        # driver = self.initializeDriver()
        self.driver.get("https://www.saucedemo.com/")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        username = self.driver.find_element(By.ID,"user-name")
        # username.send_keys("standard_user")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        password = self.driver.find_element(By.NAME,"password")
        # password.send_keys("secret_sauce")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginButton = self.driver.find_element(By.ID,"login-button")
        #action chains
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(username, "standard_user")
        actions.send_keys_to_element(password, "secret_sauce")
        actions.move_to_element(loginButton)
        actions.perform() #depolanmış aksiyonlarımızı çalıştırır
        loginButton.click()
        appLogo = self.driver.find_element(By.CLASS_NAME,"app_logo")
        testResult = appLogo.text == "Swag Labs"
        print(f"Valid Test Result: {testResult}")
        # sleep(5)
testClass = Test_Sauce()
testClass.test_invalid_login()
testClass.test_valid_login()

# self.driver.execute.script("window.scrollTo(0,500)") #Browser consoleda sayfayı en aşağı kaydırıyor