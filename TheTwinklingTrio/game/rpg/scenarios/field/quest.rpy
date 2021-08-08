define t3_scenario_field_quest_round_0_actions = [
    ActionMenuOption("Approach confidently", CharacterType.Nerdy, AttributeType.Style),
    ActionMenuOption("Cast detection spell (cost 10 Mana)", CharacterType.Nerdy, AttributeType.Magic, 10),
    ActionMenuOption("Analyze from afar", CharacterType.Nerdy, AttributeType.Wisdom),
    ActionMenuOption("Chat it up", CharacterType.Sporty, AttributeType.Style),
    ActionMenuOption("Cast detection spell (cost 10 Mana)", CharacterType.Sporty, AttributeType.Magic, 10),
    ActionMenuOption("Look closely", CharacterType.Sporty, AttributeType.Wisdom),
    ActionMenuOption("Seek an audience", CharacterType.Perfect, AttributeType.Style),
    ActionMenuOption("Cast detection spell (cost 10 Mana)", CharacterType.Perfect, AttributeType.Magic, 10),
    ActionMenuOption("Investigate further", CharacterType.Perfect, AttributeType.Wisdom)
]

label t3_scenario_field_quest:
    nerdy "The meadow was eerily quiet."
    nerdy "No animals, no monsters, no humans. Only silence."

    show nerdy_icon at centerleft
    show sporty_icon at truecenter
    show perfect_icon at centerright
    with dissolve

    nerdy "The party looked around in confusion as they discussed their next move."

    rpg_nerdy "The intell I gathered pointed to this place, but it would seem there's nothing here."

    rpg_sporty "So, what do we do now?"

    rpg_perfect "We should look around for clues. Perhaps we'll find something to point us in the right direction."

    rpg_sporty "Uh... what about that over there? Do you think that's a clue?"

    show other_icon at top with dissolve

    nerdy "A conspicuous training dummy stood alone in the middle of the meadow."

    rpg_sporty "Just a training dummy? Aww, I was hoping for something more exciting..."

    rpg_perfect "Shush. Don't question the narrator."

    rpg_sporty "Hey, don't pretend you weren't hoping for more, too."
    rpg_sporty "Like, why not a unicorn or a dragon? Ya know, something cool and exciting?"

    rpg_perfect "I don't care about seeing a unicorn. I already have the most beautiful, radiant, amazing unicorn there is."

    rpg_sporty "Huh, really? You do?"

    rpg_perfect "Of course. If you can ride a skateboard, certainly I can ride a unicorn."
    rpg_perfect "What about you, [preferences.t3_char_nerdy_name]? Er, I mean, [preferences.t3_rpg_char_nerdy_name]?"

    rpg_nerdy "I live on a giant turtle."

    rpg_sporty "Woah, you two are so cool! I'm gonna have to step up my game."
    rpg_sporty "Oh, I know! My skateboard can be magical with -"

    nerdy "The conspicuous training dummy suddenly made a sound, as if it were awkwardly clearing its wooden throat."

    rpg_other "I'm still here, you know..."

    rpg_sporty "Ack! It makes noise!"

    rpg_perfect "Calm down. It seems like it wants us to interact with it."

    nerdy "In order to interact with objects and people in the world, you have to perform actions."
    nerdy "Remember that the success or failure of an action depends on your attributes, including a strength bonus and weakness penalty."
    nerdy "Some actions may cost Mana, Money, or even Health to perform, so be careful not to run out."
    nerdy "[preferences.t3_rpg_char_nerdy_name] will go first to demonstrate."

    # Make sure nerdy is the current player since this is the tutorial
    $ game_state.t3_current_player = game_state.t3_player_nerdy

    call t3_scenario_player_action_select

    return

label t3_scenario_field_quest_nerdy_style_0_success:
    "Nerdy style success"

    return

label t3_scenario_field_quest_nerdy_style_0_failure:
    "Nerdy style failure"

    return

label t3_scenario_field_quest_nerdy_magic_0_success:
    "Nerdy magic success"

    return

label t3_scenario_field_quest_nerdy_magic_0_failure:
    "Nerdy magic failure"

    return

label t3_scenario_field_quest_nerdy_wisdom_0_success:
    "Nerdy wisdom success"

    return

label t3_scenario_field_quest_nerdy_wisdom_0_failure:
    "Nerdy wisdom failure"

    return

label t3_scenario_field_quest_sporty_style_0_success:
    "Sporty style success"

    return

label t3_scenario_field_quest_sporty_style_0_failure:
    "Sporty style failure"

    return

label t3_scenario_field_quest_sporty_magic_0_success:
    "Sporty magic success"

    return

label t3_scenario_field_quest_sporty_magic_0_failure:
    "Sporty magic failure"

    return

label t3_scenario_field_quest_sporty_wisdom_0_success:
    "Sporty wisdom success"

    return

label t3_scenario_field_quest_sporty_wisdom_0_failure:
    "Sporty wisdom failure"

    return

label t3_scenario_field_quest_perfect_style_0_success:
    "Perfect style success"

    return

label t3_scenario_field_quest_perfect_style_0_failure:
    "Perfect style failure"

    return

label t3_scenario_field_quest_perfect_magic_0_success:
    "Perfect magic success"

    return

label t3_scenario_field_quest_perfect_magic_0_failure:
    "Perfect magic failure"

    return

label t3_scenario_field_quest_perfect_wisdom_0_success:
    "Perfect wisdom success"

    return

label t3_scenario_field_quest_perfect_wisdom_0_failure:
    "Perfect wisdom failure"

    return