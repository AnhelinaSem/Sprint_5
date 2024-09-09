from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from src.config import Config
from src.locators import Mestolocators
from src.helper import get_sign_up_data
from selenium.webdriver.common.by import By

class TestRegistration:

    def test_registration(self, driver):
        driver.get(f'{Config.URL}/register')
        email_data, password_data = get_sign_up_data()
        driver.find_element(*Mestolocators.EMAIL_FIELD).send_keys(email_data)
        driver.find_element(*Mestolocators.PASSWORD_FIELD).send_keys(password_data)
        driver.find_element(By.NAME, "name").send_keys("Anhelina01")

# Добавь явное ожидание загрузки страницы
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_App__aOmNj")))
# Отправка формы
        driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()

        WebDriverWait(driver, 15).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/login"))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

    def test_incorrect_password_reg(self, driver):
        driver.get(f'{Config.URL}/register')
        email_data, password_data = get_sign_up_data()
        driver.find_element(*Mestolocators.EMAIL_FIELD).send_keys(email_data)
        driver.find_element(*Mestolocators.PASSWORD_FIELD).send_keys('1')
        driver.find_element(By.NAME, "name").send_keys("Anhelina01")

        # Проверка сообщения об ошибке
        error_message = WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//fieldset[3]/div/p[contains(text(), 'Некорректный пароль')]"))
        )
        assert error_message.is_displayed()
