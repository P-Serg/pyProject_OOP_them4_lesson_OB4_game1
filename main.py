### Шаг 1: Создание абстрактного класса для оружия

from abc import ABC, abstractmethod

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

### Пример использования

# Создание бойца и монстра
fighter = Fighter("Боец")
monster = Monster("Монстр", 100)

# Создание оружия
sword = Sword()
bow = Bow()

# Боец выбирает меч и атакует
fighter.changeWeapon(sword)
print(fighter.attack())
monster.take_damage(50)

# Боец выбирает лук и атакует
fighter.changeWeapon(bow)
print(fighter.attack())
monster.take_damage(50)
