init python:
    class Entity:
        def __init__(self, entity_type, name, icon, health, mana, money, style, magic, wisdom, strength, weakness, name_color="#999999", entity_font=""):
            self.entity_type = entity_type
            self.name = name
            self.icon = icon
            self.health = health
            self.max_health = health
            self.mana = mana
            self.max_mana = mana
            self.money = money
            self.style = style
            self.magic = magic
            self.wisdom = wisdom
            self.god_mode = False
            self.cursed_mode = False
            self.strength = strength
            self.weakness = weakness
            self.name_color = name_color
            self.entity_font = gui.preference("font", preferences.t3_default_font)

            self.update_character_name(name, entity_font)

        def modified_style(self):
            if self.strength == AttributeType.Style:
                return self.style + 1

            if self.weakness == AttributeType.Style:
                return self.style - 1

            return self.style

        def modified_magic(self):
            if self.strength == AttributeType.Magic:
                return self.magic + 1

            if self.weakness == AttributeType.Magic:
                return self.magic - 1

            return self.magic
            
        def modified_wisdom(self):
            if self.strength == AttributeType.Wisdom:
                return self.wisdom + 1

            if self.weakness == AttributeType.Wisdom:
                return self.wisdom - 1

            return self.wisdom

        def is_active(self):
            if self.god_mode:
                return True

            return self.health > 0

        def has_enough_health(self, amount):
            if self.god_mode:
                return True
            elif self.cursed_mode:
                return False

            # do you have enough health to afford to lose the amount specified?
            return self.health >= self.health - amount

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
            return self.modified_style() >= amount

        def has_enough_magic(self, amount):
            if self.god_mode:
                return True
            elif self.cursed_mode:
                return False

            # do you have the minimum amount of magic required?
            return self.modified_magic() >= amount

        def has_enough_wisdom(self, amount):
            if self.god_mode:
                return True
            elif self.cursed_mode:
                return False

            # do you have the minimum amount of wisdom required?
            return self.modified_wisdom() >= amount

        def update_health(self, amount):
            if self.god_mode:
                return

            if (self.health + amount) > self.max_health:
                self.health = self.max_health
            else:
                self.health += amount

            # can't have negative health
            if self.health < 0:
                self.health = 0
        
        def update_mana(self, amount):
            if self.god_mode:
                return

            if (self.mana + amount) > self.max_mana:
                self.mana = self.max_mana
            else:
                self.mana += amount

            # can't have negative mana
            if self.mana < 0:
                self.mana = 0

        def update_money(self, amount):
            if self.god_mode:
                return

            self.money += amount

            if self.money < 0:
                self.money = 0

        def update_character_name(self, name, entity_font = None):
            self.name = name

            if preferences.t3_use_character_specific_fonts:
                self.entity_font = entity_font or self.entity_font
            else:
                self.entity_font = gui.preference("font", preferences.t3_default_font)

            self.character = Character(self.name, color=self.name_color, what_font=self.entity_font)
