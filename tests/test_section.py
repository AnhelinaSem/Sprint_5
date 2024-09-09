from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.config import Config
from src.locators import Mestolocators

class TestSection:

    def test_section_soys(self, driver):
        driver.get(f'{Config.URL}')

        # Проверка перехода к разделу "Соусы"
        driver.find_element(*Mestolocators.SOYS_SECTION).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((Mestolocators.SOYS_SECTION)))
        assert driver.find_element(*Mestolocators.SOYS_SECTION).is_displayed()

    def test_section_bylki(self, driver):
        driver.get(f'{Config.URL}')
        # Проверка раздел "Булки" отображается

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((Mestolocators.BYLKI_SECTION)))
        assert driver.find_element(*Mestolocators.BYLKI_SECTION).is_displayed()

        # Переход к разделу "Соусы"
        driver.find_element(*Mestolocators.SOYS_SECTION).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((Mestolocators.SOYS_SECTION)))

        # Проверка перехода к разделу "Булки"
        element = driver.find_element(*Mestolocators.BYLKI_SECTION)
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((Mestolocators.BYLKI_SECTION)))
        assert driver.find_element(*Mestolocators.BYLKI_SECTION).is_displayed()

    def test_section_nachinka(self, driver):
        driver.get(f'{Config.URL}')

        # Проверка перехода к разделу "Начинки"
        driver.find_element(*Mestolocators.NACHINKA_SECTION).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((Mestolocators.NACHINKA_SECTION)))
        assert driver.find_element(*Mestolocators.NACHINKA_SECTION).is_displayed()
