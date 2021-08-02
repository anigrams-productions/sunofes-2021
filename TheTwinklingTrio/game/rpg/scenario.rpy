define ScenarioType = enum(
    Enemy="enemy",
    Boss="boss",
    Merchant="merchant",
    Priest="priest",
    Bard="bard",
    Quest="quest",
    Special="special",
    Campfire="campfire",
    Treasure="treasure",
    Puzzle="puzzle",
    Trap="trap"
)

init python:
    class Scenario:
        def __init__(self, theme, scenario_type):
            # details we need to know and initialize about the scenario
            self.theme = theme
            self.scenario_type = scenario_type

            # TODO: case statement on scenario_type to call one of the get() methods to return the appropriate script

        # def get_enemy(self):
            # TODO: get random enemy based on theme and return name of enemy script to run

        # def get_boss(self, monster = None):
            # TODO: get boss - if monster is supplied, return that one, otherwise choose random
            # return name of boss script to run

        # def get_merchant(self):
            # TODO: return name of merchant script to run

        # def get_priest(self):
            # TODO: return name of priest script to run

        # def get_bard(self):
            # TODO: return name of bard script to run

        # def get_quest(self):
            # TODO: return name of quest giver script to run

        # def get_special(self):
            # TODO: return name of special NPC script to run

        # def get_campfire(self):
            # TODO: return name of campfire script to run

        # def get_treasure(self):
            # TODO: return name of treasure script to run

        # def get_puzzle(self):
            # TODO: return name of puzzle script to run

        # def get_trap(self):
            # TODO: return name of trap script to run