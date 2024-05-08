from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 2- Aşağıda verilen test caselerin hepsini "https://www.saucedemo.com/" sitesinde gerçekleştirmeniz istenmektedir.
# Yazacağınız tüm kodları oluşturduğunuz bir classda fonksiyonlar oluşturarak gerçekleştiriniz. Bu classın fonksiyonlarını çağırarak test ediniz.
# Test Caseler;
class SauceDemo_Test:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
    # -Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.
    def test_empty_login(self):
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage = self.driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div.error-message-container.error")
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print(f"Empty Login Fields Test Result:  {testResult}")
    # -Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.
    def test_empty_password_login(self):
        self.driver.get("https://www.saucedemo.com/")
        username = self.driver.find_element(By.ID,"user-name")
        username.send_keys("standard_user")
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id=\"login_button_container\"]/div/form/div[3]")
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print(f"Empty Password Field Test Result:  {testResult}")
    # -Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
    def test_locked_out_user_login(self):
        self.driver.get("https://www.saucedemo.com/")
        username = self.driver.find_element(By.ID,"user-name")
        username.send_keys("locked_out_user")
        password = self.driver.find_element(By.NAME,"password")
        password.send_keys("secret_sauce")
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage = self.driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div.error-message-container.error")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"Locked Out User Test Result:  {testResult}")
    # -Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir. Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.
    def test_success_login(self):
        self.driver.get("https://www.saucedemo.com/")
        username = self.driver.find_element(By.ID,"user-name")
        username.send_keys("standard_user")
        password = self.driver.find_element(By.NAME,"password")
        password.send_keys("secret_sauce")
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        find6InventoryItemContainer = self.driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div')
        find6InventoryItem = find6InventoryItemContainer.find_elements(By.CLASS_NAME, "inventory_item")
        testResult = len(find6InventoryItem) == 6
        print(f"Login Success Test Result:  {testResult}")
    # Bir tane de siz bulunuz. :)
    # Successful logout will be tested
    def test_success_logout(self):
        self.driver.get("https://www.saucedemo.com/")
        username = self.driver.find_element(By.ID,"user-name")
        username.send_keys("standard_user")
        password = self.driver.find_element(By.NAME,"password")
        password.send_keys("secret_sauce")
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn")))
        menu_button = self.driver.find_element(By.ID, "react-burger-menu-btn")
        menu_button.click()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
        logout_link = self.driver.find_element(By.ID, "logout_sidebar_link")
        logout_link.click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "login-button")))
        print(f"Logout Success Test Result:  Passed")

    def quit_driver(self):
        self.driver.quit()

sauce_demo_test = SauceDemo_Test()
sauce_demo_test.test_empty_login()
sauce_demo_test.test_empty_password_login()
sauce_demo_test.test_locked_out_user_login()
sauce_demo_test.test_success_login()
sauce_demo_test.test_success_logout()
sauce_demo_test.quit_driver()
