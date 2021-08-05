label t3_encounter_scenarios_play:
    # start by meeting the quest giver
    "This is the quest scenario. Current player is [game_state.t3_current_player.name]."
    call expression game_state.t3_current_encounter.scenario_quest.script
    call t3_encounter_scenario_end

    # begin the random scenarios...
    "There should be [game_state.t3_current_encounter.number_of_scenarios] scenarios."
    $ scenario_count = 1
    while scenario_count <= game_state.t3_current_encounter.number_of_scenarios:
        "This is scenario [scenario_count] out of [game_state.t3_current_encounter.number_of_scenarios]. Current player is [game_state.t3_current_player.name]."
        call t3_encounter_scenario_select

        $ scenario_count += 1

    # meet the boss
    "This is the boss scenario. Current player is [game_state.t3_current_player.name]."
    call expression game_state.t3_current_encounter.scenario_boss.script
    call t3_encounter_scenario_end

    # finally, reach the objective
    "This is the final scenario. Current player is [game_state.t3_current_player.name]."
    call expression game_state.t3_current_encounter.scenario_special.script
    call t3_encounter_scenario_end
        
    jump expression "t3_encounter_" + game_state.t3_current_encounter.theme + "_success"

label t3_encounter_scenario_select:
    $ game_state.get_scenario_menu()

    call expression game_state.t3_current_scenario.script

    call t3_encounter_scenario_end
    return

label t3_encounter_scenario_end:
    # check if anyone's still alive
    $ game_state.update_remaining_players()

    if len(game_state.t3_remaining_players) <= 0:
        jump expression "t3_encounter_" + game_state.t3_current_encounter.theme + "_failure"

    # if we still have active players, check if they can level up
    $ active_player_count = 0
    while active_player_count < len(game_state.t3_remaining_players):
        if game_state.t3_remaining_players[active_player_count].can_level_up():
            call t3_encounter_scenario_level_up
        
        $ active_player_count += 1

    $ game_state.t3_current_player = game_state.t3_current_encounter.get_next_player()

    return

label t3_encounter_scenario_level_up:
    if game_state.t3_current_encounter.current_player.character_type == CharacterType.Nerdy:
        nerdy "I leveled up!"
    elif game_state.t3_current_encounter.current_player.character_type == CharacterType.Sporty:
        sporty "I leveled up!"
    elif game_state.t3_current_encounter.current_player.character_type == CharacterType.Perfect:
        perfect "I leveled up!"

    $ game_state.t3_current_encounter.current_player.level_up()

    return