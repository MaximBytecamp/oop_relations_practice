class Stats:
    def __init__(self, strength: int, intelligence: int, agility: int):
        self.strength = strength
        self.intelligence = intelligence
        self.agility = agility


class Health:
    def __init__(self, max_hp: int):
        self.max_hp = max_hp
        self.current_hp = max_hp

    def take_damage(self, amount: int):
        self.current_hp -= amount
        if self.current_hp < 0:
            self.current_hp = 0


class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item: str):
        self.items.append(item)


class Character:
    def __init__(self, name: str, strength: int, intelligence: int, agility: int, max_hp: int):
        self.name = name
        self.stats = Stats(strength, intelligence, agility)  # композиция
        self.health = Health(max_hp)                         # композиция
        self.inventory = Inventory()                         # композиция

    def attack(self):
        raise NotImplementedError("Метод нужно переопределить")

    def print_info(self):
        print(f"Имя: {self.name}")
        print(f"Здоровье: {self.health.current_hp}/{self.health.max_hp}")
        print(f"Сила: {self.stats.strength}")
        print(f"Интеллект: {self.stats.intelligence}")
        print(f"Ловкость: {self.stats.agility}")
        print(f"Инвентарь: {', '.join(self.inventory.items)}")

class Warrior(Character):
    def attack(self, target):
        hp_loss = self.stats.strength * 2
        target.health.take_damage(hp_loss)
        return hp_loss

    


class Mage(Character):
    def attack(self, target):
        hp_loss = self.stats.intelligence * 3
        target.health.take_damage(hp_loss)
        return hp_loss


warrior = Warrior("Рагнар", strength=10, intelligence=2, agility=5, max_hp=120)
mage = Mage("Элира", strength=2, intelligence=12, agility=4, max_hp=80)

warrior.inventory.add_item("Меч")
mage.inventory.add_item("Посох")
warrior.inventory.add_item("Щит")
warrior.inventory.add_item("Броня")

print(warrior.attack(mage))
print(mage.attack(warrior))

warrior.print_info()
mage.print_info()