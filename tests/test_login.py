from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data import DEFAULT_USER_NAME, WAIT_TIMEOUT, ExistingUser
from locators import AuthModalLocators, HeaderLocators


class TestLogin:

    def test_login_existing_user_shows_avatar_and_name(self, driver):
        wait = WebDriverWait(driver, WAIT_TIMEOUT)
        wait.until(EC.element_to_be_clickable(HeaderLocators.LOGIN_AND_REGISTRATION_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(AuthModalLocators.EMAIL_INPUT)).send_keys(ExistingUser.EMAIL)
        driver.find_element(*AuthModalLocators.PASSWORD_INPUT).send_keys(ExistingUser.PASSWORD)
        driver.find_element(*AuthModalLocators.LOGIN_BUTTON).click()

        user_name = wait.until(EC.visibility_of_element_located(HeaderLocators.USER_NAME)).text
        avatar_displayed = driver.find_element(*HeaderLocators.USER_AVATAR).is_displayed()
        auth_modals_count = len(driver.find_elements(*AuthModalLocators.MODAL_TITLE))

        assert (auth_modals_count, avatar_displayed, user_name) == (0, True, DEFAULT_USER_NAME)
