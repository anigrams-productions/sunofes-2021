## This file contains additional game preferences.
## These will eventually be modifiable through the Advanced Settings menu.
## More details: https://github.com/anigrams-productions/sunofes-2021/blob/main/Game%20Design/Interface/Advanced%20Settings.md

# Initialize Enumerations
define AutoSelection = enum("On","Others", "Off")
define Frequency = enum("Low","Normal","High")
define Difficulty = enum("Casual","Easy","Normal","Hard","Nightmare")

## NAMES
#### char = character
default preferences.char_nerdy_name = "Lisa"
default preferences.rpg_char_nerdy_name = "Endaleus"
default preferences.rpg_char_nerdy_title = "Ancient Hermit"

default preferences.char_sporty_name = "Christine"
default preferences.rpg_char_sporty_name = "Desiree"
default preferences.rpg_char_sporty_title = "Fairy Princess"

default preferences.char_perfect_name = "Jane"
default preferences.rpg_char_perfect_name = "Lustrea"
default preferences.rpg_char_perfect_title = "Rainbow Witch"

default preferences.rpg_group_name = config.name
default preferences.rpg_group_name_short = "T3"

## PRONOUNS
## See https://uwm.edu/lgbtrc/support/gender-pronouns/
#### sub = subject
#### obj = object
#### pos = possessive
#### poss = possessive pronoun (usually possessive + "s")
#### ref = reflexive
default preferences.pronoun_nerdy_sub = "she"
default preferences.pronoun_nerdy_obj = "her"
default preferences.pronoun_nerdy_pos = "her"
default preferences.pronoun_nerdy_poss = "hers"
default preferences.pronoun_nerdy_ref = "herself"

default preferences.rpg_pronoun_nerdy_sub = "they"
default preferences.rpg_pronoun_nerdy_obj = "them"
default preferences.rpg_pronoun_nerdy_pos = "their"
default preferences.rpg_pronoun_nerdy_poss = "theirs"
default preferences.rpg_pronoun_nerdy_ref = "themself"

default preferences.pronoun_sporty_sub = "she"
default preferences.pronoun_sporty_obj = "her"
default preferences.pronoun_sporty_pos = "her"
default preferences.pronoun_sporty_poss = "hers"
default preferences.pronoun_sporty_ref = "herself"

default preferences.rpg_pronoun_sporty_sub = "she"
default preferences.rpg_pronoun_sporty_obj = "her"
default preferences.rpg_pronoun_sporty_pos = "her"
default preferences.rpg_pronoun_sporty_poss = "hers"
default preferences.rpg_pronoun_sporty_ref = "herself"

default preferences.pronoun_perfect_sub = "she"
default preferences.pronoun_perfect_obj = "her"
default preferences.pronoun_perfect_pos = "her"
default preferences.pronoun_perfect_poss = "hers"
default preferences.pronoun_perfect_ref = "herself"

default preferences.rpg_pronoun_perfect_sub = "she"
default preferences.rpg_pronoun_perfect_obj = "her"
default preferences.rpg_pronoun_perfect_pos = "her"
default preferences.rpg_pronoun_perfect_poss = "hers"
default preferences.rpg_pronoun_perfect_ref = "herself"

## GAMEPLAY - ATTRIBUTES
default preferences.rpg_attribute_total_points = 30
default preferences.rpg_attribute_starting_health = 100
default preferences.rpg_attribute_starting_mana = 100
default preferences.rpg_attribute_starting_money = 100

default preferences.rpg_attribute_restore_health = True
default preferences.rpg_attribute_restore_mana = True
default preferences.rpg_attribute_restore_money = False

## GAMEPLAY - RANDOMIZATION
#### min = minimum
#### max = maximum
default preferences.rpg_random_strength_weakness = False
default preferences.rpg_random_attribute_allocation = False

default preferences.rpg_random_seed = None

default preferences.rpg_random_min_scenarios = 5
default preferences.rpg_random_max_scenarios = 7

## GAMEPLAY - AUTOMATION
#### auto = automatic
default preferences.rpg_auto_scenarios = AutoSelection.Others
default preferences.rpg_auto_actions = AutoSelection.Others

## GAMEPLAY - DIFFICULTY AND OTHER OPTIONS
default preferences.rpg_option_battle_frequency = Frequency.Normal
default preferences.rpg_option_battle_difficulty = Difficulty.Normal
default preferences.rpg_option_puzzle_difficulty = Difficulty.Normal
