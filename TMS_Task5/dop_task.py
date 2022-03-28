#def check_password(func):
#   def wrapper():
#        func()


def create_new_accaunt():
    user_login = input("Введите логин(Учтите, мы очень любим почты yandex:) Другие не признаем): ")
    user_password = input("Введите пароль: ")
    file_database = open('users.txt', 'r+')
    special_symbols = ["!", "?", "_", "*"]
    domain_checking = "@yandex.by"
    if len(user_password) >= 8 and user_login[-10:] == domain_checking:
        for letter in user_password:
            if letter in special_symbols:
                file_database.write(f"{user_login}: {user_password}")
                print("Вы зарегистрированы")
    else:
        print("Проверьте вводимые данные! пароль не меньше 8, почту и наличие спец символов")
    file_database.close()



def log_in_into_accaunt():
    user_login = input("Введите логин: ")
    user_password = input("Введите пароль: ")
    file_database = open('users.txt', 'r')
    combination = f"{user_login}: {user_password}"
    if combination in file_database:
        print('Вы вошли в систему!')
    else:
        print("Данных нет в системе")
    file_database.close()


user_choice = input("Войти / Регистрация: ")
if user_choice == "Войти":
    log_in_into_accaunt()
    pass
elif user_choice == "Регистрация":
    create_new_accaunt()
    pass
else:
    print("Проверьте Ваш запрос.")


