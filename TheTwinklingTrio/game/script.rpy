# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define nerdy = Character(preferences.char_nerdy_name)
define sporty = Character(preferences.char_sporty_name)
define perfect = Character(preferences.char_perfect_name)

init python:
    rpg_players = {
        CharacterType.Nerdy: Hero(CharacterType.Nerdy),
        CharacterType.Sporty: Hero(CharacterType.Sporty),
        CharacterType.Perfect: Hero(CharacterType.Perfect)
    }
    rpg_current_player = CharacterType.Nerdy

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

    $ rpg_current_encounter = Encounter(Theme.Field, rpg_players, rpg_players[rpg_current_player])

    call expression "encounter_" + rpg_current_encounter.theme + "_start"

    "We're back at the start label."

    # This ends the game.

    return
