# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define nerdy = Character(preferences.char_nerdy_name, color="#827281")
define sporty = Character(preferences.char_sporty_name, color="#e5914f")
define perfect = Character(preferences.char_perfect_name, color="#e3848e")

define rpg_nerdy = Character(preferences.rpg_char_nerdy_name, color="#827281")
define rpg_sporty = Character(preferences.rpg_char_sporty_name, color="#e5914f")
define rpg_perfect = Character(preferences.rpg_char_perfect_name, color="#e3848e")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room day open

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show nerdy casual 1 at topleft
    show sporty casual 1 at top
    show perfect casual 1 at topright

    # These display lines of dialogue.

    $ game_state = GameState()

    call expression game_state.current_encounter.script

    "We're back at the start label."

    # This ends the game.

    return
