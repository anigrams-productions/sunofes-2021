init python:
    import math

    NonCombatScenarioTypes = [
        ScenarioType.Merchant,
        # ScenarioType.Priest,
        # ScenarioType.Bard,
        ScenarioType.Campfire,
        ScenarioType.Treasure
        # ScenarioType.Puzzle,
        # ScenarioType.Trap
    ]

    class Encounter:
        def __init__(self, theme, players, current_player):
            # details we need to know and initialize about the encounter
            self.theme = theme
            self.players = players
            self.script = "t3_encounter_" + self.theme + "_start"

            # determine how long this particular encounter will last (minus mandatory scenarios)
            self.number_of_scenarios = self.get_number_of_scenarios()

            # generate list of possible scenarios based on battle frequency setting
            self.scenarios = self.get_scenarios(self.get_battle_frequency())

            # make sure to add quest, special, and boss scenarios after determining random scenarios
            self.scenario_quest = Scenario(self.theme, ScenarioType.Quest)
            self.scenario_boss = Scenario(self.theme, ScenarioType.Boss)
            self.scenario_special = Scenario(self.theme, ScenarioType.Special)

            # keep track of which scenario we're currently on, default 0 (first)
            self.current_scenario = self.scenarios[0]
            self.current_player = current_player

            # reset resource values if options are enabled
            for player in self.get_active_players():
                player.reset_health()
                player.reset_mana()
                player.reset_money()

        def get_number_of_scenarios(self):
            # TODO: Make sure we're using the correct random seed
            return renpy.random.randint(preferences.t3_rpg_random_min_scenarios, preferences.t3_rpg_random_max_scenarios)

        def get_active_players(self):
            return filter(lambda player: player.is_active(), self.players)

        def get_battle_frequency(self):
            # translate battle frequency preference into a number of scenarios
            if preferences.t3_rpg_option_battle_frequency == Frequency.Low:
                return .3
            elif preferences.t3_rpg_option_battle_frequency == Frequency.Normal:
                return .5
            elif preferences.t3_rpg_option_battle_frequency == Frequency.High:
                return .8
            else:
                raise ValueError("Invalid battle frequency " + preferences.t3_rpg_option_battle_frequency + " specified.")

        def get_scenarios(self, battle_frequency):
            scenarios = []
            
            # add non-combat encounters since there will always be the same number
            for scenario in NonCombatScenarioTypes:
                scenarios.append(Scenario(self.theme, scenario))

            # calculate how many enemy scenarios to include based on battle frequency option
            number_of_enemy_scenarios = int(math.floor(self.number_of_scenarios * battle_frequency))
            
            # sanity check: need to have at least one enemy and can't have more enemies than scenarios available
            if number_of_enemy_scenarios < 1:
                number_of_enemy_scenarios = 1
            elif number_of_enemy_scenarios > self.number_of_scenarios:
                number_of_enemy_scenarios = self.number_of_scenarios

            for n in range(number_of_enemy_scenarios):
                scenarios.append(Scenario(self.theme, ScenarioType.Enemy))

            return scenarios

        def pick_random_scenarios(self):
            number_of_samples = preferences.t3_rpg_number_scenario_options
            number_of_scenarios = len(self.scenarios)

            # if we don't have enough scenarios, generate some more
            if number_of_samples > number_of_scenarios:
                possible_scenario_types = []
                scenarios_to_generate = number_of_samples - number_of_scenarios

                possible_scenario_types.extend(NonCombatScenarioTypes)
                possible_scenario_types.append(ScenarioType.Enemy)

                for n in range(scenarios_to_generate):
                    scenario_type = renpy.random.choice(possible_scenario_types)
                    self.scenarios.append(Scenario(self.theme, scenario_type))

            return renpy.random.sample(self.scenarios, number_of_samples)

        def select_scenario(self, scenario):
            # set current scenario to the one that was passed in
            self.current_scenario = scenario

            # remove the scenario from the list of possible scenarios so it can't be picked again
            self.scenarios.remove(scenario)

        def get_next_player(self):
            current_index = self.players.index(self.current_player)
            current_index += 1

            # if we reach the end of the list, start back at 0
            if current_index > (len(self.players) - 1):
                current_index = 0

            self.current_player = self.players[current_index]

            return self.current_player
