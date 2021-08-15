init python:
    class Hero(Entity):
        def __init__(self, character_type):
            # details we need to know and initialize about the hero/character
            self.character_type = character_type

            if self.character_type == CharacterType.Nerdy:
                self.get_nerdy_values()
            elif self.character_type == CharacterType.Sporty:
                self.get_sporty_values()
            elif self.character_type == CharacterType.Perfect:
                self.get_perfect_values()
            else:
                raise ValueError("Invalid character type " + character_type + " specified.")

            icon = character_type + ' icon'

            health = preferences.t3_rpg_attribute_starting_health
            mana = preferences.t3_rpg_attribute_starting_mana
            money = preferences.t3_rpg_attribute_starting_money

            self.attribute_points = preferences.t3_rpg_attribute_total_points
            # TODO: set these back to 0 before shipping the game
            style = 10
            magic = 10
            wisdom = 10

            self.level = 1
            self.experience_points = 0
            self.experience_needed = 100

            # used to keep track of "memories" from each encounter
            self.enemies_met = []
            self.enemies_defeated = []
            self.enemies_defeated_by = []
            self.enemies_pacified = []
            self.bosses_met = []
            self.bosses_defeated = []
            self.bosses_defeated_by = []
            self.bosses_pacified = []
            self.merchants_met = []
            self.merchant_items_purchased = []
            self.priests_met = []
            self.priest_blessings_purchased = []
            self.bards_met = []
            self.campfires_used = []
            self.treasure_found = []
            self.money_found = 0
            self.puzzles_encountered = []
            self.puzzles_solved = []
            self.traps_encountered = []
            self.traps_defeated = []

            Entity.__init__(self, character_type, self.name, icon, health, mana, money, style, magic, wisdom, self.strength, self.weakness, self.color)

        def get_nerdy_values(self):
            self.name = preferences.t3_rpg_char_nerdy_name
            self.title = preferences.t3_rpg_char_nerdy_title
            self.color = "#827281"
            self.action_start_phrases = ["It's my turn.", "Time for me to act.", "I'm ready."]
            self.level_up_phrases = ["I leveled up.", "I've gotten stronger.", "I can be better."]
            # TODO: allow for randomizing strength and weakness
            self.strength = AttributeType.Wisdom
            self.weakness = AttributeType.Style

        def get_sporty_values(self):
            self.name = preferences.t3_rpg_char_sporty_name
            self.title = preferences.t3_rpg_char_sporty_title
            self.color = "#e5914f"
            self.action_start_phrases = ["Sweet, it's my time to shine!", "I'm ready to go!", "Let's do this!"]
            self.level_up_phrases = ["Awesome, I leveled up!", "I feel stronger already!", "Ultimate POWER!!"]
            # TODO: allow for randomizing strength and weakness
            self.strength = AttributeType.Style
            self.weakness = AttributeType.Wisdom

        def get_perfect_values(self):
            self.name = preferences.t3_rpg_char_perfect_name
            self.title = preferences.t3_rpg_char_perfect_title
            self.color = "#e3848e"
            self.action_start_phrases = ["Oh, it's my turn already?", "I'll show you how it's done.", "I'm ready whenever you are."]
            self.level_up_phrases = ["Nice, I leveled up.", "My hard work must be paying off.", "I promise to work even harder."]
            # TODO: allow for randomizing strength and weakness
            self.strength = AttributeType.Magic
            self.weakness = None

        def get_action_start_phrase(self):
            return renpy.random.choice(self.action_start_phrases)

        def get_level_up_phrase(self):
            return renpy.random.choice(self.level_up_phrases)

        def can_level_up(self):
            return self.is_active() and (self.experience_points >= self.experience_needed)

        def level_up(self):
            if can_level_up(self):
                # "Pay" the experience points necessary to level up
                self.experience_points -= self.experience_needed

                # Increase level, grant an extra attribute point, and increase the exp needed for the next level
                self.level += 1
                self.attribute_points += 1
                self.experience_needed *= 1.5

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

        def gain_experience(self, success):
            exp = 0

            if success:
                exp = renpy.random.randint(preferences.t3_rpg_random_min_exp_success, preferences.t3_rpg_random_max_exp_success)
            else:
                exp = renpy.random.randint(preferences.t3_rpg_random_min_exp_failure, preferences.t3_rpg_random_max_exp_failure)

            self.experience_points += exp

            return exp

        def has_encountered_enemy(self, enemy):
            return enemy in self.enemies_met or enemy in self.bosses_met

        def has_encountered_enemy_type(self, enemy):
            enemy_types_encountered = list(map(lambda x: x.enemy_type, self.enemies_met))
            enemy_types_encountered.append(list(map(lambda x: x.enemy_type, self.bosses_met)))

            return enemy.enemy_type in enemy_types_encountered

        def has_defeated_enemy(self, enemy):
            return enemy in self.enemies_defeated or enemy in self.bosses_defeated

        def has_pacified_enemy(self, enemy):
            return enemy in self.enemies_pacified or enemy in self.bosses_pacified
