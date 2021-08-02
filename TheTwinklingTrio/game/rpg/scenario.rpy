init python:
    class Scenario:
        def __init__(self, theme, scenario_type):
            # details we need to know and initialize about the scenario
            self.theme = theme
            self.scenario_type = scenario_type

            if self.scenario_type == ScenarioType.Enemy:
                self.script = self.get_enemy()
            elif self.scenario_type == ScenarioType.Boss:
                self.script = self.get_boss()
            elif self.scenario_type == ScenarioType.Merchant:
                self.script = self.get_merchant()
            elif self.scenario_type == ScenarioType.Priest:
                self.script = self.get_priest()
            elif self.scenario_type == ScenarioType.Bard:
                self.script = self.get_bard()
            elif self.scenario_type == ScenarioType.Quest:
                self.script = self.get_quest()
            elif self.scenario_type == ScenarioType.Special:
                self.script = self.get_special()
            elif self.scenario_type == ScenarioType.Campfire:
                self.script = self.get_campfire()
            elif self.scenario_type == ScenarioType.Treasure:
                self.script = self.get_treasure()
            elif self.scenario_type == ScenarioType.Puzzle:
                self.script = self.get_puzzle()
            elif self.scenario_type == ScenarioType.Trap:
                self.script = self.get_trap()
            else:
                raise ValueError("Invalid scenario type {scenario_type} specified.")

        def get_enemy(self):
            # get random enemy based on theme and return name of enemy script to run
            if self.theme == Theme.Field:
                enemy_list = FieldEnemies
            elif self.theme == Theme.Desert:
                enemy_list = DesertEnemies
            else:
                raise ValueError("Invalid theme {self.theme} specified.")

            random_enemy = renpy.random.choice(enemy_list)

            return "scenario_" + random_enemy.theme + "_enemy_" + random_enemy.enemy_type

        def get_boss(self, boss = None):
            # get boss - if boss Enemy is supplied, return that one, otherwise choose random
            # return name of boss script to run
            
            if self.theme == Theme.Field:
                boss_list = FieldBosses
            elif self.theme == Theme.Desert:
                boss_list = DesertBosses
            else:
                raise ValueError("Invalid theme {self.theme} specified.")

            random_boss = boss or renpy.random.choice(boss_list)

            return "scenario_" + random_boss.theme + "_boss_" + random_boss.enemy_type

        def get_merchant(self):
            # return name of merchant script to run
            return "scenario_" + self.theme + "_merchant"

        def get_priest(self):
            # return name of priest script to run
            return "scenario_" + self.theme + "_priest"

        def get_bard(self):
            # return name of bard script to run
            return "scenario_" + self.theme + "_bard"

        def get_quest(self):
            # return name of quest giver script to run
            return "scenario_" + self.theme + "_quest"

        def get_special(self):
            # return name of special NPC script to run
            return "scenario_" + self.theme + "_special"

        def get_campfire(self):
            # return name of campfire script to run
            return "scenario_" + self.theme + "_campfire"

        def get_treasure(self):
            # return name of treasure script to run
            return "scenario_" + self.theme + "_treasure"

        def get_puzzle(self):
            # return name of puzzle script to run
            return "scenario_" + self.theme + "_puzzle"

        def get_trap(self):
            # return name of trap script to run
            return "scenario_" + self.theme + "_trap"
