init python:
    class Action:
        def __init__(self, scenario_label, performed_by, action_type, id, points_required, mana_cost = 0, money_cost = 0, health_cost = 0):
            self.scenario_label = scenario_label
            self.performed_by = performed_by
            self.action_type = action_type
            self.id = id
            self.attribute_points_required = points_required
            self.mana_cost = mana_cost
            self.money_cost = money_cost
            self.health_cost = health_cost

            self.get_action_scripts()

        def get_action_scripts(self):
            base_label = str(self.scenario_label) + "_" + str(self.performed_by.character_type) + "_" + str(self.action_type) + "_" + str(self.id)

            self.success_script = base_label + "_success"
            self.failure_script = base_label + "_failure"
        
        def is_success(self):
            if self.action_type == AttributeType.Style:
                return self.performed_by.has_enough_style(self.attribute_points_required)
            elif self.action_type == AttributeType.Magic:
                return self.performed_by.has_enough_magic(self.attribute_points_required)
            elif self.action_type == AttributeType.Wisdom:
                return self.performed_by.has_enough_wisdom(self.attribute_points_required)
            else:
                raise ValueError("Invalid action type " + self.action_type + " specified.")

        def is_available(self):
            return self.performed_by.has_enough_health(self.health_cost) and \
                   self.performed_by.has_enough_mana(self.mana_cost) and \
                   self.performed_by.has_enough_money(self.money_cost)

        def return_action_result(self):
            if self.is_success():
                return self.success_script
            else:
                return self.failure_script

    class ActionMenuOption:
        def __init__(self, menu_label, character_type, action_type, mana_cost = 0, money_cost = 0, health_cost = 0):
            self.menu_label = menu_label
            self.character_type = character_type
            self.action_type = action_type
            self.mana_cost = mana_cost
            self.money_cost = money_cost
            self.health_cost = health_cost