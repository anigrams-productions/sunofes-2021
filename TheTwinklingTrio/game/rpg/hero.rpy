init python:
    class Hero(Entity):
        def __init__(self, character_type):
            # details we need to know and initialize about the hero/character
            self.character_type = character_type

            if self.character_type == CharacterType.Nerdy:
                self.name = preferences.rpg_char_nerdy_name
                self.title = preferences.rpg_char_nerdy_title
            elif self.character_type == CharacterType.Sporty:
                self.name = preferences.rpg_char_sporty_name
                self.title = preferences.rpg_char_sporty_title
            elif self.character_type == CharacterType.Perfect:
                self.name = preferences.rpg_char_perfect_name
                self.title = preferences.rpg_char_perfect_title
            else:
                raise ValueError("Invalid character type {character_type} specified.")

            self.icon = character_type + ' icon'

            self.health = preferences.rpg_attribute_starting_health
            self.mana = preferences.rpg_attribute_starting_mana
            self.money = preferences.rpg_attribute_starting_money

            self.attribute_points = preferences.rpg_attribute_total_points
            self.style = 0
            self.magic = 0
            self.wisdom = 0

            self.level = 1
            self.experience_points = 0
            self.experience_needed = 100

        def can_level_up(self):
            return self.is_active() and (self.experience_points >= self.experience_needed)

        def level_up(self):
            if can_level_up(self):
                self.level += 1
                self.experience_needed *= 1.5
                self.attribute_points += 1

        def reset_health(self):
            if preferences.rpg_attribute_restore_health:
                self.health = preferences.rpg_attribute_starting_health

        def reset_mana(self):
            if preferences.rpg_attribute_restore_mana:
                self.mana = preferences.rpg_attribute_starting_mana

        def reset_money(self):
            if preferences.rpg_attribute_restore_money:
                self.money = preferences.rpg_attribute_starting_money
