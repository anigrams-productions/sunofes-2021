label t3_scenario_merchant:
    $ game_state.t3_current_player.merchants_met.append(game_state.t3_current_scenario)

    "A merchant has set up shop, shelves stocked and ready to peddle to any passersby."

    show nerdy_icon at centerleft
    show sporty_icon at truecenter
    show perfect_icon at centerright
    with dissolve

    if game_state.t3_current_player.character_type == CharacterType.Nerdy:
        rpg_nerdy "Looks like a good place to shop."
    elif game_state.t3_current_player.character_type == CharacterType.Sporty:
        rpg_sporty "Ooh, I love shopping! I wonder what kinda neat things are for sale?"
    elif game_state.t3_current_player.character_type == CharacterType.Perfect:
        rpg_perfect "We should stock up on supplies while we can."

    show other_icon at top with dissolve

    rpg_other "Hello, how may I help you?"

    # loop through each (active) player and give them a menu of items to buy

    $ player_count_for_shop = 0
    $ original_player = game_state.t3_current_player

    while player_count_for_shop < len(game_state.t3_remaining_players):

        if game_state.t3_current_player.character_type == CharacterType.Nerdy:
            rpg_nerdy "What I should buy?"
        elif game_state.t3_current_player.character_type == CharacterType.Sporty:
            rpg_sporty "Everything looks useful! What should I buy?"
        elif game_state.t3_current_player.character_type == CharacterType.Perfect:
            rpg_perfect "I wonder what I should buy."

        "[game_state.t3_current_player.name] has [game_state.t3_current_player.health] Health, [game_state.t3_current_player.mana] Mana, and [game_state.t3_current_player.money] Money remaining."

        menu:
            "What should we buy?"

            "Health Potion (cost [preferences.t3_rpg_shop_health_potion_cost] Money)":
                rpg_other "Excellent choice. This potion should restore [preferences.t3_rpg_shop_health_potion_amt] Health."

                $ game_state.t3_current_player.update_money(preferences.t3_rpg_shop_health_potion_cost * -1)
                $ game_state.t3_current_player.update_health(preferences.t3_rpg_shop_health_potion_amt)

                "[game_state.t3_current_player.name] now has [game_state.t3_current_player.health] Health and [game_state.t3_current_player.money] Money."

            "Mana Potion (cost [preferences.t3_rpg_shop_mana_potion_cost] Money)":
                rpg_other "You have a good eye. This potion should restore [preferences.t3_rpg_shop_mana_potion_amt] Mana."

                $ game_state.t3_current_player.update_money(preferences.t3_rpg_shop_mana_potion_cost * -1)
                $ game_state.t3_current_player.update_mana(preferences.t3_rpg_shop_mana_potion_amt)

                "[game_state.t3_current_player.name] now has [game_state.t3_current_player.mana] Mana and [game_state.t3_current_player.money] Money."

            "Nothing":
                rpg_other "Oh, that's a shame."

        $ game_state.t3_current_player = game_state.t3_current_encounter.get_next_player()

        $ player_count_for_shop += 1

    rpg_other "Thank you and come again."

    hide other_icon
    hide nerdy_icon
    hide sporty_icon
    hide perfect_icon
    with dissolve

    return