from abc import ABC, abstractmethod

### Шаг 1: Создание абстрактного класса для оружия

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

### Шаг 2: Реализация конкретных типов оружия

class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."

### Шаг 3: Модификация класса Fighter

class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def changeWeapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {type(weapon).__name__.lower()}.")

    def attack(self):
        if self.weapon:
            return self.weapon.attack()
        else:
            return "Нет оружия для атаки."

### Шаг 4: Реализация класса Monster

class Monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} побежден!")
        else:
            print(f"{self.name} осталось {self.health} здоровья.")

### Основная игровая логика

def main():
    # Создание бойца и монстра
    fighter = Fighter("Боец")
    monsters = [
        Monster("Монстр 1", 100),
        Monster("Монстр 2", 150)
    ]

    # Создание оружия
    sword = Sword()
    bow = Bow()

    while monsters:
        monster = monsters[0]
        print(f"\nВы столкнулись с {monster.name}, у которого {monster.health} здоровья.")

        while monster.health > 0:
            print("\nВыберите действие:")
            print("1. Выбрать меч")
            print("2. Выбрать лук")
            print("3. Атаковать")

            choice = input("> ")

            if choice == "1":
                fighter.changeWeapon(sword)
            elif choice == "2":
                fighter.changeWeapon(bow)
            elif choice == "3":
                if fighter.weapon:
                    print(fighter.attack())
                    monster.take_damage(50)
                else:
                    print("Сначала выберите оружие!")
            else:
                print("Неверный выбор. Попробуйте снова.")

            monsters.pop(0)
            print(f"Вы победили {monster.name}!")

            print("Все монстры побеждены! Игра окончена.")

            if __name__ == "__main__":
                main()