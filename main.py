# Создание абстрактного класса оружия
from abc import ABC, abstractmethod


class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass
# Реализация конкретных типов оружия


class Sword(Weapon):
    def attack(self):
        return "Боец выбирает меч.\nБоец бьет монстра мечом."


class Bow(Weapon):
    def attack(self):
        return "Боец выбирает лук.\nБоец стреляет  из лука в монстра."

class Spear(Weapon):
    def attack(self):
        return "Боец выбирает копье .\nБоец метает копье в монстра."


class Stick(Weapon):
    def attack(self):
        return "Боец выбирает палку.\nБоец  бьет толстокожего монстра палкой."


# Модификация класса Fighter **
class Fighter:
    def changeWeapon(self, weapon: Weapon):
        self.weapon = weapon

    def fight(self):
        if self.weapon:
            return self.weapon.attack()
        else:
            return "Боец не выбрал оружие!"

# Реализация механизма боя

class Monster:
    def defeat(self):
        return 'О какой ужас! Монстр погибает от рук бойца.'
    def dancing(self):
        return 'Монстр танцует от радости.'



# Теперь, реализуем простой сценарий боя:
# Создаем бойца и монстра

fighter = Fighter()
monster = Monster()

# Выбираем оружие и атакуем монстра
fighter.changeWeapon(Sword())
print(fighter.fight())
print(monster.defeat())

# Меняем оружие бойца и снова атакуем монстра
fighter.changeWeapon(Bow())
print(fighter.fight())

# Предполагаем, что это другой монстр
monster = Monster()
print(monster.defeat())

fighter.changeWeapon(Spear())
print(fighter.fight())
monster = Monster()
print(monster.defeat())

fighter.changeWeapon(Stick())
print(fighter.fight())
monster = Monster()
print(monster.dancing())