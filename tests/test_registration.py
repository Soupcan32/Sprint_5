from selenium.webdriver.support import expected_conditions as EC

from data import DEFAULT_USER_NAME, ExistingUser, Messages
from helpers import generate_email, generate_invalid_email, generate_password
from locators import AuthModalLocators, HeaderLocators


class TestRegistration:

    def open_registration_form(self, wait):
        wait.until(EC.element_to_be_clickable(HeaderLocators.LOGIN_AND_REGISTRATION_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(AuthModalLocators.NO_ACCOUNT_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(AuthModalLocators.CREATE_ACCOUNT_BUTTON))

    def fill_registration_form(self, driver, email, password):
        driver.find_element(*AuthModalLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*AuthModalLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*AuthModalLocators.REPEAT_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*AuthModalLocators.CREATE_ACCOUNT_BUTTON).click()

    def get_highlighted_fields_and_error(self, driver, wait):
        error_message = wait.until(EC.visibility_of_element_located(AuthModalLocators.EMAIL_ERROR_MESSAGE)).text
        highlighted_fields = [
            driver.find_element(*AuthModalLocators.EMAIL_INPUT_WITH_ERROR).is_displayed(),
            driver.find_element(*AuthModalLocators.PASSWORD_INPUT_WITH_ERROR).is_displayed(),
            driver.find_element(*AuthModalLocators.REPEAT_PASSWORD_INPUT_WITH_ERROR).is_displayed(),
        ]
        return highlighted_fields, error_message

    def test_registration_new_user_shows_avatar_and_name(self, driver, wait):
        self.open_registration_form(wait)
        self.fill_registration_form(driver, generate_email(), generate_password())

        user_name = wait.until(EC.visibility_of_element_located(HeaderLocators.USER_NAME)).text
        avatar_displayed = driver.find_element(*HeaderLocators.USER_AVATAR).is_displayed()
        auth_modals_count = len(driver.find_elements(*AuthModalLocators.MODAL_TITLE))

        assert (auth_modals_count, avatar_displayed, user_name) == (0, True, DEFAULT_USER_NAME)

    def test_registration_email_not_matching_mask_shows_error(self, driver, wait):
        self.open_registration_form(wait)
        driver.find_element(*AuthModalLocators.EMAIL_INPUT).send_keys(generate_invalid_email())
        driver.find_element(*AuthModalLocators.CREATE_ACCOUNT_BUTTON).click()

        highlighted_fields, error_message = self.get_highlighted_fields_and_error(driver, wait)

        assert (highlighted_fields, error_message) == ([True, True, True], Messages.EMAIL_ERROR)

    def test_registration_existing_user_shows_error(self, driver, wait):
        self.open_registration_form(wait)
        self.fill_registration_form(driver, ExistingUser.EMAIL, ExistingUser.PASSWORD)

        highlighted_fields, error_message = self.get_highlighted_fields_and_error(driver, wait)

        assert (highlighted_fields, error_message) == ([True, True, True], Messages.EMAIL_ERROR)
