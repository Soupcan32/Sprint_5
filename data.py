BASE_URL = "https://qa-desk.education-services.ru/"

WAIT_TIMEOUT = 20


class ExistingUser:
    # Заранее созданный в системе пользователь
    EMAIL = "sprint5qauser@example.com"
    PASSWORD = "Sprint5Pass123"


# Имя, которое сайт показывает в шапке любому новому пользователю
DEFAULT_USER_NAME = "User."


class AdData:
    DESCRIPTION = "Книга в хорошем состоянии, все страницы на месте"
    PRICE = "1500"


class Messages:
    AUTH_REQUIRED_TITLE = "Чтобы разместить объявление, авторизуйтесь"
    EMAIL_ERROR = "Ошибка"
