label t3_encounter_scenarios_play:
    ## Start by meeting the quest giver
    # "This is the quest scenario. Current player is [game_state.t3_current_player.name]."
    $ game_state.t3_current_scenario = game_state.t3_current_encounter.scenario_quest
    call expression game_state.t3_current_encounter.scenario_quest.script
    call t3_encounter_scenario_end

    ## Begin the random scenarios...
    # "There should be [game_state.t3_current_encounter.number_of_scenarios] scenarios."
    $ scenario_count = 1
    while scenario_count <= game_state.t3_current_encounter.number_of_scenarios:
        # "This is scenario [scenario_count] out of [game_state.t3_current_encounter.number_of_scenarios]. Current player is [game_state.t3_current_player.name]."
        call t3_encounter_scenario_select

        $ scenario_count += 1

    ## Meet the boss
    # "This is the boss scenario. Current player is [game_state.t3_current_player.name]."
    $ game_state.t3_current_scenario = game_state.t3_current_encounter.scenario_boss
    call expression game_state.t3_current_encounter.scenario_boss.script
    call t3_encounter_scenario_end

    ## Finally, reach the objective
    # "This is the final scenario. Current player is [game_state.t3_current_player.name]."
    $ game_state.t3_current_scenario = game_state.t3_current_encounter.scenario_special
    call expression game_state.t3_current_encounter.scenario_special.script
    call t3_encounter_scenario_end
        
    jump expression "t3_encounter_" + game_state.t3_current_encounter.theme + "_success"

label t3_encounter_scenario_select:
    $ game_state.get_scenario_menu()

    call expression game_state.t3_current_scenario.script

    call t3_encounter_scenario_end
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

    $ game_state.t3_current_player = game_state.t3_current_encounter.get_next_player()

    return

label t3_encounter_scenario_level_up_nerdy:
    $ nerdy_rpg(game_state.t3_player_sporty.get_level_up_phrase())

    $ game_state.t3_player_nerdy.level_up()

    menu:
        "Which attribute should be increased?"

        "Style":
            $ game_state.t3_player_nerdy.style += 1
            nerdy "[game_state.t3_player_nerdy.name] now has [game_state.t3_player_nerdy.style] Style."
        "Magic":
            $ game_state.t3_player_nerdy.magic += 1
            nerdy "[game_state.t3_player_nerdy.name] now has [game_state.t3_player_nerdy.magic] Magic."
        "Wisdom":
            $ game_state.t3_player_nerdy.wisdom += 1
            nerdy "[game_state.t3_player_nerdy.name] now has [game_state.t3_player_nerdy.wisdom] Wisdom."

    return

label t3_encounter_scenario_level_up_sporty:
    $ sporty_rpg(game_state.t3_player_sporty.get_level_up_phrase())

    $ game_state.t3_player_sporty.level_up()

    menu:
        "Which attribute should be increased?"

        "Style":
            $ game_state.t3_player_sporty.style += 1
            nerdy "[game_state.t3_player_sporty.name] now has [game_state.t3_player_sporty.style] Style."
        "Magic":
            $ game_state.t3_player_sporty.magic += 1
            nerdy "[game_state.t3_player_sporty.name] now has [game_state.t3_player_sporty.magic] Magic."
        "Wisdom":
            $ game_state.t3_player_sporty.wisdom += 1
            nerdy "[game_state.t3_player_sporty.name] now has [game_state.t3_player_sporty.wisdom] Wisdom."

    return

label t3_encounter_scenario_level_up_perfect:
    $ perfect_rpg(game_state.t3_player_sporty.get_level_up_phrase())

    $ game_state.t3_player_perfect.level_up()

    menu:
        "Which attribute should be increased?"

        "Style":
            $ game_state.t3_player_perfect.style += 1
            nerdy "[game_state.t3_player_perfect.name] now has [game_state.t3_player_perfect.style] Style."
        "Magic":
            $ game_state.t3_player_perfect.magic += 1
            nerdy "[game_state.t3_player_perfect.name] now has [game_state.t3_player_perfect.magic] Magic."
        "Wisdom":
            $ game_state.t3_player_perfect.wisdom += 1
            nerdy "[game_state.t3_player_perfect.name] now has [game_state.t3_player_perfect.wisdom] Wisdom."

    return