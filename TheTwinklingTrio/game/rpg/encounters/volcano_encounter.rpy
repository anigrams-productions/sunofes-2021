label t3_encounter_volcano_start:

    scene black

    # Some description

    scene bg rpg volcano

    # "Chapter 2: ???"

    call t3_encounter_scenarios_play from _call_t3_encounter_scenarios_play

    return

label t3_encounter_volcano_success:
    "You won!"

    return

label t3_encounter_volcano_failure:
    "You lost..."

    return