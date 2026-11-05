from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data import WAIT_TIMEOUT
from locators import HeaderLocators


class TestLogout:

    def test_logout_shows_login_button_instead_of_user(self, logged_in_driver):
        wait = WebDriverWait(logged_in_driver, WAIT_TIMEOUT)
        logged_in_driver.find_element(*HeaderLocators.LOGOUT_BUTTON).click()

        login_button_displayed = wait.until(
            EC.visibility_of_element_located(HeaderLocators.LOGIN_AND_REGISTRATION_BUTTON)
        ).is_displayed()
        avatars_count = len(logged_in_driver.find_elements(*HeaderLocators.USER_AVATAR))
        user_names_count = len(logged_in_driver.find_elements(*HeaderLocators.USER_NAME))

        assert (login_button_displayed, avatars_count, user_names_count) == (True, 0, 0)
