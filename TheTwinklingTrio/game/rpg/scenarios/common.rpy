label t3_scenario_dice_roll:
    $ game_state.roll_dice()

    show dice_1 at diceleft onlayer dice with dissolve
    show dice_2 at dicecenter onlayer dice with dissolve
    show dice_3 at diceright onlayer dice with dissolve

    return

label t3_scenario_hide_dice_roll:
    hide dice_1 onlayer dice
    hide dice_2 onlayer dice
    hide dice_3 onlayer dice

    return

label t3_scenario_player_action_select:
    $ original_player = game_state.t3_current_player
    $ current_action_menu = []

    while game_state.t3_current_scenario.keep_going:
        call t3_scenario_hide_dice_roll

        # Try to grab actions for the this round - if there aren't any, we must be done
        python:
            try:
                current_action_menu = renpy.python.py_eval(game_state.t3_current_scenario.script + "_round_" + str(game_state.t3_current_action_round) + "_actions")
            except:
                game_state.t3_current_scenario.keep_going = False

        if game_state.t3_current_scenario.keep_going:

            if game_state.t3_current_player.character_type == CharacterType.Nerdy:
                $ rpg_nerdy(game_state.t3_current_player.get_action_start_phrase())
            elif game_state.t3_current_player.character_type == CharacterType.Sporty:
                $ rpg_sporty(game_state.t3_current_player.get_action_start_phrase())
            elif game_state.t3_current_player.character_type == CharacterType.Perfect:
                $ rpg_perfect(game_state.t3_current_player.get_action_start_phrase())

            nerdy "[game_state.t3_current_player.name] has [game_state.t3_current_player.health] Health, [game_state.t3_current_player.mana] Mana, and [game_state.t3_current_player.money] Money remaining."

            # TODO: Implement ability to enable automatic action selection
            $ game_state.get_action_menu(current_action_menu)

            call t3_scenario_dice_roll

            $ game_state.t3_current_action.attribute_points_required = game_state.t3_total_dice_roll

            nerdy "[game_state.t3_current_player.name] rolled [game_state.t3_total_dice_roll]."

            $ current_attribute_amount = getattr(game_state.t3_current_player, game_state.t3_current_action.action_type)
            nerdy "[game_state.t3_current_player.name] has [current_attribute_amount] [game_state.t3_current_action.action_type]."

            if game_state.t3_current_player.strength == game_state.t3_current_action.action_type:
                $ current_attribute_amount += 1
                nerdy "A +1 Strength bonus is applied, increasing [game_state.t3_current_player.name]'s [game_state.t3_current_action.action_type] to [current_attribute_amount]."

            if game_state.t3_current_player.weakness == game_state.t3_current_action.action_type:
                $ current_attribute_amount -= 1
                nerdy "A -1 Weakness pernalty is applied, decreasing [game_state.t3_current_player.name]'s [game_state.t3_current_action.action_type] to [current_attribute_amount]."

            $ game_state.t3_action_successful = game_state.t3_current_action.is_success()

            if game_state.t3_action_successful:
                nerdy "The action was successful."
            else:
                nerdy "The action was not successful."

            call expression game_state.t3_current_action.return_action_result()

            $ experience_gained = game_state.t3_current_player.gain_experience(game_state.t3_action_successful)

            nerdy "[game_state.t3_current_player.name] gained [experience_gained] experience points."

            $ game_state.t3_current_player = game_state.t3_current_encounter.get_next_player()

            # If we've looped through everyone and gotten back to the beginning, increase round count
            if game_state.t3_current_player == original_player:
                $ game_state.t3_current_action_round += 1

    return
