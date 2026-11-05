from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data import DEFAULT_USER_NAME, WAIT_TIMEOUT, ExistingUser, Messages
from helpers import generate_email, generate_invalid_email, generate_password
from locators import AuthModalLocators, HeaderLocators


class TestRegistration:

    def test_registration_new_user_shows_avatar_and_name(self, driver):
        wait = WebDriverWait(driver, WAIT_TIMEOUT)
        password = generate_password()
        wait.until(EC.element_to_be_clickable(HeaderLocators.LOGIN_AND_REGISTRATION_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(AuthModalLocators.NO_ACCOUNT_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(AuthModalLocators.CREATE_ACCOUNT_BUTTON))
        driver.find_element(*AuthModalLocators.EMAIL_INPUT).send_keys(generate_email())
        driver.find_element(*AuthModalLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*AuthModalLocators.REPEAT_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*AuthModalLocators.CREATE_ACCOUNT_BUTTON).click()

        user_name = wait.until(EC.visibility_of_element_located(HeaderLocators.USER_NAME)).text
        avatar_displayed = driver.find_element(*HeaderLocators.USER_AVATAR).is_displayed()
        auth_modals_count = len(driver.find_elements(*AuthModalLocators.MODAL_TITLE))

        assert (auth_modals_count, avatar_displayed, user_name) == (0, True, DEFAULT_USER_NAME)

    def test_registration_email_not_matching_mask_shows_error(self, driver):
        wait = WebDriverWait(driver, WAIT_TIMEOUT)
        wait.until(EC.element_to_be_clickable(HeaderLocators.LOGIN_AND_REGISTRATION_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(AuthModalLocators.NO_ACCOUNT_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(AuthModalLocators.CREATE_ACCOUNT_BUTTON))
        driver.find_element(*AuthModalLocators.EMAIL_INPUT).send_keys(generate_invalid_email())
        driver.find_element(*AuthModalLocators.CREATE_ACCOUNT_BUTTON).click()

        error_message = wait.until(EC.visibility_of_element_located(AuthModalLocators.EMAIL_ERROR_MESSAGE)).text
        highlighted_fields = [
            driver.find_element(*AuthModalLocators.EMAIL_INPUT_WITH_ERROR).is_displayed(),
            driver.find_element(*AuthModalLocators.PASSWORD_INPUT_WITH_ERROR).is_displayed(),
            driver.find_element(*AuthModalLocators.REPEAT_PASSWORD_INPUT_WITH_ERROR).is_displayed(),
        ]

        assert (highlighted_fields, error_message) == ([True, True, True], Messages.EMAIL_ERROR)

    def test_registration_existing_user_shows_error(self, driver):
        wait = WebDriverWait(driver, WAIT_TIMEOUT)
        wait.until(EC.element_to_be_clickable(HeaderLocators.LOGIN_AND_REGISTRATION_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(AuthModalLocators.NO_ACCOUNT_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(AuthModalLocators.CREATE_ACCOUNT_BUTTON))
        driver.find_element(*AuthModalLocators.EMAIL_INPUT).send_keys(ExistingUser.EMAIL)
        driver.find_element(*AuthModalLocators.PASSWORD_INPUT).send_keys(ExistingUser.PASSWORD)
        driver.find_element(*AuthModalLocators.REPEAT_PASSWORD_INPUT).send_keys(ExistingUser.PASSWORD)
        driver.find_element(*AuthModalLocators.CREATE_ACCOUNT_BUTTON).click()

        error_message = wait.until(EC.visibility_of_element_located(AuthModalLocators.EMAIL_ERROR_MESSAGE)).text
        highlighted_fields = [
            driver.find_element(*AuthModalLocators.EMAIL_INPUT_WITH_ERROR).is_displayed(),
            driver.find_element(*AuthModalLocators.PASSWORD_INPUT_WITH_ERROR).is_displayed(),
            driver.find_element(*AuthModalLocators.REPEAT_PASSWORD_INPUT_WITH_ERROR).is_displayed(),
        ]

        assert (highlighted_fields, error_message) == ([True, True, True], Messages.EMAIL_ERROR)
