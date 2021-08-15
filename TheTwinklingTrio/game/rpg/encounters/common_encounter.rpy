label t3_encounter_scenarios_play:
    ## Start by meeting the quest giver
    $ game_state.t3_current_scenario = game_state.t3_current_encounter.scenario_quest
    $ game_state.t3_current_scenario.current_entity.update_character_name(game_state.t3_current_scenario.current_entity.name)
    call expression game_state.t3_current_encounter.scenario_quest.script
    call t3_encounter_scenario_end

    ## Begin the random scenarios...
    $ scenario_count = 1
    while scenario_count <= game_state.t3_current_encounter.number_of_scenarios:
        # "This is scenario [scenario_count] out of [game_state.t3_current_encounter.number_of_scenarios]. Current player is [game_state.t3_current_player.name]."
        call t3_encounter_scenario_select

        $ scenario_count += 1

    ## Meet the boss
    $ game_state.t3_current_scenario = game_state.t3_current_encounter.scenario_boss
    $ game_state.t3_current_scenario.current_entity.update_character_name(game_state.t3_current_scenario.current_entity.name)
    call expression game_state.t3_current_encounter.scenario_boss.script
    call t3_encounter_scenario_end

    ## Finally, reach the objective
    $ game_state.t3_current_scenario = game_state.t3_current_encounter.scenario_objective
    $ game_state.t3_current_scenario.current_entity.update_character_name(game_state.t3_current_scenario.current_entity.name)
    call expression game_state.t3_current_encounter.scenario_objective.script
    call t3_encounter_scenario_end
        
    jump expression "t3_encounter_" + game_state.t3_current_encounter.theme + "_success"

label t3_encounter_scenario_select:
    $ game_state.get_scenario_menu()

    $ game_state.t3_current_scenario.current_entity.update_character_name(game_state.t3_current_scenario.current_entity.name)

    call expression game_state.t3_current_scenario.script

    call t3_encounter_scenario_end

    $ game_state.t3_current_player = game_state.t3_current_encounter.get_next_player()
    
    return

label t3_encounter_scenario_end:
    hide other_icon

    ## Check if anyone's still alive
    $ game_state.update_remaining_players()

    if len(game_state.t3_remaining_players) <= 0:
        jump expression "t3_encounter_" + game_state.t3_current_encounter.theme + "_failure"

    ## If we still have active players, check if they can level up
    $ active_player_count = 0
    while active_player_count < len(game_state.t3_remaining_players):
        if game_state.t3_remaining_players[active_player_count].can_level_up():
            call expression "t3_encounter_scenario_level_up_" + game_state.t3_remaining_players[active_player_count].character_type
        
        $ active_player_count += 1

    return

label t3_encounter_scenario_level_up_nerdy:
    $ nerdy_rpg(game_state.t3_player_sporty.get_level_up_phrase())

    $ game_state.t3_player_nerdy.level_up()

    menu:
        "Which attribute should be increased?"

        "Style":
            $ game_state.t3_player_nerdy.style += 1
            "[game_state.t3_player_nerdy.name] now has [game_state.t3_player_nerdy.style] {color=#6684a3}Style{/color}."
        "Magic":
            $ game_state.t3_player_nerdy.magic += 1
            "[game_state.t3_player_nerdy.name] now has [game_state.t3_player_nerdy.magic] {color=#6684a3}Magic{/color}."
        "Wisdom":
            $ game_state.t3_player_nerdy.wisdom += 1
            "[game_state.t3_player_nerdy.name] now has [game_state.t3_player_nerdy.wisdom] {color=#6684a3}Wisdom{/color}."

    return

label t3_encounter_scenario_level_up_sporty:
    $ sporty_rpg(game_state.t3_player_sporty.get_level_up_phrase())

    $ game_state.t3_player_sporty.level_up()

    menu:
        "Which attribute should be increased?"

        "Style":
            $ game_state.t3_player_sporty.style += 1
            "[game_state.t3_player_sporty.name] now has [game_state.t3_player_sporty.style] {color=#6684a3}Style{/color}."
        "Magic":
            $ game_state.t3_player_sporty.magic += 1
            "[game_state.t3_player_sporty.name] now has [game_state.t3_player_sporty.magic] {color=#6684a3}Magic{/color}."
        "Wisdom":
            $ game_state.t3_player_sporty.wisdom += 1
            "[game_state.t3_player_sporty.name] now has [game_state.t3_player_sporty.wisdom] {color=#6684a3}Wisdom{/color}."

    return

label t3_encounter_scenario_level_up_perfect:
    $ perfect_rpg(game_state.t3_player_sporty.get_level_up_phrase())

    $ game_state.t3_player_perfect.level_up()

    menu:
        "Which attribute should be increased?"

        "Style":
            $ game_state.t3_player_perfect.style += 1
            "[game_state.t3_player_perfect.name] now has [game_state.t3_player_perfect.style] {color=#6684a3}Style{/color}."
        "Magic":
            $ game_state.t3_player_perfect.magic += 1
            "[game_state.t3_player_perfect.name] now has [game_state.t3_player_perfect.magic] {color=#6684a3}Magic{/color}."
        "Wisdom":
            $ game_state.t3_player_perfect.wisdom += 1
            "[game_state.t3_player_perfect.name] now has [game_state.t3_player_perfect.wisdom] {color=#6684a3}Wisdom{/color}."

    return