label encounter_scenarios_play:
    # start by meeting the quest giver
    $ current_character_name = rpg_players[rpg_current_player].name
    "This is the quest scenario. Current player is [current_character_name]."
    call expression rpg_current_encounter.scenario_quest.script
    call encounter_scenario_end

    # begin the random scenarios...
    "There should be [rpg_current_encounter.number_of_scenarios] scenarios."
    $ scenario_count = 1
    while scenario_count <= rpg_current_encounter.number_of_scenarios:
        $ current_character_name = rpg_players[rpg_current_player].name
        "This is scenario [scenario_count] out of [rpg_current_encounter.number_of_scenarios]. Current player is [current_character_name]."
        call encounter_scenario_select

        $ scenario_count += 1

    # meet the boss
    $ current_character_name = rpg_players[rpg_current_player].name
    "This is the boss scenario. Current player is [current_character_name]."
    call expression rpg_current_encounter.scenario_boss.script
    call encounter_scenario_end

    # finally, reach the objective
    $ current_character_name = rpg_players[rpg_current_player].name
    "This is the final scenario. Current player is [current_character_name]."
    call expression rpg_current_encounter.scenario_special.script
    call encounter_scenario_end
        
    jump expression "encounter_" + rpg_current_encounter.theme + "_success"

label encounter_scenario_select:
    python:
        rpg_scenario_options = rpg_current_encounter.pick_random_scenarios()
        rpg_scenario_menu_options = []

        for option in rpg_scenario_options:
            rpg_scenario_menu_options.append((option.menu_label, option))

        narrator("Where should we go next?", interact=False)
        rpg_selected_scenario = renpy.display_menu(rpg_scenario_menu_options)

        rpg_current_encounter.select_scenario(rpg_selected_scenario)

    call expression rpg_selected_scenario.script

    call encounter_scenario_end
    return

label encounter_scenario_end:
    # check if anyone's still alive
    $ remaining_players = rpg_current_encounter.get_active_players()

    if len(remaining_players) <= 0:
        jump expression "encounter_" + rpg_current_encounter.theme + "_failure"

    # if we still have active players, check if they can level up
    $ active_player_count = 0
    while active_player_count < len(remaining_players):
        if remaining_players[active_player_count].can_level_up():
            call encounter_scenario_level_up
        
        $ active_player_count += 1

    $ rpg_current_player = rpg_current_encounter.get_next_player()

    return

label encounter_scenario_level_up:
    if rpg_current_encounter.current_player.character_type == CharacterType.Nerdy:
        nerdy "I leveled up!"
    elif rpg_current_encounter.current_player.character_type == CharacterType.Sporty:
        sporty "I leveled up!"
    elif rpg_current_encounter.current_player.character_type == CharacterType.Perfect:
        perfect "I leveled up!"

    $ rpg_current_encounter.current_player.level_up()

    return