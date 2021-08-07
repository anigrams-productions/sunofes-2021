label t3_encounter_field_start:

    # scene black

    # TODO: show title screen

    # nerdy "Word had spread of a terrible curse afflicting humans and turning them into fearsome monsters."
    # nerdy "Seeking answers, the [preferences.t3_rpg_char_nerdy_title] requested aid from the non-human races."
    # nerdy "The fairies sent a royal ambassador, [preferences.t3_rpg_char_sporty_name] the [preferences.t3_rpg_char_sporty_title], to accompany the [preferences.t3_rpg_char_nerdy_title]."

    # sporty "Hey, that's me!"

    # nerdy "And the sorcerers sent the most powerful among them, [preferences.t3_rpg_char_perfect_name] the [preferences.t3_rpg_char_perfect_title], to lend [preferences.t3_rpg_pronoun_perfect_pos] strength."

    # perfect "Of course, happy to help."

    scene bg rpg field

    # nerdy "The three of them traveled to a lush, fantastical meadow, where the first monsters were rumored to have appeared."

    call t3_encounter_scenarios_play

    return

label t3_encounter_field_success:
    "You won!"

    return

label t3_encounter_field_failure:
    "You lost..."

    return