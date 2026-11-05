from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data import WAIT_TIMEOUT, AdData, Messages
from helpers import generate_ad_title
from locators import AuthModalLocators, CreateAdLocators, HeaderLocators, ProfileLocators


class TestCreateAd:

    def test_create_ad_unauthorized_user_shows_auth_modal(self, driver):
        wait = WebDriverWait(driver, WAIT_TIMEOUT)
        wait.until(EC.element_to_be_clickable(HeaderLocators.POST_AD_BUTTON)).click()

        modal_title = wait.until(EC.visibility_of_element_located(AuthModalLocators.MODAL_TITLE)).text

        assert modal_title == Messages.AUTH_REQUIRED_TITLE

    def test_create_ad_authorized_user_ad_shown_in_profile(self, logged_in_new_user_driver):
        wait = WebDriverWait(logged_in_new_user_driver, WAIT_TIMEOUT)
        ad_title = generate_ad_title()
        logged_in_new_user_driver.find_element(*HeaderLocators.POST_AD_BUTTON).click()

        wait.until(EC.visibility_of_element_located(CreateAdLocators.TITLE_INPUT)).send_keys(ad_title)
        logged_in_new_user_driver.find_element(*CreateAdLocators.DESCRIPTION_INPUT).send_keys(AdData.DESCRIPTION)
        logged_in_new_user_driver.find_element(*CreateAdLocators.PRICE_INPUT).send_keys(AdData.PRICE)
        logged_in_new_user_driver.find_element(*CreateAdLocators.CATEGORY_DROPDOWN).click()
        wait.until(EC.element_to_be_clickable(CreateAdLocators.CATEGORY_BOOKS_OPTION)).click()
        logged_in_new_user_driver.find_element(*CreateAdLocators.CITY_DROPDOWN).click()
        wait.until(EC.element_to_be_clickable(CreateAdLocators.CITY_KAZAN_OPTION)).click()
        logged_in_new_user_driver.find_element(*CreateAdLocators.CONDITION_USED_RADIO).click()
        logged_in_new_user_driver.find_element(*CreateAdLocators.PUBLISH_BUTTON).click()

        wait.until(EC.invisibility_of_element_located(CreateAdLocators.PUBLISH_BUTTON))
        logged_in_new_user_driver.find_element(*HeaderLocators.USER_AVATAR).click()
        first_my_ad_title = wait.until(EC.visibility_of_element_located(ProfileLocators.FIRST_MY_AD_TITLE)).text

        assert first_my_ad_title == ad_title
