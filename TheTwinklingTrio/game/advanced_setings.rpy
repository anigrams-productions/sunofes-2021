## This file contains additional game preferences.
## These will eventually be modifiable through the Advanced Settings menu.
## More details: https://github.com/anigrams-productions/sunofes-2021/blob/main/Game%20Design/Interface/Advanced%20Settings.md

## NAMES
#### char = character
default preferences.t3_char_nerdy_name = "Lisa"
default preferences.t3_rpg_char_nerdy_name = "Endaleus"
default preferences.t3_rpg_char_nerdy_title = "Ancient Hermit"

default preferences.t3_char_sporty_name = "Christine"
default preferences.t3_rpg_char_sporty_name = "Desiree"
default preferences.t3_rpg_char_sporty_title = "Fairy Princess"

default preferences.t3_char_perfect_name = "Jane"
default preferences.t3_rpg_char_perfect_name = "Lustrea"
default preferences.t3_rpg_char_perfect_title = "Moon Sorceress"

default preferences.t3_rpg_char_villain_name = "Keres"
default preferences.t3_rpg_char_villain_title = "The Dark Lord"

default preferences.t3_rpg_group_name = config.name
default preferences.t3_rpg_group_name_short = "T3"

## PRONOUNS
## See https://uwm.edu/lgbtrc/support/gender-pronouns/
#### sub = subject
#### obj = object
#### pos = possessive
#### poss = possessive pronoun (usually possessive + "s")
#### ref = reflexive
default preferences.t3_pronoun_nerdy_sub = "she"
default preferences.t3_pronoun_nerdy_obj = "her"
default preferences.t3_pronoun_nerdy_pos = "her"
default preferences.t3_pronoun_nerdy_poss = "hers"
default preferences.t3_pronoun_nerdy_ref = "herself"

default preferences.t3_rpg_pronoun_nerdy_sub = "they"
default preferences.t3_rpg_pronoun_nerdy_obj = "them"
default preferences.t3_rpg_pronoun_nerdy_pos = "their"
default preferences.t3_rpg_pronoun_nerdy_poss = "theirs"
default preferences.t3_rpg_pronoun_nerdy_ref = "themself"

default preferences.t3_pronoun_sporty_sub = "she"
default preferences.t3_pronoun_sporty_obj = "her"
default preferences.t3_pronoun_sporty_pos = "her"
default preferences.t3_pronoun_sporty_poss = "hers"
default preferences.t3_pronoun_sporty_ref = "herself"

default preferences.t3_rpg_pronoun_sporty_sub = "she"
default preferences.t3_rpg_pronoun_sporty_obj = "her"
default preferences.t3_rpg_pronoun_sporty_pos = "her"
default preferences.t3_rpg_pronoun_sporty_poss = "hers"
default preferences.t3_rpg_pronoun_sporty_ref = "herself"

default preferences.t3_pronoun_perfect_sub = "she"
default preferences.t3_pronoun_perfect_obj = "her"
default preferences.t3_pronoun_perfect_pos = "her"
default preferences.t3_pronoun_perfect_poss = "hers"
default preferences.t3_pronoun_perfect_ref = "herself"

default preferences.t3_rpg_pronoun_perfect_sub = "she"
default preferences.t3_rpg_pronoun_perfect_obj = "her"
default preferences.t3_rpg_pronoun_perfect_pos = "her"
default preferences.t3_rpg_pronoun_perfect_poss = "hers"
default preferences.t3_rpg_pronoun_perfect_ref = "herself"

default preferences.t3_rpg_pronoun_villain_sub = "they"
default preferences.t3_rpg_pronoun_villain_obj = "them"
default preferences.t3_rpg_pronoun_villain_pos = "their"
default preferences.t3_rpg_pronoun_villain_poss = "theirs"
default preferences.t3_rpg_pronoun_villain_ref = "themself"

## GAMEPLAY - ATTRIBUTES
default preferences.t3_rpg_attribute_total_points = 30
default preferences.t3_rpg_attribute_starting_health = 100
default preferences.t3_rpg_attribute_starting_mana = 100
default preferences.t3_rpg_attribute_starting_money = 100

default preferences.t3_rpg_attribute_restore_health = True
default preferences.t3_rpg_attribute_restore_mana = True
default preferences.t3_rpg_attribute_restore_money = False

## GAMEPLAY - RANDOMIZATION
#### min = minimum
#### max = maximum
#### exp = experience
# TODO: implement setting random seed
# default preferences.t3_rpg_random_seed = None

# TODO: implement random strengths and weaknesses
# default preferences.t3_rpg_random_strength_weakness = False
# TODO: implement random attribute allocation
# default preferences.t3_rpg_random_attribute_allocation = False

default preferences.t3_rpg_random_min_scenarios = 5
default preferences.t3_rpg_random_max_scenarios = 7

default preferences.t3_rpg_number_scenario_options = 3

default preferences.t3_rpg_random_max_exp_success = 100
default preferences.t3_rpg_random_min_exp_success = 51
default preferences.t3_rpg_random_max_exp_failure = 50
default preferences.t3_rpg_random_min_exp_failure = 1

default preferences.t3_rpg_random_max_money_reward = 1000
default preferences.t3_rpg_random_min_money_reward = 100

## GAMEPLAY - AUTOMATION
#### auto = automatic
# TODO: implement automatic selection of scenarios and actions
# default preferences.t3_rpg_auto_scenarios = AutoSelection.Others
# default preferences.t3_rpg_auto_actions = AutoSelection.Others

## GAMEPLAY - DIFFICULTY
default preferences.t3_rpg_option_battle_frequency = Frequency.Normal
default preferences.t3_rpg_option_battle_difficulty = Difficulty.Normal
default preferences.t3_rpg_option_puzzle_difficulty = Difficulty.Normal

## GAMEPLAY - SHOP
#### amt = amount
default preferences.t3_rpg_shop_health_potion_cost = 50
default preferences.t3_rpg_shop_health_potion_amt = 50
default preferences.t3_rpg_shop_mana_potion_cost = 50
default preferences.t3_rpg_shop_mana_potion_amt = 50

## ACCESSIBILITY
default preferences.t3_default_font = gui.preference("font", "fonts/normal/Chilanka-Regular.ttf")
default preferences.t3_default_font_size = gui.preference("size", 28)
default preferences.t3_use_character_specific_fonts = True