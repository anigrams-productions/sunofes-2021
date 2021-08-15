define t3_scenario_enemy_player_actions = [
    ActionMenuOption("(Style) Hurl Insult", CharacterType.Nerdy, AttributeType.Style),
    ActionMenuOption("(Magic) Heal allies (cost 20 Mana)", CharacterType.Nerdy, AttributeType.Magic, 20),
    ActionMenuOption("(Wisdom) Analyze", CharacterType.Nerdy, AttributeType.Wisdom),
    ActionMenuOption("(Style) Perform trick", CharacterType.Sporty, AttributeType.Style),
    ActionMenuOption("(Magic) Summon flames (cost 20 Mana)", CharacterType.Sporty, AttributeType.Magic, 20),
    ActionMenuOption("(Wisdom) Play dumb", CharacterType.Sporty, AttributeType.Wisdom),
    ActionMenuOption("(Style) Summon familiar", CharacterType.Perfect, AttributeType.Style),
    ActionMenuOption("(Magic) Cast tidal wave (cost 20 Mana)", CharacterType.Perfect, AttributeType.Magic, 20),
    ActionMenuOption("(Wisdom) Use charm", CharacterType.Perfect, AttributeType.Wisdom)
]

label t3_scenario_enemy_end:
    $ game_state.t3_current_player.enemies_met.append(game_state.t3_current_scenario.current_entity)

    call t3_scenario_hide_trio

    return

label t3_scenario_enemy_dragon:
    show other_icon at top with dissolve

    "A wild dragon appeared!"

    call t3_scenario_show_trio

    if game_state.t3_current_player.character_type == CharacterType.Nerdy:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_nerdy "Oh no. Another dragon."
        else:
            rpg_nerdy "Oh no. It's a dragon."

            rpg_sporty "You could act a bit more surprised, you know."
            rpg_sporty "Like this: Oh no! It's a dragon! WE'RE ALL GONNA DIE!!"

            rpg_nerdy "Too much effort."

    elif game_state.t3_current_player.character_type == CharacterType.Sporty:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_sporty "Nice! We've got another dragon to fight."
        else:
            rpg_sporty "Woah, a dragon? So cool!!"

            rpg_perfect "You'll have to admire it later. Right now, it looks like it wants to eat us."

            rpg_sporty "Good point. Okay, let's do this!"

    elif game_state.t3_current_player.character_type == CharacterType.Perfect:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_perfect "Another dragon? They must not be as rare as I thought."
        else:
            rpg_perfect "This will be a tough battle. Let's keep our wits about us."

            rpg_sporty "Yeah, let's do this! You better watch out, dragon."

            rpg_perfect "Time to fight."

    call t3_scenario_enemy_end

    return

label t3_scenario_enemy_orc:
    show other_icon at top with dissolve

    "A wild orc appeared!"

    call t3_scenario_show_trio

    if game_state.t3_current_player.character_type == CharacterType.Nerdy:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_nerdy "Oh no. It's another orc."
        else:
            rpg_nerdy "Oh no. It's an orc."

            rpg_sporty "...Is that your response to everything?"

            rpg_nerdy "Yes."

    elif game_state.t3_current_player.character_type == CharacterType.Sporty:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_sporty "Another orc to fight, huh?"
            rpg_sporty "I'll, uh, try to be nicer this time, I guess."
        else:
            rpg_sporty "Wow. Super ugly, ain't he?"

            rpg_perfect "Now, [preferences.t3_rpg_char_sporty_name], be nice."
            rpg_perfect "And also, don't assume the poor orc's gender."

            rpg_sporty "Yes, yes, you're right. Sorry. Can we start the fight now?"
        
    elif game_state.t3_current_player.character_type == CharacterType.Perfect:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_perfect "Oh, another orc?"
            rpg_perfect "Sorry for bothering you. I promise we'll be out of your way shortly."
        else:
            rpg_perfect "Orcs are intelligent creatures. We may be able to reason with them."

            rpg_sporty "Are you sure? They don't seem all that smart to me."
            rpg_sporty "After all, they were dumb enough to pick a fight with us."

            rpg_perfect "We can't blame them for defending their territory."
            rpg_perfect "But sadly, it looks like we'll have to fight all the same."

    call t3_scenario_enemy_end

    return

label t3_scenario_enemy_fish:
    show other_icon at top with dissolve

    "A wild fish appeared!"

    call t3_scenario_show_trio

    if game_state.t3_current_player.character_type == CharacterType.Nerdy:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_nerdy "Gross. It's another fish."
        else:
            rpg_nerdy "Gross. It's a fish."

            rpg_perfect "Oh my, this is surprising. Do you not like fish, [preferences.t3_rpg_char_nerdy_name]?"

            rpg_nerdy "Not really."

    elif game_state.t3_current_player.character_type == CharacterType.Sporty:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_sporty "Uh oh, looks like another one of those magic fish out of water."
        else:
            rpg_sporty "What the heck? How can that fish even survive out here?"

            rpg_perfect "We don't know much about this world. Perhaps fish don't need water here."
            rpg_perfect "Do you know how the fish is surviving without water, [preferences.t3_rpg_char_nerdy_name]?"

            rpg_nerdy "Magic."

            rpg_perfect "Well, there you go, [preferences.t3_rpg_char_sporty_name]. It's all thanks to the wonders of magic."

            rpg_sporty "Magic or not, time to put this fish out of its misery."

    elif game_state.t3_current_player.character_type == CharacterType.Perfect:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_perfect "Another fish, hm? Fried fish still sounds so good..."
        else:
            rpg_perfect "I suddenly have a craving for fried fish."
            rpg_perfect "Perhaps I can cook some up for dinner after this. Doesn't that sound delicious?"

            rpg_sporty "Hey, you probably shouldn't talk about eating fish when there's one, like, right there."
            rpg_sporty "What if you end up eating one of its friends or family members or something?"

            rpg_perfect "Do you think the fish is intelligent enough to know I'm talking about eating its friends?"
            rpg_perfect "Fine, I suppose I'll refrain from talking about cooking fish in front of it."

    call t3_scenario_enemy_end

    return

label t3_scenario_enemy_reptile:
    show other_icon at top with dissolve

    "A wild reptile appeared!"

    call t3_scenario_show_trio

    if game_state.t3_current_player.character_type == CharacterType.Nerdy:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_nerdy ""
        else:
            rpg_nerdy ""

    elif game_state.t3_current_player.character_type == CharacterType.Sporty:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_sporty ""
        else:
            rpg_sporty ""

    elif game_state.t3_current_player.character_type == CharacterType.Perfect:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_perfect ""
        else:
            rpg_perfect ""

    call t3_scenario_enemy_end

    return

label t3_scenario_enemy_mammal:
    show other_icon at top with dissolve

    "A wild mammal appeared!"

    call t3_scenario_show_trio

    if game_state.t3_current_player.character_type == CharacterType.Nerdy:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_nerdy ""
        else:
            rpg_nerdy ""

    elif game_state.t3_current_player.character_type == CharacterType.Sporty:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_sporty ""
        else:
            rpg_sporty ""

    elif game_state.t3_current_player.character_type == CharacterType.Perfect:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_perfect ""
        else:
            rpg_perfect ""

    call t3_scenario_enemy_end

    return

label t3_scenario_enemy_bird:
    show other_icon at top with dissolve

    "A wild bird appeared!"

    call t3_scenario_show_trio

    if game_state.t3_current_player.character_type == CharacterType.Nerdy:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_nerdy ""
        else:
            rpg_nerdy ""

    elif game_state.t3_current_player.character_type == CharacterType.Sporty:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_sporty ""
        else:
            rpg_sporty ""

    elif game_state.t3_current_player.character_type == CharacterType.Perfect:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_perfect ""
        else:
            rpg_perfect ""

    call t3_scenario_enemy_end

    return

label t3_scenario_enemy_insect:
    show other_icon at top with dissolve

    "A wild insect appeared!"

    call t3_scenario_show_trio

    if game_state.t3_current_player.character_type == CharacterType.Nerdy:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_nerdy ""
        else:
            rpg_nerdy ""

    elif game_state.t3_current_player.character_type == CharacterType.Sporty:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_sporty ""
        else:
            rpg_sporty ""

    elif game_state.t3_current_player.character_type == CharacterType.Perfect:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_perfect ""
        else:
            rpg_perfect ""

    call t3_scenario_enemy_end

    return

label t3_scenario_enemy_knight:
    show other_icon at top with dissolve

    "A wild knight appeared!"

    call t3_scenario_show_trio

    if game_state.t3_current_player.character_type == CharacterType.Nerdy:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_nerdy ""
        else:
            rpg_nerdy ""

    elif game_state.t3_current_player.character_type == CharacterType.Sporty:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_sporty ""
        else:
            rpg_sporty ""

    elif game_state.t3_current_player.character_type == CharacterType.Perfect:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_perfect ""
        else:
            rpg_perfect ""

    call t3_scenario_enemy_end

    return

label t3_scenario_enemy_goblin:
    show other_icon at top with dissolve

    "A wild goblin appeared!"

    call t3_scenario_show_trio

    if game_state.t3_current_player.character_type == CharacterType.Nerdy:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_nerdy ""
        else:
            rpg_nerdy ""

    elif game_state.t3_current_player.character_type == CharacterType.Sporty:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_sporty ""
        else:
            rpg_sporty ""

    elif game_state.t3_current_player.character_type == CharacterType.Perfect:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_perfect ""
        else:
            rpg_perfect ""

    call t3_scenario_enemy_end

    return

label t3_scenario_enemy_spirit:
    show other_icon at top with dissolve

    "A wild spirit appeared!"

    call t3_scenario_show_trio

    if game_state.t3_current_player.character_type == CharacterType.Nerdy:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_nerdy ""
        else:
            rpg_nerdy ""

    elif game_state.t3_current_player.character_type == CharacterType.Sporty:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_sporty ""
        else:
            rpg_sporty ""

    elif game_state.t3_current_player.character_type == CharacterType.Perfect:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_perfect ""
        else:
            rpg_perfect ""

    call t3_scenario_enemy_end

    return

label t3_scenario_enemy_slime:
    show other_icon at top with dissolve

    "A wild slime appeared!"

    call t3_scenario_show_trio

    if game_state.t3_current_player.character_type == CharacterType.Nerdy:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_nerdy ""
        else:
            rpg_nerdy ""

    elif game_state.t3_current_player.character_type == CharacterType.Sporty:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_sporty ""
        else:
            rpg_sporty ""

    elif game_state.t3_current_player.character_type == CharacterType.Perfect:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_perfect ""
        else:
            rpg_perfect ""

    call t3_scenario_enemy_end

    return

label t3_scenario_enemy_plant:
    show other_icon at top with dissolve

    "A wild plant appeared!"

    call t3_scenario_show_trio

    if game_state.t3_current_player.character_type == CharacterType.Nerdy:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_nerdy ""
        else:
            rpg_nerdy ""

    elif game_state.t3_current_player.character_type == CharacterType.Sporty:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_sporty ""
        else:
            rpg_sporty ""

    elif game_state.t3_current_player.character_type == CharacterType.Perfect:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_perfect ""
        else:
            rpg_perfect ""

    call t3_scenario_enemy_end

    return

label t3_scenario_enemy_golem:
    show other_icon at top with dissolve

    "A wild golem appeared!"

    call t3_scenario_show_trio

    if game_state.t3_current_player.character_type == CharacterType.Nerdy:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_nerdy ""
        else:
            rpg_nerdy ""

    elif game_state.t3_current_player.character_type == CharacterType.Sporty:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_sporty ""
        else:
            rpg_sporty ""

    elif game_state.t3_current_player.character_type == CharacterType.Perfect:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_perfect ""
        else:
            rpg_perfect ""

    call t3_scenario_enemy_end

    return

label t3_scenario_enemy_undead:
    show other_icon at top with dissolve

    "A wild undead appeared!"

    call t3_scenario_show_trio

    if game_state.t3_current_player.character_type == CharacterType.Nerdy:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_nerdy ""
        else:
            rpg_nerdy ""

    elif game_state.t3_current_player.character_type == CharacterType.Sporty:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_sporty ""
        else:
            rpg_sporty ""

    elif game_state.t3_current_player.character_type == CharacterType.Perfect:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_perfect ""
        else:
            rpg_perfect ""

    call t3_scenario_enemy_end

    return

label t3_scenario_enemy_demon:
    show other_icon at top with dissolve

    "A wild demon appeared!"

    call t3_scenario_show_trio

    if game_state.t3_current_player.character_type == CharacterType.Nerdy:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_nerdy ""
        else:
            rpg_nerdy ""

    elif game_state.t3_current_player.character_type == CharacterType.Sporty:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_sporty ""
        else:
            rpg_sporty ""

    elif game_state.t3_current_player.character_type == CharacterType.Perfect:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_perfect ""
        else:
            rpg_perfect ""

    call t3_scenario_enemy_end

    return

label t3_scenario_enemy_robot:
    show other_icon at top with dissolve

    "A wild robot appeared!"

    call t3_scenario_show_trio

    if game_state.t3_current_player.character_type == CharacterType.Nerdy:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_nerdy ""
        else:
            rpg_nerdy ""

    elif game_state.t3_current_player.character_type == CharacterType.Sporty:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_sporty ""
        else:
            rpg_sporty ""

    elif game_state.t3_current_player.character_type == CharacterType.Perfect:
        if game_state.t3_current_player.has_encountered_enemy_type(game_state.t3_current_scenario.current_entity):
            rpg_perfect ""
        else:
            rpg_perfect ""

    call t3_scenario_enemy_end

    return