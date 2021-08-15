init python:
    class GameState:
        def __init__(self):
            self.t3_player_nerdy = Hero(CharacterType.Nerdy)
            self.t3_player_sporty = Hero(CharacterType.Sporty)
            self.t3_player_perfect = Hero(CharacterType.Perfect)

            self.t3_villain = GraveyardBosses[0]
            self.t3_villain_known_name = preferences.t3_rpg_char_villain_title
            self.t3_villain_actual_name = preferences.t3_rpg_char_villain_name

            self.t3_players = [self.t3_player_nerdy, self.t3_player_sporty, self.t3_player_perfect]
            self.t3_current_player = self.t3_players[0]

            self.t3_encounters = self.get_encounters()
            self.t3_current_encounter = self.t3_encounters[0]

            self.t3_current_scenario = None
            self.t3_current_action = None
            self.t3_current_action_round = 0

            self.t3_current_speaker = None
            
            self.update_remaining_players()

            self.t3_attribute_points_to_allocate = preferences.t3_rpg_attribute_total_points

            self.t3_dice_roll_1 = 1
            self.t3_dice_roll_2 = 1
            self.t3_dice_roll_3 = 1
            self.t3_total_dice_roll = 0

            self.t3_experience_gained = 0

            self.t3_training_dummy = QuestNpcs[0]
            self.t3_training_dummy_known_name = "Training Dummy"
            self.t3_training_dummy_actual_name = "Rembi"
            self.t3_egg_man_known_name = "Egg Man"
            self.t3_egg_man_actual_name = "Korro"

        def get_encounters(self):
            encounter_types = [Theme.Field, Theme.Volcano, Theme.Desert, Theme.Snow, Theme.Graveyard]
            encounters = []

            for theme in encounter_types:
                encounters.append(Encounter(theme, self.t3_players, self.t3_current_player))

            return encounters

        def get_scenario_menu(self):
            scenario_options = self.t3_current_encounter.pick_random_scenarios()
            scenario_menu_options = []

            for option in scenario_options:
                scenario_menu_options.append((option.menu_label, option))

            narrator("Where should {color=#6684a3}[game_state.t3_current_player.name]{/color} go next?", interact=False)
            selected_scenario = renpy.display_menu(scenario_menu_options)

            self.t3_current_encounter.select_scenario(selected_scenario)
            self.t3_current_scenario = selected_scenario

        def get_action_menu(self, actions):
            action_options = filter(lambda action: action.character_type == self.t3_current_player.character_type, actions)
            action_menu_options = []

            for option in action_options:
                option_as_action = Action(self.t3_current_scenario.script, self.t3_current_player, option.action_type, self.t3_current_action_round, self.t3_total_dice_roll, option.mana_cost, option.money_cost, option.health_cost)
                
                # only add it to the menu if the player can actually do it
                if option_as_action.is_available():
                    action_menu_options.append((option.menu_label, option_as_action))

            narrator("What should {color=#6684a3}[game_state.t3_current_player.name]{/color} do?", interact=False)
            selected_action = renpy.display_menu(action_menu_options)

            self.t3_current_action = selected_action

        def update_remaining_players(self):
            self.t3_remaining_players = self.t3_current_encounter.get_active_players()

        def get_next_encounter(self):
            current_index = self.t3_encounters.index(self.t3_current_encounter)
            current_index += 1

            # if we reach the end of the list, return nothing
            if current_index > (len(self.t3_encounters) - 1):
                return None

            self.t3_current_encounter = self.t3_encounters[current_index]

            return self.t3_current_encounter

        def calculate_attribute_allocation(self, level, current_points = 0):
            expected_points = 0
            if level == AttributeAllocation.Novice:
                expected_points = round(preferences.t3_rpg_attribute_total_points * 0.167)
            elif level == AttributeAllocation.Average:
                expected_points = round(preferences.t3_rpg_attribute_total_points * 0.333)
            elif level == AttributeAllocation.Expert:
                expected_points = round(preferences.t3_rpg_attribute_total_points * 0.5)

            # if expected points is greater than the points remaining, go ahead and return the points remaining
            if expected_points > (preferences.t3_rpg_attribute_total_points - current_points):
                expected_points = preferences.t3_rpg_attribute_total_points - current_points

            return expected_points

        def roll_dice(self):
            self.t3_dice_roll_1 = renpy.random.randint(1, 6)
            self.t3_dice_roll_2 = renpy.random.randint(1, 6)
            self.t3_dice_roll_3 = renpy.random.randint(1, 6)

            self.t3_total_dice_roll = self.t3_dice_roll_1 + self.t3_dice_roll_2 + self.t3_dice_roll_3

        def have_players_killed(self):
            return len(self.t3_player_nerdy.enemies_defeated) > 0 or len(self.t3_player_sporty.enemies_defeated) > 0 or len(self.t3_player_perfect.enemies_defeated) > 0