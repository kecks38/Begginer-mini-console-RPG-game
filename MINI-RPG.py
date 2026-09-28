import random

class Character:
    def __init__(self, name, hp, max_hp, attack_min, attack_max):
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
        self.attack_min = attack_min
        self.attack_max = attack_max

    def attack_enemy(self, other):
        damage = random.randint(self.attack_min , self.attack_max)
        if random.random() < 0.1:
            damage = damage * 2
            print(f"{self.name} наносит Крит!")     
        other.hp -= damage

    def heal(self):
        
        restore_hp = random.randint(5, 20)
        self.hp += restore_hp
        self.hp = min(self.hp, self.max_hp)
    
    def is_alive(self):
        return self.hp > 0 

hero = Character("Герой", 100, 100, 5, 15)

enemy = Character("Гоблин", 40, 40, 5, 15)

print(f"Произошла стычка. {enemy.name}!")

surrendered = False
heal_potion = 3 

while hero.is_alive() and enemy.is_alive() :
    print(f"{hero.name}: {hero.hp} ОЗ \n{enemy.name}: {enemy.hp} ОЗ\n")
    print("Действия: \n 1 - Удар \n 2 Зелье ОЗ \n 3 Сдаться")
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
        if heal_potion > 0:
            print(f"{hero.name} достает зелье и восстанавливет ОЗ!")
            hero.heal()
            heal_potion -= 1
            print(f"Осталось зелий {heal_potion}")
            if random.random() < 0.8:
                print(f"{enemy.name} возмущён такой наглостью и наносит удар")
                enemy.attack_enemy(hero)
        else:
            print("Ничего не произошло, зелий лечения нет")
            if random.random() < 0.8:
                print(f"{enemy.name} возмущён такой наглостью и наносит удар")
                enemy.attack_enemy(hero)

    elif choice == 3:
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
    
