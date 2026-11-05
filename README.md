
## Структура проекта

```text
Sprint_5/
├── conftest.py          # фикстуры: драйвер Chrome, явное ожидание, вход под существующим и новым пользователем
├── data.py              # URL, данные заранее созданного пользователя, тестовые данные и тексты
├── helpers.py           # генераторы email, пароля и названия объявления
├── locators.py          # локаторы элементов, сгруппированные по страницам/блокам
├── requirements.txt
└── tests/
    ├── test_registration.py  # TestRegistration — регистрация пользователя
    ├── test_login.py         # TestLogin — вход пользователя
    ├── test_logout.py        # TestLogout — выход пользователя
    └── test_create_ad.py     # TestCreateAd — создание объявления
```

## Тестовые сценарии

| Модуль | Тест | Что проверяет |
| --- | --- | --- |
| test_registration.py | `test_registration_new_user_shows_avatar_and_name` | после регистрации в шапке отображаются аватар и имя User |
| | `test_registration_email_not_matching_mask_shows_error` | email не по маске → поля Email, «Пароль», «Повторите пароль» красные, под Email «Ошибка» |
| | `test_registration_existing_user_shows_error` | регистрация существующего пользователя → та же ошибка |
| test_login.py | `test_login_existing_user_shows_avatar_and_name` | после входа в шапке отображаются аватар и имя User |
| test_logout.py | `test_logout_shows_login_button_instead_of_user` | после выхода вместо аватара и имени снова кнопка «Вход и регистрация» |
| test_create_ad.py | `test_create_ad_unauthorized_user_shows_auth_modal` | неавторизованному пользователю показывается окно «Чтобы разместить объявление, авторизуйтесь» |
| | `test_create_ad_authorized_user_ad_shown_in_profile` | созданное объявление появляется в блоке «Мои объявления» профиля |

# Sprint_5
