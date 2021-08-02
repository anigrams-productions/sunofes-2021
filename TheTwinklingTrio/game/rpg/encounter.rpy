init python:
    import math

    NonCombatScenarioTypes = [
        ScenarioType.Merchant,
        ScenarioType.Priest,
        ScenarioType.Bard,
        ScenarioType.Campfire,
        ScenarioType.Treasure,
        ScenarioType.Puzzle,
        ScenarioType.Trap
    ]

    class Encounter:
        def __init__(self, theme, players):
            # details we need to know and initialize about the encounter
            self.theme = theme
            self.players = players

            # determine how long this particular encounter will last (minus mandatory scenarios)
            self.number_of_scenarios = self.get_number_of_scenarios()

            # generate list of possible scenarios based on battle frequency setting
            self.scenarios = self.get_scenarios(self.get_battle_frequency())

            # make sure to add on quest, special, and boss scenarios after determining random scenarios
            self.scenarios.insert(0, Scenario(self.theme, ScenarioType.Quest)) # quest giver
            self.scenarios.append(Scenario(self.theme, ScenarioType.Boss)) # boss battle
            self.scenarios.append(Scenario(self.theme, ScenarioType.Special)) # objective

            # keep track of which scenario we're currently on, default 0 (first)
            self.current_scenario = self.scenarios[0]

            # reset resource values if options are enabled
            for player in self.get_active_players():
                player.reset_health()
                player.reset_mana()
                player.reset_money()

        def get_number_of_scenarios(self):
            # TODO: Make sure we're using the correct random seed
            return renpy.random.randint(preferences.rpg_random_min_scenarios, preferences.rpg_random_max_scenarios)

        def get_active_players(self):
            return filter(lambda player: player.is_active(), self.players.values())

        def get_battle_frequency(self):
            # translate battle frequency preference into a percentage of scenarios
            if preferences.rpg_option_battle_frequency == Frequency.Low:
                return .3
            elif preferences.rpg_option_battle_frequency == Frequency.Normal:
                return .5
            elif preferences.rpg_option_battle_frequency == Frequency.High:
                return .8
            else:
                raise ValueError("Invalid battle frequency {preferences.rpg_option_battle_frequency} specified.")

        def get_scenarios(self, battle_frequency):
            scenarios = []
            number_of_enemy_scenarios = int(math.floor(self.number_of_scenarios * battle_frequency))
            
            # sanity check: need to have at least one enemy and can't have more enemies than scenarios available
            if number_of_enemy_scenarios < 1:
                number_of_enemy_scenarios = 1
            elif number_of_enemy_scenarios > self.number_of_scenarios:
                number_of_enemy_scenarios = self.number_of_scenarios

            for n in range(number_of_enemy_scenarios):
                scenarios.append(Scenario(self.theme, ScenarioType.Enemy))

            # now to fill in the rest of the scenarios with non-combat encounters
            number_remaining_scenarios = self.number_of_scenarios - number_of_enemy_scenarios
            remaining_scenarios = renpy.random.sample(NonCombatScenarioTypes, number_remaining_scenarios)

            for scenario in remaining_scenarios:
                scenarios.append(Scenario(self.theme, scenario))

            renpy.random.shuffle(scenarios)

            return scenarios

        # def next_scenario(self):
            # TODO: call each character's level_up() method

            # TODO: check if party has failed prematurely (all characters dead) - if so, call return_failure()

            # TODO: check if we've reached the end of the encounter - if so, call return_success()

            # if we can't hit anything yet, call pick_scenarios_for_selection()

        # def pick_scenarios_for_selection(self):
            # TODO: Pick 3 random scenarios from list of possible scenarios

        def select_scenario(self, scenario):
            # TODO: Do something with the scenario selected

            self.current_scenario += 1

        # def get_success(self):
            # TODO: indicate encounter completed successfully

        # def get_failure(self):
            # TODO: indicate encounter did NOT complete successfully
