def check_registration(func):
    def wrapper(some_login, some_password):
        special_symbols = ["!", "?", "_", "*"]
        domain_checking = "@yandex.by"
        if len(some_password) >= 8 and some_login[-10:] == domain_checking:
            for letter in some_password:
                if letter in special_symbols:
                    func(some_login, some_password)

        else:
            print("Проверьте вводимые данные! пароль не меньше 8, почту и наличие спец символов")
    return wrapper


@check_registration
def create_new_accaunt(login: str, password: str):
    file_database = open('users.txt', 'r+')
    file_database.write(f"{login}: {password} ")
    print("Вы зарегистрированы")
    file_database.close()


def log_in_into_accaunt():
    file_database = open('users.txt', 'r')
    login = input("Введите Ваш логин: ")
    password = input("Введите Ваш пароль: ")
    combination = f"{login}: {password} "
    if combination in file_database:
        print('Вы вошли в систему!')
    else:
        print("Данных нет в системе")
    file_database.close()


user_choice = input("Войти / Регистрация: ")
if user_choice == "Войти":
    log_in_into_accaunt()
elif user_choice == "Регистрация":
    user_login = input("Введите Ваш логин: ")
    user_password = input("Введите Ваш пароль: ")
    create_new_accaunt(user_login, user_password)
else:
    print("Проверьте Ваш запрос.")


