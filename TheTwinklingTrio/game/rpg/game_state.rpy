init python:
    class GameState:
        def __init__(self):
            self.t3_player_nerdy = Hero(CharacterType.Nerdy)
            self.t3_player_sporty = Hero(CharacterType.Sporty)
            self.t3_player_perfect = Hero(CharacterType.Perfect)

            self.t3_players = [self.t3_player_nerdy, self.t3_player_sporty, self.t3_player_perfect]
            self.t3_current_player = self.t3_players[0]

            self.t3_encounters = self.get_encounters()
            self.t3_current_encounter = self.t3_encounters[0]

            self.t3_current_scenario = None
            
            self.update_remaining_players()

            self.t3_attribute_points_to_allocate = preferences.t3_rpg_attribute_total_points

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

            narrator("Where should we go next?", interact=False)
            selected_scenario = renpy.display_menu(scenario_menu_options)

            self.t3_current_encounter.select_scenario(selected_scenario)
            self.t3_current_scenario = selected_scenario

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