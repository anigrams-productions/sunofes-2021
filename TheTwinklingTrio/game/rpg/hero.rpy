define CharacterType = enum(Nerdy="nerdy", Sporty="sporty", Perfect="perfect")

init python:
    class Hero:
        def __init__(self, character_type):
            # details we need to know and initialize about the hero/character
            
            if character_type == CharacterType.Nerdy:
                self.rpg_name = preferences.rpg_char_nerdy_name
                self.rpg_title = preferences.rpg_char_nerdy_title
            elif character_type == CharacterType.Sporty:
                self.rpg_name = preferences.rpg_char_sporty_name
                self.rpg_title = preferences.rpg_char_sporty_title
            elif character_type == CharacterType.Perfect:
                self.rpg_name = preferences.rpg_char_perfect_name
                self.rpg_title = preferences.rpg_char_perfect_title
            else:
                raise ValueError("Invalid character type {character_type} specified.")

            self.rpg_health = preferences.rpg_attribute_starting_health
            self.rpg_mana = preferences.rpg_attribute_starting_mana
            self.rpg_money = preferences.rpg_attribute_starting_money

            self.rpg_attribute_points = preferences.rpg_attribute_total_points
            self.rpg_style = 0
            self.rpg_magic = 0
            self.rpg_wisdom = 0

            self.rpg_level = 1
            self.rpg_experience_points = 0
            self.rpg_experience_needed = 100

        def is_active(self):
            return self.rpg_health > 0

        def can_level_up(self):
            return self.is_active() and (self.rpg_experience_points >= self.rpg_experience_needed)

        def level_up(self):
            if can_level_up(self):
                self.rpg_level += 1
                self.rpg_experience_needed *= 1.5
                self.rpg_attribute_points += 1

        def update_health(self, amount):
            self.rpg_health += amount

            # can't have negative health
            if self.rpg_health < 0:
                self.rpg_health = 0
        
        def update_mana(self, amount):
            self.rpg_mana += amount

            if self.rpg_mana < 0:
                self.rpg_mana = 0

        def update_money(self, amount):
            self.rpg_money += amount

            if self.rpg_money < 0:
                self.rpg_money = 0

        def reset_health(self):
            if preferences.rpg_attribute_restore_health:
                self.rpg_health = preferences.rpg_attribute_starting_health

        def reset_mana(self):
            if preferences.rpg_attribute_restore_mana:
                self.rpg_mana = preferences.rpg_attribute_starting_mana

        def reset_money(self):
            if preferences.rpg_attribute_restore_money:
                self.rpg_money = preferences.rpg_attribute_starting_money
