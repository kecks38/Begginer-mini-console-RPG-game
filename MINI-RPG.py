import random

class Character:
    def __init__(self, name, hp, attack_min, attack_max):
        self.name = name
        self.hp = hp
        self.attack_min = attack_min
        self.attack_max = attack_max

    def attack_enemy(self, other):
        damage = random.randint(self.attack_min , self.attack_max)
         
        other.hp -= damage

    def is_alive(self):
        return self.hp > 0

hero = Character("Герой", 100, 5, 15)

enemy = Character("Гоблин", 40, 5, 15)

print(f"Произошла стычка. {enemy.name}!")

surrendered = False

while hero.is_alive() and enemy.is_alive() :
    print(f"{hero.name}: {hero.hp} ОЗ \n{enemy.name}: {enemy.hp} ОЗ\n")
    print("Действия: \n 1 - Удар \n 2 Сдаться")
    try:
        choice = int(input())
    except(ValueError):
        print("Выберите правильное действие")
        continue
    if choice == 1:
        print("Герой атакует...")
        hero.attack_enemy(enemy)
        if not enemy.is_alive():
            break
        print("Гоблин атакует в ответ...")
        enemy.attack_enemy(hero)

    elif choice == 2:
        surrendered = True
        break
    else: 
        print("Противники молча стоят друг напротив друга.. \n Перекати-поле ... *вшш.. вш..*")   

if surrendered :
        print("Герой.. сдался..\n Вы проиграли.")
else:

    if hero.is_alive():
    
    
        print()
        print("Герой размашистым ударом валит на землю своего противника! \nГерой победил!")
        print(f"Остаток ОЗ: \n{hero.name}: {hero.hp}")
    else:
        print("Вы проиграли.. \nВраг победил")
    
