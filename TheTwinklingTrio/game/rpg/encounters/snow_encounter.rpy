label t3_encounter_snow_start:

    scene black

    # Some description

    scene bg rpg snow

    # "Chapter 4: ???"

    call t3_encounter_scenarios_play from _call_t3_encounter_scenarios_play_4

    return

label t3_encounter_snow_success:
    "You won!"

    return

label t3_encounter_snow_failure:
    "You lost..."

    return