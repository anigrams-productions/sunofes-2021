label t3_encounter_desert_start:

    scene black

    # Some description

    scene bg rpg desert

    # "Chapter 3: ???"

    call t3_encounter_scenarios_play

    return

label t3_encounter_desert_success:
    "You won!"

    return

label t3_encounter_desert_failure:
    "You lost..."

    return