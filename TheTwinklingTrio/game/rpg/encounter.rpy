define Theme = enum(
    Field="field",
    Volcano="volcano",
    Desert="desert",
    Snow="snow",
    Graveyard="grave"
)

init python:
    class Encounter:
        def __init__(self, theme):
            # details we need to know and initialize about the encounter

            # theme determines just about everything
            self.theme = theme

            # determine how long this particular encounter will last (minus mandatory scenarios)
            self.number_of_scenarios = get_number_of_scenarios()

            # keep track of which scenario we're currently on, default 0 (first)
            self.current_scenario = 0

            # TODO: generate list of possible scenarios based on battle frequency setting
            # make sure to add on quest, special, and boss scenarios after determining random scenarios

            # reset resource values if options are enabled
            # some character.reset_health()

        def get_number_of_scenarios():
            # TODO: Make sure we're using the correct random seed
            return renpy.random.randint(preferences.rpg_random_min_scenarios, preferences.rpg_random_max_scenarios)

        # def next_scenario(self):
            # TODO: call each character's level_up() method

            # TODO: check if party has failed prematurely (all characters dead) - if so, call get_failure()

            # TODO: check if we've reached the end of the encounter - if so, call get_success()

            # if we can't hit anything yet, call pick_scenarios_for_selection()

        # def pick_scenarios_for_selection(self):
            # TODO: Pick 3 random scenarios from list of possible scenarios

        def select_scenario(self, scenario):
            # TODO: Do something with the scenario selected

            self.current_scenario += 1

        # def get_success(self):
            # TODO: return name of success script to run

        # def get_failure(self):
            # TODO: return name of failure script to run
