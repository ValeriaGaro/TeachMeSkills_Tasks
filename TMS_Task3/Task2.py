# Сделать программу, в которой нужно угадать число

bot_number = 39
user_number = None
while bot_number != user_number:
    user_number = int(input("Попробуй угадать, что я загадал: "))
    if 39 > user_number > 30:
        print("Ты почти у цели, но я пока выигрываю!")
    elif 50 > user_number > 40:
        print("Ты почти у цели, но я пока выигрываю!")
    elif user_number > 100:
        print("Не так сложно, все гораздо проще")
    elif 0 < user_number < 15:
        print("Не так все просто!")
    else:
        print("Ну подумай еще")
print("Угадал!")

