label t3_scenario_field_quest:
    nerdy "The meadow was eerily quiet."
    nerdy "No animals, no monsters, no humans. Only silence."

    show nerdy icon at centerleft with dissolve

    rpg_nerdy "The intell I gathered pointed to this place, but it would seem there's nothing here."

    hide nerdy icon
    show sporty icon at truecenter with dissolve

    rpg_sporty "So what now?"

    hide sporty icon
    show perfect icon at centerright with dissolve

    rpg_perfect "We should look around for clues. Perhaps we'll find something."

    hide perfect icon
    show sporty icon at truecenter with dissolve

    rpg_sporty "Do you think that thing's a clue?"

    hide sporty icon
    show npc field quest at top with dissolve

    nerdy "A conspicuous training dummy stood alone in the middle of the meadow."
    nerdy "In order to interact with objects and people in the world, we have to perform actions."
    nerdy "Remember that the success or failure of an action depends on your attributes, including a strength bonus and weakness penalty."
    
    show nerdy icon at centerleft with dissolve
    
    rpg_nerdy "I'll go first."

    # Make sure nerdy is the current player since this is the tutorial
    $ game_state.t3_current_player = game_state.t3_player_nerdy
    $ game_state.t3_current_player.style = 15

    menu:
        "What should I do?"

        "Style choice":

            "I chose Style. I currently have [game_state.t3_current_player.style] Style."

            $ game_state.roll_dice()

            show dice_1 at diceleft onlayer dice with dissolve
            show dice_2 at dicecenter onlayer dice with dissolve
            show dice_3 at diceright onlayer dice with dissolve

            if game_state.t3_current_player.has_enough_style(game_state.t3_total_dice_roll):
                "I rolled [game_state.t3_total_dice_roll] and I have [game_state.t3_current_player.style] Style."
                "I am successful."
            else:
                "I rolled [game_state.t3_total_dice_roll] but I only have [game_state.t3_current_player.style] Style."
                "I am a failure."

        "Magic choice (cost 1 Mana)":

            "I chose Magic"

            # if has_enough_attribute():
                # success
            # else:
                # failure
        "Wisdom choice":

            "I chose Wisdom"

            # if has_enough_attribute():
                # success
            # else:
                # failure

    return

label t3_scenario_field_special:
    "You met a special NPC."

    return

label t3_scenario_field_merchant:
    "You met a merchant."

    return

label t3_scenario_field_priest:
    "You met a priest."

    return

label t3_scenario_field_bard:
    "You met a bard."

    return