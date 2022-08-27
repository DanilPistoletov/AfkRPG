import platform
pcname = platform.node()
Name = 0
Years = 0
Sex = 0
print("""
AFKRPG 0.1 [28.8.2022]
Автор: Данил Пистолетов
Сайт: danil-pistoletov.org

Привет, """ + pcname + """, ты попал в игру AFKRPG. Суть игры состоит в том, что персонаж развивается без твоего участия.
Тебе не нужно ничего делать, ты можешь только наблюдать.""")
reaction = input("Имя твоего персонажа - " + pcname + ", оставить его таким? (Да/Нет)")
if reaction == "да" or reaction == "ДА" or reaction == "Да":
    Name = pcname
else:
    Name = input("Какое имя вы хотите дать персонажу?")
reaction = int(input("Имя для " + Name + " было придумано, теперь укажите возраст"))
while Years == 0:
    if reaction < 16:
        reaction = int(input("Персонаж слишком юн для этого жестокого мира, укажите более реальный возраст"))
    elif reaction > 70:
        reaction = int(input("Персонаж слишком стар для этого прогнившего мира, укажите более реальный возраст"))
    elif reaction > 15 and reaction < 71:
        Years = reaction
    else:
        print("Введён неверный возраст")
Years = str(Years)
print("""
Возраст выбран, теперь выберите пол.
М - Мужской
Ж - Женский
""")
reaction = input()
if reaction == "М" or reaction == "м":
    print("Вашего героя зовут " + Name + ", ему " + Years)
if reaction == "Ж" or reaction == "ж":
    print("Вашу героиню зовут " + Name + ", ей " + Years)