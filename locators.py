from selenium.webdriver.common.by import By


class HeaderLocators:
    # Кнопка «Вход и регистрация» в шапке
    LOGIN_AND_REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Вход и регистрация']")
    # Кнопка «Разместить объявление» в шапке
    POST_AD_BUTTON = (By.XPATH, "//button[text()='Разместить объявление']")
    # Аватар авторизованного пользователя
    USER_AVATAR = (By.CSS_SELECTOR, "button.circleSmall")
    # Имя авторизованного пользователя
    USER_NAME = (By.CSS_SELECTOR, "h3.profileText.name")
    # Кнопка «Выйти»
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")


class AuthModalLocators:
    # Заголовок модального окна
    MODAL_TITLE = (By.CSS_SELECTOR, "form[class*='popUp_shell'] h1")
    # Поле Email
    EMAIL_INPUT = (By.NAME, "email")
    # Поле «Пароль»
    PASSWORD_INPUT = (By.NAME, "password")
    # Поле «Повторите пароль»
    REPEAT_PASSWORD_INPUT = (By.NAME, "submitPassword")
    # Кнопка «Нет аккаунта»
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Нет аккаунта']")
    # Кнопка «Войти»
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    # Кнопка «Создать аккаунт»
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Создать аккаунт']")
    # Поле Email, выделенное красным
    EMAIL_INPUT_WITH_ERROR = (By.XPATH, "//input[@name='email']/parent::div[contains(@class, 'input_inputError')]")
    # Поле «Пароль», выделенное красным
    PASSWORD_INPUT_WITH_ERROR = (By.XPATH, "//input[@name='password']/parent::div[contains(@class, 'input_inputError')]")
    # Поле «Повторите пароль», выделенное красным
    REPEAT_PASSWORD_INPUT_WITH_ERROR = (
        By.XPATH, "//input[@name='submitPassword']/parent::div[contains(@class, 'input_inputError')]"
    )
    # Сообщение об ошибке под полем Email
    EMAIL_ERROR_MESSAGE = (By.XPATH, "//input[@name='email']/ancestor::div[2]/following-sibling::span")


class CreateAdLocators:
    # Поле «Название»
    TITLE_INPUT = (By.CSS_SELECTOR, "form[class*='createListing'] input[name='name']")
    # Поле «Описание товара»
    DESCRIPTION_INPUT = (By.CSS_SELECTOR, "form[class*='createListing'] textarea[name='description']")
    # Поле «Стоимость»
    PRICE_INPUT = (By.CSS_SELECTOR, "form[class*='createListing'] input[name='price']")
    # Кнопка раскрытия Dropdown «Категория»
    CATEGORY_DROPDOWN = (By.XPATH, "//form[contains(@class, 'createListing')]//input[@name='category']/following-sibling::button")
    # Вариант «Книги» в Dropdown «Категория»
    CATEGORY_BOOKS_OPTION = (
        By.XPATH,
        "//form[contains(@class, 'createListing')]//input[@name='category']/../following-sibling::div//span[text()='Книги']"
    )
    # Кнопка раскрытия Dropdown «Город»
    CITY_DROPDOWN = (By.XPATH, "//form[contains(@class, 'createListing')]//input[@name='city']/following-sibling::button")
    # Вариант «Казань» в Dropdown «Город»
    CITY_KAZAN_OPTION = (
        By.XPATH,
        "//form[contains(@class, 'createListing')]//input[@name='city']/../following-sibling::div//span[text()='Казань']"
    )
    # RadioButton «Б/У» в блоке «Состояние товара»
    CONDITION_USED_RADIO = (By.XPATH, "//input[@name='condition' and @value='Б/У']/following-sibling::div")
    # Кнопка «Опубликовать»
    PUBLISH_BUTTON = (By.XPATH, "//button[text()='Опубликовать']")


class ProfileLocators:
    # Название первого объявления в блоке «Мои объявления»
    FIRST_MY_AD_TITLE = (
        By.XPATH, "(//h1[text()='Мои объявления']/following-sibling::*//div[@class='about']/h2)[1]"
    )
