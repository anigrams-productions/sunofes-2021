init python:
    class Hero(Entity):
        def __init__(self, character_type):
            # details we need to know and initialize about the hero/character
            self.character_type = character_type

            if self.character_type == CharacterType.Nerdy:
                name = preferences.t3_rpg_char_nerdy_name
                self.title = preferences.t3_rpg_char_nerdy_title
                # TODO: allow for randomizing strength and weakness
                strength = AttributeType.Wisdom
                weakness = AttributeType.Style
            elif self.character_type == CharacterType.Sporty:
                name = preferences.t3_rpg_char_sporty_name
                self.title = preferences.t3_rpg_char_sporty_title
                # TODO: allow for randomizing strength and weakness
                strength = AttributeType.Style
                weakness = AttributeType.Wisdom
            elif self.character_type == CharacterType.Perfect:
                name = preferences.t3_rpg_char_perfect_name
                self.title = preferences.t3_rpg_char_perfect_title
                # TODO: allow for randomizing strength and weakness
                strength = AttributeType.Magic
                weakness = None
            else:
                raise ValueError("Invalid character type " + character_type + " specified.")

            icon = character_type + ' icon'

            health = preferences.t3_rpg_attribute_starting_health
            mana = preferences.t3_rpg_attribute_starting_mana
            money = preferences.t3_rpg_attribute_starting_money

            self.attribute_points = preferences.t3_rpg_attribute_total_points
            style = 0
            magic = 0
            wisdom = 0

            self.level = 1
            self.experience_points = 0
            self.experience_needed = 100

            # used to keep track of "memories" from each encounter
            self.enemies_met = []
            self.enemies_defeated = []
            self.enemies_defeated_by = []
            self.bosses_met = []
            self.bosses_defeated = []
            self.bosses_defeated_by = []
            self.merchants_met = []
            self.merchant_items_purchased = []
            self.priests_met = []
            self.priest_blessings_purchased = []
            self.bards_met = []
            self.treasure_found = []
            self.puzzles_encountered = []
            self.puzzles_solved = []
            self.traps_encountered = []
            self.traps_defeated = []

            Entity.__init__(self, character_type, name, icon, health, mana, money, style, magic, wisdom, strength, weakness)

        def can_level_up(self):
            return self.is_active() and (self.experience_points >= self.experience_needed)

        def level_up(self):
            if can_level_up(self):
                self.level += 1
                self.experience_needed *= 1.5
                self.attribute_points += 1

        def reset_health(self):
            if preferences.t3_rpg_attribute_restore_health:
                self.health = preferences.t3_rpg_attribute_starting_health

        def reset_mana(self):
            if preferences.t3_rpg_attribute_restore_mana:
                self.mana = preferences.t3_rpg_attribute_starting_mana

        def reset_money(self):
            if preferences.t3_rpg_attribute_restore_money:
                self.money = preferences.t3_rpg_attribute_starting_money

        def increase_style(self, amount):
            self.style += amount
            calculate_modified_attributes()

        def increase_magic(self, amount):
            self.magic += amount
            calculate_modified_attributes()

        def increase_wisdom(self, amount):
            self.wisdom += amount
            calculate_modified_attributes()

        def increase_experience(self, amount):
            self.expected_points += amount
