import random
# Полный вариянт игры с использованием Random

while True:
    reply_list = ['камень', 'ножницы', 'бумага']
    print("ROCK -- PAPER -- SCISSORS | GAME \n")
    user_new_inp = input("Выберай: Камень | Ножницы | Бумага: ")
    ai_rps_random = random.choice(reply_list)
    print(f"Вы выбрали: {user_new_inp} \n AI выбрал: {ai_rps_random}")

    if user_new_inp == ai_rps_random:
        print(f"Оба выбрали {user_new_inp}. Ничья")
    elif user_new_inp == 'камень':
        if ai_rps_random == 'ножницы':
            print("Камень бьет ножницы - ВЫ ПОБЕДИЛИ!")
        else:
            print("Бумага накрывает камень - ВЫ ПРОИГРАЛИ!")
    elif user_new_inp == 'бумага':
        if ai_rps_random == 'камень':
            print("Бумага накрывает камень - ВЫ ПОБЕДИЛИ!")
        else:
            print("Ножницы режут бумагу - ВЫ ПРОИГРАЛИ!")
    elif user_new_inp == 'ножницы':
        if ai_rps_random == 'бамага':
            print("Ножницы режут бумагу - ВЫ ПОБЕДИЛИ!")
        else:
            print("Камень бьет ножницы - ВЫ ПРОИГРАЛИ!")
    play_again = input("Хотите сыграть снова | да / нет: ")
    if play_again.lower() != 'да':
        print('До свидания : ✖◕‿◕✖')
        break
print("by Asylbekov Arstan")




