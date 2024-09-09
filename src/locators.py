from selenium.webdriver.common.by import By

class Mestolocators:
    EMAIL_FIELD = By.XPATH, "//label[text()='Email']/following-sibling::input"
    PASSWORD_FIELD = By.XPATH, "//input[contains(@type,'password')]"
    NAME_FIELD = By.XPATH, "//label[text()='Имя']/following-sibling::input"
    PERSONAL_ACCOUNT = By.XPATH, "//p[text()='Личный Кабинет']"
    LOGIN_BUTTON = By.XPATH, "//button[text()='Войти']"
    BYLKI_SECTION = By.XPATH, "//h2[text()='Булки']"
    SOYS_SECTION = By.XPATH, "//h2[text()='Соусы']"
    NACHINKA_SECTION = By.XPATH, "//h2[text()='Начинки']"


    EMAIL_HEADER = By.XPATH, "//p[contains(@class, 'user')]"
    LOGOUT_BUTTON = By.XPATH, "//button[contains(@class, 'logout')]"
