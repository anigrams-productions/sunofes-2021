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

label t3_scenario_show_trio:
    show nerdy_icon at centerleft
    show sporty_icon at truecenter
    show perfect_icon at centerright
    with dissolve

    return

label t3_scenario_hide_trio:
    hide other_icon
    hide nerdy_icon
    hide sporty_icon
    hide perfect_icon
    with dissolve

    return

label t3_scenario_player_action_select:
    $ original_player = game_state.t3_current_player
    $ current_action_menu = []

    while game_state.t3_current_scenario.keep_going:
        call t3_scenario_hide_dice_roll from _call_t3_scenario_hide_dice_roll

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

            "{color=#6684a3}[game_state.t3_current_player.name]{/color} has {color=#6684a3}[game_state.t3_current_player.health] Health{/color}, {color=#6684a3}[game_state.t3_current_player.mana] Mana{/color}, and {color=#6684a3}[game_state.t3_current_player.money] Money{/color} remaining."

            # TODO: Implement ability to enable automatic action selection
            $ game_state.get_action_menu(current_action_menu)

            # subtract health, mana, and money costs
            $ game_state.t3_current_player.update_health(game_state.t3_current_action.health_cost * -1)
            $ game_state.t3_current_player.update_mana(game_state.t3_current_action.mana_cost * -1)
            $ game_state.t3_current_player.update_money(game_state.t3_current_action.money_cost * -1)

            call t3_scenario_dice_roll from _call_t3_scenario_dice_roll

            $ game_state.t3_current_action.attribute_points_required = game_state.t3_total_dice_roll

            "{color=#6684a3}[game_state.t3_current_player.name]{/color} rolled {color=#6684a3}[game_state.t3_total_dice_roll]{/color}."

            $ current_attribute_amount = getattr(game_state.t3_current_player, game_state.t3_current_action.action_type)
            "{color=#6684a3}[game_state.t3_current_player.name]{/color} has {color=#6684a3}[current_attribute_amount] [game_state.t3_current_action.action_type]{/color}."

            if game_state.t3_current_player.strength == game_state.t3_current_action.action_type:
                $ current_attribute_amount += 1
                "A +1 Strength bonus is applied, increasing {color=#6684a3}[game_state.t3_current_player.name]{/color}'s {color=#6684a3}[game_state.t3_current_action.action_type]{/color} to [current_attribute_amount]."

            if game_state.t3_current_player.weakness == game_state.t3_current_action.action_type:
                $ current_attribute_amount -= 1
                "A -1 Weakness pernalty is applied, decreasing {color=#6684a3}[game_state.t3_current_player.name]{/color}'s {color=#6684a3}[game_state.t3_current_action.action_type]{/color} to [current_attribute_amount]."

            $ game_state.t3_action_successful = game_state.t3_current_action.is_success()

            if game_state.t3_action_successful:
                "The check was successful."
            else:
                "The check was not successful."

            call t3_scenario_hide_dice_roll from _call_t3_scenario_hide_dice_roll_1

            call expression game_state.t3_current_action.return_action_result() from _call_expression_6

            $ experience_gained = game_state.t3_current_player.gain_experience(game_state.t3_action_successful)

            "{color=#6684a3}[game_state.t3_current_player.name]{/color} gained {color=#6684a3}[experience_gained]{/color} experience points."

            $ game_state.t3_current_player = game_state.t3_current_encounter.get_next_player()

            # If we've looped through everyone and gotten back to the beginning, increase round count
            if game_state.t3_current_player == original_player:
                $ game_state.t3_current_action_round += 1

    return
