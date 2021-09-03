define t3_scenario_merchant_health_items = ["Cheeseburger", "Hot Dog", "Ice Cream", "House Salad", "French Fries"]
define t3_scenario_merchant_mana_items = ["Milkshake", "Smoothie", "Coffee", "Iced Tea", "Soda"]

label t3_scenario_merchant:
    $ game_state.t3_current_player.merchants_met.append(game_state.t3_current_scenario.current_entity)
    $ health_item_of_choice = renpy.random.choice(t3_scenario_merchant_health_items).capitalize()
    $ mana_item_of_choice = renpy.random.choice(t3_scenario_merchant_mana_items).capitalize()

    "A merchant has set up shop, shelves stocked and ready to peddle to any passersby."

    call t3_scenario_show_trio from _call_t3_scenario_show_trio_5

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

        "[game_state.t3_current_player.name] has [game_state.t3_current_player.health] {color=#6684a3}Health{/color}, [game_state.t3_current_player.mana] {color=#6684a3}Mana{/color}, and [game_state.t3_current_player.money] {color=#6684a3}Money{/color} remaining."

        menu:
            "What should we buy?"

            # TODO: Create Item class with name, type, cost, and how much it adds/restores/subtracts (depending on type) and use that here instead
            "[health_item_of_choice] (cost [preferences.t3_rpg_shop_health_potion_cost] Money)":
                rpg_other "Excellent choice. This food should restore [preferences.t3_rpg_shop_health_potion_amt] {color=#6684a3}Health{/color}."

                $ game_state.t3_current_player.update_money(preferences.t3_rpg_shop_health_potion_cost * -1)
                $ game_state.t3_current_player.update_health(preferences.t3_rpg_shop_health_potion_amt)
                $ game_state.t3_current_player.merchant_items_purchased.append(health_item_of_choice)

                "[game_state.t3_current_player.name] now has [game_state.t3_current_player.health] {color=#6684a3}Health{/color} and [game_state.t3_current_player.money] {color=#6684a3}Money{/color}."

            "[mana_item_of_choice] (cost [preferences.t3_rpg_shop_mana_potion_cost] Money)":
                rpg_other "You have a good eye. This drink should restore [preferences.t3_rpg_shop_mana_potion_amt] {color=#6684a3}Mana{/color}."

                $ game_state.t3_current_player.update_money(preferences.t3_rpg_shop_mana_potion_cost * -1)
                $ game_state.t3_current_player.update_mana(preferences.t3_rpg_shop_mana_potion_amt)
                $ game_state.t3_current_player.merchant_items_purchased.append(mana_item_of_choice)

                "[game_state.t3_current_player.name] now has [game_state.t3_current_player.mana] {color=#6684a3}Mana{/color} and [game_state.t3_current_player.money] {color=#6684a3}Money{/color}."

            "Nothing":
                rpg_other "Oh, that's a shame."

        $ game_state.t3_current_player = game_state.t3_current_encounter.get_next_player()

        $ player_count_for_shop += 1

    rpg_other "Thank you and come again."

    call t3_scenario_hide_trio from _call_t3_scenario_hide_trio_3

    return