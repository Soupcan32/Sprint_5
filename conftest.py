import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data import BASE_URL, WAIT_TIMEOUT, ExistingUser
from helpers import generate_email, generate_password
from locators import AuthModalLocators, HeaderLocators


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    # На узком окне сайт переключается на мобильную вёрстку и прячет имя пользователя
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    driver.get(BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def logged_in_driver(driver):
    wait = WebDriverWait(driver, WAIT_TIMEOUT)
    wait.until(EC.element_to_be_clickable(HeaderLocators.LOGIN_AND_REGISTRATION_BUTTON)).click()
    wait.until(EC.visibility_of_element_located(AuthModalLocators.EMAIL_INPUT)).send_keys(ExistingUser.EMAIL)
    driver.find_element(*AuthModalLocators.PASSWORD_INPUT).send_keys(ExistingUser.PASSWORD)
    driver.find_element(*AuthModalLocators.LOGIN_BUTTON).click()
    wait.until(EC.visibility_of_element_located(HeaderLocators.USER_NAME))
    return driver


@pytest.fixture
def logged_in_new_user_driver(driver):
    # Свежий пользователь без объявлений: профиль показывает старые объявления первыми и удалить их нельзя
    wait = WebDriverWait(driver, WAIT_TIMEOUT)
    email = generate_email()
    password = generate_password()
    wait.until(EC.element_to_be_clickable(HeaderLocators.LOGIN_AND_REGISTRATION_BUTTON)).click()
    wait.until(EC.element_to_be_clickable(AuthModalLocators.NO_ACCOUNT_BUTTON)).click()
    wait.until(EC.visibility_of_element_located(AuthModalLocators.REPEAT_PASSWORD_INPUT))
    driver.find_element(*AuthModalLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*AuthModalLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*AuthModalLocators.REPEAT_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*AuthModalLocators.CREATE_ACCOUNT_BUTTON).click()
    wait.until(EC.element_to_be_clickable(HeaderLocators.LOGOUT_BUTTON)).click()
    wait.until(EC.element_to_be_clickable(HeaderLocators.LOGIN_AND_REGISTRATION_BUTTON)).click()
    wait.until(EC.visibility_of_element_located(AuthModalLocators.EMAIL_INPUT)).send_keys(email)
    driver.find_element(*AuthModalLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*AuthModalLocators.LOGIN_BUTTON).click()
    wait.until(EC.visibility_of_element_located(HeaderLocators.USER_NAME))
    return driver
