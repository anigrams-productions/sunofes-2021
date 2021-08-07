define t3_scenario_field_quest_round_0_actions = [
    ActionMenuOption("Approach confidently", CharacterType.Nerdy, AttributeType.Style),
    ActionMenuOption("Cast detection spell (cost 1 Mana)", CharacterType.Nerdy, AttributeType.Magic, 1),
    ActionMenuOption("Analyze from afar", CharacterType.Nerdy, AttributeType.Wisdom),
    ActionMenuOption("Chat it up", CharacterType.Sporty, AttributeType.Style),
    ActionMenuOption("Cast detection spell (cost 1 Mana)", CharacterType.Sporty, AttributeType.Magic, 1),
    ActionMenuOption("Look closely", CharacterType.Sporty, AttributeType.Wisdom),
    ActionMenuOption("Seek an audience", CharacterType.Perfect, AttributeType.Style),
    ActionMenuOption("Cast detection spell (cost 1 Mana)", CharacterType.Perfect, AttributeType.Magic, 1),
    ActionMenuOption("Investigate further", CharacterType.Perfect, AttributeType.Wisdom)
]

label t3_scenario_field_quest:
    # nerdy "The meadow was eerily quiet."
    # nerdy "No animals, no monsters, no humans. Only silence."

    # show nerdy icon at centerleft with dissolve

    # rpg_nerdy "The intell I gathered pointed to this place, but it would seem there's nothing here."

    # hide nerdy icon
    # show sporty icon at truecenter with dissolve

    # rpg_sporty "So what do we do now?"

    # hide sporty icon
    # show perfect icon at centerright with dissolve

    # rpg_perfect "We should look around for clues. Perhaps we'll find something."

    # hide perfect icon
    # show sporty icon at truecenter with dissolve

    # rpg_sporty "Uh... do you think that thing's a clue?"

    # hide sporty icon
    # show npc field quest at top with dissolve

    # nerdy "A conspicuous training dummy stood alone in the middle of the meadow."
    # nerdy "In order to interact with objects and people in the world, we have to perform actions."
    # nerdy "Remember that the success or failure of an action depends on your attributes, including a strength bonus and weakness penalty."

    # Make sure nerdy is the current player since this is the tutorial
    $ game_state.t3_current_player = game_state.t3_player_nerdy

    call t3_scenario_player_action_select

    return

label t3_scenario_field_quest_nerdy_start:
    hide sporty icon
    hide perfect icon

    show nerdy icon at centerleft with dissolve
    
    rpg_nerdy "It's my turn."

    return

label t3_scenario_field_quest_nerdy_style_0_success:
    $ game_state.t3_action_successful = True
    nerdy "The action was successful."

    return

label t3_scenario_field_quest_nerdy_style_0_failure:
    $ game_state.t3_action_successful = False
    nerdy "The action was not successful."

    return

label t3_scenario_field_quest_nerdy_magic_0_success:
    $ game_state.t3_action_successful = True
    nerdy "The action was successful."

    return

label t3_scenario_field_quest_nerdy_magic_0_failure:
    $ game_state.t3_action_successful = False
    nerdy "The action was not successful."
    return

label t3_scenario_field_quest_nerdy_wisdom_0_success:
    $ game_state.t3_action_successful = True
    nerdy "The action was successful."

    return

label t3_scenario_field_quest_nerdy_wisdom_0_failure:
    $ game_state.t3_action_successful = False
    nerdy "The action was not successful."
    return

label t3_scenario_field_quest_sporty_start:
    hide nerdy icon
    hide perfect icon

    show sporty icon at truecenter with dissolve
    
    rpg_sporty "Sweet, it's time for me to shine!"

    return

label t3_scenario_field_quest_sporty_style_0_success:
    $ game_state.t3_action_successful = True
    nerdy "The action was successful."

    return

label t3_scenario_field_quest_sporty_style_0_failure:
    $ game_state.t3_action_successful = False
    nerdy "The action was not successful."

    return

label t3_scenario_field_quest_sporty_magic_0_success:
    $ game_state.t3_action_successful = True
    nerdy "The action was successful."

    return

label t3_scenario_field_quest_sporty_magic_0_failure:
    $ game_state.t3_action_successful = False
    nerdy "The action was not successful."
    return

label t3_scenario_field_quest_sporty_wisdom_0_success:
    $ game_state.t3_action_successful = True
    nerdy "The action was successful."

    return

label t3_scenario_field_quest_sporty_wisdom_0_failure:
    $ game_state.t3_action_successful = False
    nerdy "The action was not successful."
    return

label t3_scenario_field_quest_perfect_start:
    hide nerdy icon
    hide sporty icon

    show perfect icon at centerright with dissolve
    
    rpg_perfect "I'll show you how it's done."

    return

label t3_scenario_field_quest_perfect_style_0_success:
    $ game_state.t3_action_successful = True
    nerdy "The action was successful."

    return

label t3_scenario_field_quest_perfect_style_0_failure:
    $ game_state.t3_action_successful = False
    nerdy "The action was not successful."

    return

label t3_scenario_field_quest_perfect_magic_0_success:
    $ game_state.t3_action_successful = True
    nerdy "The action was successful."

    return

label t3_scenario_field_quest_perfect_magic_0_failure:
    $ game_state.t3_action_successful = False
    nerdy "The action was not successful."
    return

label t3_scenario_field_quest_perfect_wisdom_0_success:
    $ game_state.t3_action_successful = True
    nerdy "The action was successful."

    return

label t3_scenario_field_quest_perfect_wisdom_0_failure:
    $ game_state.t3_action_successful = False
    nerdy "The action was not successful."
    return