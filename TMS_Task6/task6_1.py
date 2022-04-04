# Написать программу, которая получит имя и возраст пользователя, записывает данные в JSON, CSV
import json
import csv

# json file:
user_name = input("Введите свое имя: ")
user_age = input("Введите свой возраст: ")
user_information = {user_name: user_age}
json_string = json.dumps(user_information)
with open("users_ages_1.json", "a") as database:
    database.write(json_string)

# csv file:

with open("users_ages.csv", "a", newline="") as database_users:
    fieldnames = ["user", "age"]
    writer = csv.DictWriter(database_users, fieldnames=fieldnames)
    writer.writeheader()
    name = input("Введите свое имя: ")
    age = input("Введите свой возраст: ")
    writer.writerow({"user": name, "age": age})
