init python:
    class GameState:
        def __init__(self):
            self.players = self.get_players()
            self.current_player = self.players[0]

            self.encounters = self.get_encounters()
            self.current_encounter = self.encounters[0]

            self.current_scenario = None
            
            self.update_remaining_players()

        def get_players(self):
            character_types = [CharacterType.Nerdy, CharacterType.Sporty, CharacterType.Perfect]
            characters = []

            for character_type in character_types:
                characters.append(Hero(character_type))

            return characters

        def get_encounters(self):
            encounter_types = [Theme.Field, Theme.Volcano, Theme.Desert, Theme.Snow, Theme.Graveyard]
            encounters = []

            for theme in encounter_types:
                encounters.append(Encounter(theme, self.players, self.current_player))

            return encounters

        def get_scenario_menu(self):
            scenario_options = self.current_encounter.pick_random_scenarios()
            scenario_menu_options = []

            for option in scenario_options:
                scenario_menu_options.append((option.menu_label, option))

            narrator("Where should we go next?", interact=False)
            selected_scenario = renpy.display_menu(scenario_menu_options)

            self.current_encounter.select_scenario(selected_scenario)
            self.current_scenario = selected_scenario

        def update_remaining_players(self):
            self.remaining_players = self.current_encounter.get_active_players()
