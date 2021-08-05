init python:
    class Entity:
        def __init__(self, entity_type, name, icon, health, mana, money, style, magic, wisdom):
            self.entity_type = entity_type
            self.name = name
            self.icon = icon
            self.health = health
            self.mana = mana
            self.money = money
            self.style = style
            self.wisdom = wisdom
            self.god_mode = False
            self.cursed_mode = False

        def is_active(self):
            if self.god_mode:
                return True

            return self.health > 0

        def has_enough_mana(self, amount):
            if self.god_mode:
                return True
            elif self.cursed_mode:
                return False

            # do you have enough mana to afford to lose the amount specified?
            return self.mana >= self.mana - amount

        def has_enough_money(self, amount):
            # do you have enough money to afford to lose the amount specified?
            return self.money >= self.money - amount

        def has_enough_style(self, amount):
            if self.god_mode:
                return True
            elif self.cursed_mode:
                return False

            # do you have the minimum amount of style required?
            return self.style >= amount

        def has_enough_magic(self, amount):
            if self.god_mode:
                return True
            elif self.cursed_mode:
                return False

            # do you have the minimum amount of magic required?
            return self.magic >= amount

        def has_enough_wisdom(self, amount):
            if self.god_mode:
                return True
            elif self.cursed_mode:
                return False

            # do you have the minimum amount of wisdom required?
            return self.widsom >= amount

        def update_health(self, amount):
            if self.god_mode:
                return

            self.health += amount

            # can't have negative health
            if self.health < 0:
                self.health = 0
        
        def update_mana(self, amount):
            if self.god_mode:
                return

            self.mana += amount

            if self.mana < 0:
                self.mana = 0

        def update_money(self, amount):
            if self.god_mode:
                return

            self.money += amount

            if self.money < 0:
                self.money = 0
