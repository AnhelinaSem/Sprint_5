from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site")

# Проверка перехода к разделу "Начинки"
driver.find_element(By.XPATH, "//span[text()='Начинки']").click()
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Начинки']")))
assert driver.find_element(By.XPATH, "//h2[text()='Начинки']").is_displayed()

driver.quit()
