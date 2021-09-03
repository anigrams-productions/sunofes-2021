label t3_scenario_campfire:
    call t3_scenario_show_trio from _call_t3_scenario_show_trio_1

    "The weary party came across an inviting campfire."
    "Its soothing flames seemed like they could cure all ills and restore the party's strength."

    if game_state.t3_current_player.character_type == CharacterType.Nerdy:
        rpg_nerdy "This seems like a good place to make camp."
    elif game_state.t3_current_player.character_type == CharacterType.Sporty:
        rpg_sporty "Ah, finally a spot to relax. Let's kick back for a bit, yeah?"
    elif game_state.t3_current_player.character_type == CharacterType.Perfect:
        rpg_perfect "Oh my, what a cute little camp. Shall we take a break?"

    menu:
        "What should we do?"

        "Rest and heal":
            $ game_state.t3_current_player.campfires_used.append(game_state.t3_current_scenario)
            $ party_member_count = 0

            while party_member_count < len(game_state.t3_remaining_players):
                $ game_state.t3_remaining_players[party_member_count].reset_health()
                $ game_state.t3_remaining_players[party_member_count].reset_mana()
                $ party_member_count += 1
            
            "The party sat a while and rested, making small talk as they huddled around the fire."
            "After some sleep and good conversation, they felt completely rested and ready to take on the challenges awaiting them."
        "Continue forward":
            "Despite the allure of the campfire, the party decided to push forward, confident in their ability to take on the dangers ahead."

    call t3_scenario_hide_trio from _call_t3_scenario_hide_trio_1

    return

label t3_scenario_treasure:
    call t3_scenario_show_trio from _call_t3_scenario_show_trio_2

    $ treasure_reward = renpy.random.randint(1,1000)

    "As the party entered an area seemingly free of monsters, [game_state.t3_current_player.name] noticed something shining nearby."

    if game_state.t3_current_player.character_type == CharacterType.Nerdy:
        rpg_nerdy "There seems to be a treasure chest nearby. I'll check it."
    elif game_state.t3_current_player.character_type == CharacterType.Sporty:
        rpg_sporty "Woah, is that a treasure chest? Sweet! Lemme see what's in it!"
    elif game_state.t3_current_player.character_type == CharacterType.Perfect:
        rpg_perfect "A treasure chest, hmm? I'll gladly help myself, then."

    "[game_state.t3_current_player.name] found [treasure_reward] Money."

    $ game_state.t3_current_player.money += treasure_reward
    $ game_state.t3_current_player.treasure_found.append(game_state.t3_current_scenario)
    $ game_state.t3_current_player.money_found += treasure_reward

    call t3_scenario_hide_trio from _call_t3_scenario_hide_trio_2

    return

label t3_scenario_puzzle:
    "You discovered a puzzle."

    return

label t3_scenario_trap:
    "You discovered a trap."

    return