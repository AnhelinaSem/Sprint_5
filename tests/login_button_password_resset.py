from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

# Нажать кнопку
driver.find_element(By.XPATH, ".//a[text()='Войти']").click()

# Ввести email и пароль
driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input[@name='name']").send_keys("Anhelina01@ya.ru")
driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input[@name='Пароль']").send_keys("password1123")
# Нажать кнопку "Войти"
driver.find_element(By.XPATH, "//button[text()='Войти']").click()
# Добавь явное ожидание загрузки страницы
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "App_App__aOmNj")))



driver.quit()
