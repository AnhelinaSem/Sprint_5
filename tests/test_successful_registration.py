from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/register")

#  поле "Имя"
driver.find_element(By.NAME, "name").send_keys("Anhelina01")

#  поле "Email"
driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input[@name='name']").send_keys("Anhelina01@ya.ru")

#  поля "Пароль"
driver.find_element(By.XPATH, ".//fieldset[3]/div/div/input[@name='Пароль']").send_keys("password1123")

# Добавь явное ожидание загрузки страницы
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "App_App__aOmNj")))

# Отправка формы
driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()

WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"


driver.quit()
