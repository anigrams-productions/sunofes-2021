label t3_encounter_field_start:

    scene black

    nerdy "Word had spread of several human villages mysteriously disappearing without a trace."
    nerdy "Seeking answers, the [preferences.t3_rpg_char_nerdy_title] requested aid from the non-human races."
    nerdy "The fairies sent a royal ambassador, {color=#6684a3}[preferences.t3_rpg_char_sporty_name] the [preferences.t3_rpg_char_sporty_title]{/color}, to accompany the [preferences.t3_rpg_char_nerdy_title]."

    sporty "Hey, that's me!"

    nerdy "And the sorcerers sent the most powerful among them, {color=#6684a3}[preferences.t3_rpg_char_perfect_name] the [preferences.t3_rpg_char_perfect_title]{/color}, to lend [preferences.t3_rpg_pronoun_perfect_pos] strength."

    perfect "Of course, happy to help."

    nerdy "And so, the three of them traveled to a lush, fantastical meadow, where the first human village was rumored to have disappeared."

    scene bg rpg field

    "Chapter 1: In Fields Where We Lay"

    call t3_encounter_scenarios_play

    return

label t3_encounter_field_success:
    "You won!"

    return

label t3_encounter_field_failure:
    "You lost..."

    return