label t3_encounter_grave_start:

    scene black

    # Some description

    scene bg rpg graveyard

    # "Chapter 5: ???"

    call t3_encounter_scenarios_play

    return

label t3_encounter_grave_success:
    "You won!"

    return

label t3_encounter_grave_failure:
    "You lost..."

    return