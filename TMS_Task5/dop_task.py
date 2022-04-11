import re

database_file = 'users.txt'


def validate_credentials(func):
    def wrapper(some_login, some_password):
        password_re = r'[A-Za-z0-9@#$%^&+=]{8,}'
        login_re = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        password_pattern = re.compile(password_re)
        mat = re.search(password_pattern, some_password)
        if not re.fullmatch(login_re, some_login):
            raise Exception("Проверьте логин")
        if not mat:
            raise Exception("Проверьте пароль")
        func(some_login, some_password)
    return wrapper


@validate_credentials
def create_new_account(login: str, password: str):
    with open(database_file, 'a') as file_database:
        credentials = f"{login}:{password}\n"
        file_database.writelines([credentials])
        print("Вы зарегистрированы")


def log_in_into_account(login: str, password: str):
    with open('users.txt', 'r') as file_database:
        credentials = f"{login}:{password}"
        if credentials in file_database.read():
            print('Вы вошли в систему!')
        else:
            print("Данных нет в системе")


def ask_credentials() -> tuple:
    login = input("Введите Ваш логин: ")
    password = input("Введите Ваш пароль: ")
    return (login, password)


def main():
    try:
        while True:
            user_choice = input("Меню: \nВойти/Регистрация/Выход: ")
            if user_choice == "Войти":
                login, password = ask_credentials()
                log_in_into_account(login, password)

            elif user_choice == "Регистрация":
                login, password = ask_credentials()

                create_new_account(login, password)
            elif user_choice == "Выход":
                return

    except Exception:
        print("Проверьте вводимые данные в пароле или логине")


main()

