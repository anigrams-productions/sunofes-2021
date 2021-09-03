label t3_scenario_field_boss_dragon:
    scene bg rpg field

    show other_icon at top with dissolve

    "The boss [game_state.t3_current_scenario.current_entity.name] appeared!"

    call t3_scenario_show_trio from _call_t3_scenario_show_trio_6

    if game_state.t3_current_player.character_type == CharacterType.Nerdy:
        rpg_nerdy "Careful. This one looks strong."

    elif game_state.t3_current_player.character_type == CharacterType.Sporty:
        rpg_sporty "Uh oh, this one looks bigger and stronger than the others."

    elif game_state.t3_current_player.character_type == CharacterType.Perfect:
        rpg_perfect "This will be a particularly tough battle. Be careful."

    call t3_scenario_enemy_battle_start from _call_t3_scenario_enemy_battle_start
    
    call t3_scenario_enemy_end from _call_t3_scenario_enemy_end

    return

label t3_scenario_field_boss_orc:
    call t3_scenario_enemy_orc from _call_t3_scenario_enemy_orc_3

    return