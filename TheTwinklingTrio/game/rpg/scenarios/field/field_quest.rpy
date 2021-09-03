define t3_scenario_field_quest_round_0_actions = [
    ActionMenuOption("(Style) Approach confidently", CharacterType.Nerdy, AttributeType.Style),
    ActionMenuOption("(Magic) Read its mind (cost 10 Mana)", CharacterType.Nerdy, AttributeType.Magic, 10),
    ActionMenuOption("(Wisdom) Analyze from afar", CharacterType.Nerdy, AttributeType.Wisdom),
    ActionMenuOption("(Style) Show off cool moves", CharacterType.Sporty, AttributeType.Style),
    ActionMenuOption("(Magic) Throw a fireball (cost 10 Mana)", CharacterType.Sporty, AttributeType.Magic, 10),
    ActionMenuOption("(Wisdom) Use the senses", CharacterType.Sporty, AttributeType.Wisdom),
    ActionMenuOption("(Style) Intimidate", CharacterType.Perfect, AttributeType.Style),
    ActionMenuOption("(Magic) Cast detection spell (cost 10 Mana)", CharacterType.Perfect, AttributeType.Magic, 10),
    ActionMenuOption("(Wisdom) Seek an audience", CharacterType.Perfect, AttributeType.Wisdom)
]

label t3_scenario_field_quest:
    scene bg rpg field

    "The empty meadow was eerily quiet."
    "No animals, no monsters, no humans. Only silence."

    call t3_scenario_show_trio from _call_t3_scenario_show_trio

    "The party looked around as they discussed their next move."

    rpg_nerdy "The intell I gathered pointed to this place, but it would seem there really is nothing here."

    rpg_sporty "So, what do we do now?"

    rpg_perfect "We should look around for clues. Perhaps we'll find something to point us in the right direction."

    rpg_sporty "Uh... what about that thing over there? Do you think that's a clue?"

    show other_icon at top with dissolve

    "A conspicuous [game_state.t3_current_scenario.current_entity.name] stood alone in the middle of the meadow."

    rpg_sporty "Just a [game_state.t3_current_scenario.current_entity.name]? Aww, I was hoping for something more exciting..."

    rpg_perfect "Shush. Don't question the narrator."

    rpg_sporty "Hey, don't pretend you weren't hoping for more, too."
    rpg_sporty "Like, why not a unicorn or a dragon? Ya know, something cool and exciting?"

    rpg_perfect "Ha! I already have the most beautiful, radiant, amazing unicorn there is."

    rpg_sporty "Huh, really? You do?"

    rpg_perfect "Of course. If you can ride a skateboard, certainly I can ride a unicorn."
    rpg_perfect "What about you, [preferences.t3_char_nerdy_name]? Er, I mean, [preferences.t3_rpg_char_nerdy_name]?"

    rpg_nerdy "I live on a giant turtle."

    rpg_sporty "Woah, you two are so cool! I'm gonna have to step up my game."
    rpg_sporty "Oh, I know! My skateboard can be magical with -"

    "The conspicuous [game_state.t3_current_scenario.current_entity.name] suddenly made a sound, as if it were awkwardly clearing its wooden throat."

    rpg_other "I'm still here, you know..."

    rpg_sporty "Ack! It makes noise!"

    rpg_perfect "Calm down. It seems like it wants us to interact with it."

    "In order to interact with objects and people in the world, you have to perform actions."
    "Remember that the success or failure of an action depends on your attributes, including a strength bonus and weakness penalty."
    "Some actions may cost {color=#6684a3}Mana{/color}, {color=#6684a3}Money{/color}, or even {color=#6684a3}Health{/color} to perform, so be careful not to run out."
    "{color=#6684a3}[preferences.t3_rpg_char_nerdy_name]{/color} will go first to demonstrate."

    # Make sure nerdy is the current player
    $ game_state.t3_current_player = game_state.t3_player_nerdy

    call t3_scenario_player_action_select from _call_t3_scenario_player_action_select

    rpg_other "The only thing I remember is that I had a fight with my best friend back when I was human."
    rpg_other "It was such a silly, pointless fight. All I want to do is find him and tell him how sorry I am, but I can't look for him like this."
    rpg_other "I just want to know if he's okay. Will you help me?"

    rpg_sporty "Of course we'll help, right?"

    rpg_perfect "Indeed, I believe we should."
    rpg_perfect "[game_state.t3_current_scenario.current_entity.name], can you think of anything else you can tell us?"
    rpg_perfect "Do you remember anything ususual happening before or after the fight with your friend?"

    rpg_other "Hmm... let me think."
    rpg_other "Now that you mention it, I remember a strange traveler coming to town. A knight."

    rpg_sporty "A knight? Like the holier than thou, 'chivalry isn't dead' type?"

    rpg_perfect "More importantly, why would a knight come to a small human village in the middle of nowhere?"
    rpg_perfect "I am, of course, assuming that knights in this world are lords and ladies of the human realm."
    rpg_perfect "Is that a correct assumption, [preferences.t3_rpg_char_nerdy_name]?"

    rpg_nerdy "Yes, that's correct."
    rpg_nerdy "It would be highly unusual for a knight to come to this remote human village."

    rpg_other "Exactly, which is why it caused such a fuss."
    rpg_other "Not that any of that matters now..."

    rpg_sporty "Cheer up, [game_state.t3_current_scenario.current_entity.name]! We'll find your friend in no time, just leave it to us."

    rpg_perfect "And we'll keep an eye out for this strange knight, as well."

    rpg_nerdy "Do you know where your friend is, [game_state.t3_current_scenario.current_entity.name]?"

    rpg_other "There's a really tall, green hill to the east of here."
    rpg_other "He always goes there when he's upset. The village looks so tiny from up there, it makes all your problems seem unimportant."

    rpg_sporty "Nice! Sounds like we're going hiking."

    rpg_perfect "I'm detecting the presence of monsters in that direction..."
    rpg_perfect "We should probably be prepared to fight."

    rpg_nerdy "Let's go."

    rpg_other "Thank you so much for agreeing to help me. Please come back safely!"

    # Save current NPC's name for later
    $ game_state.t3_training_dummy_known_name = game_state.t3_current_scenario.current_entity.name

    call t3_scenario_hide_trio from _call_t3_scenario_hide_trio

    return

label t3_scenario_field_quest_nerdy_style_0_success:
    # "(Style) Approach confidently"
    
    rpg_nerdy "Hello, strange being. My name is [preferences.t3_rpg_char_nerdy_name]. I've come to help."
    rpg_nerdy "Do you know what happened here?"

    $ game_state.t3_current_scenario.current_entity.update_character_name(game_state.t3_training_dummy_actual_name)

    rpg_other "O-oh, hello. I'm, uh, [game_state.t3_current_scenario.current_entity.name]."

    rpg_other "I'm sorry, it's just been such a long time since I've talked to someone."

    rpg_nerdy "That's alright. There's no need to be worried."

    rpg_other "Are you... are you a sorcerer, by any chance? Maybe you really can help."
    rpg_other "My memory is hazy, but I think... I think I used to be human."
    rpg_other "But now I'm stuck like this: wooden, lifeless. I don't even have legs."

    rpg_nerdy "I see."
    
    $ game_state.t3_current_scenario.keep_going = False

    return

label t3_scenario_field_quest_nerdy_style_0_failure:
    # "(Style) Approach confidently"
    
    rpg_nerdy "Hello, I'm the [preferences.t3_rpg_char_nerdy_title] and I'm here to solve all your problems."
    rpg_nerdy "Would you like some linseed oil? I've heard it can do wonders for a wooden finish as fine as yours."

    rpg_other "Umm... no, thanks."

    rpg_nerdy "I guess I overdid it."

    return

label t3_scenario_field_quest_nerdy_magic_0_success:
    # "(Magic) Read its mind (cost 10 Mana)"
    
    "[preferences.t3_rpg_char_nerdy_name] cast Telepathy."

    rpg_nerdy "...Yes, I see."
    rpg_nerdy "Hello, [game_state.t3_training_dummy_actual_name]. My name is [preferences.t3_rpg_char_nerdy_name]. I've come to help."

    $ game_state.t3_current_scenario.current_entity.update_character_name(game_state.t3_training_dummy_actual_name)

    rpg_other "H-how did you know my name? Are you a sorcerer?"

    rpg_nerdy "I'm the [preferences.t3_rpg_char_nerdy_title]. Could you tell me what happened?"

    rpg_other "Um, well, to be honest... I'm not quite sure."
    rpg_other "My memory is hazy, but I think... I think I used to be human."
    rpg_other "But as you can see, I'm stuck like this now: wooden, lifeless. I don't even have legs."

    rpg_nerdy "I understand."

    $ game_state.t3_current_scenario.keep_going = False

    return

label t3_scenario_field_quest_nerdy_magic_0_failure:
    # "(Magic) Read its mind (cost 10 Mana)"

    "[preferences.t3_rpg_char_nerdy_name] cast Telepathy."

    rpg_nerdy "...I'm not reading anything."
    rpg_nerdy "You must be an inanimate object after all."

    rpg_other "Er, no, I'm definitely not."
    rpg_other "How could an inanimate object talk?"

    rpg_nerdy "It wouldn't be impossible for inanimate objects can talk and move in this world."
    rpg_nerdy "Does that mean I'm also an inanimate object?"
    rpg_nerdy "Am I a puppet being given words by some higher force?"
    rpg_nerdy "I'll have to ponder this."

    return

label t3_scenario_field_quest_nerdy_wisdom_0_success:
    # "(Wisdom) Analyze from afar"
    
    rpg_nerdy "Based on the information I received, there used to be a human village here."
    rpg_nerdy "But now there's nothing but a [game_state.t3_current_scenario.current_entity.name]."
    rpg_nerdy "It can talk, so it's clearly not a normal [game_state.t3_current_scenario.current_entity.name]."
    rpg_nerdy "Maybe this [game_state.t3_current_scenario.current_entity.name] is actually an unfortunate human being."
    rpg_nerdy "Excuse me, [game_state.t3_current_scenario.current_entity.name], could you tell me your name?"

    $ game_state.t3_current_scenario.current_entity.update_character_name(game_state.t3_training_dummy_actual_name)

    rpg_other "O-oh, right, yes, hello. I'm, uh, [game_state.t3_current_scenario.current_entity.name]."

    rpg_other "Are you... are you a sorcerer, by any chance? Maybe you really can help."
    rpg_other "My memory is hazy, but I think... I think I used to be human, like you said."
    rpg_other "But now I'm stuck like this: wooden, lifeless. I don't even have legs."

    rpg_nerdy "I see."
    
    $ game_state.t3_current_scenario.keep_going = False

    return

label t3_scenario_field_quest_nerdy_wisdom_0_failure:
    # "(Wisdom) Analyze from afar"

    rpg_nerdy "Based on the information I received, there used to be a human village here."
    rpg_nerdy "But now there's nothing but a [game_state.t3_current_scenario.current_entity.name]."
    rpg_nerdy "Maybe the village got transformed into a [game_state.t3_current_scenario.current_entity.name]."

    rpg_other "Umm... that's definitely not right."

    rpg_nerdy "Oh. It seems I analyzed the situation poorly."

    return

label t3_scenario_field_quest_sporty_style_0_success:
    # "(Style) Show off cool moves"
    
    rpg_sporty "Hey, wanna see something cool?"
    rpg_sporty "This trick here is called an ollie. Awesome, right?"

    rpg_other "W-wow, I've never seen anything like that before!"
    rpg_other "Umm... uh... what is that thing you're standing on?"

    rpg_sporty "It's called a skateboard, and it's super rad."
    rpg_sporty "Wanna try?"

    rpg_other "O-oh, sorry, I can't. I, um, don't have legs."

    rpg_sporty "Oh my gosh, of course! Duh. I'm so sorry."
    rpg_sporty "Do you want to talk about it?"
    rpg_sporty "I'm [preferences.t3_rpg_char_sporty_name], by the way. Nice to meetcha!"

    $ game_state.t3_current_scenario.current_entity.update_character_name(game_state.t3_training_dummy_actual_name)

    rpg_other "I'm [game_state.t3_current_scenario.current_entity.name]. I think... I think I used to be human."

    rpg_sporty "Woah, really? You used to be human?"
    rpg_sporty "How did you end up all wooden and lifeless?"

    rpg_other "...I'm not sure."
    rpg_other "I can't remember much about my life before this."

    rpg_sporty "Aww, that's a bummer."

    $ game_state.t3_current_scenario.keep_going = False

    return

label t3_scenario_field_quest_sporty_style_0_failure:
    # "(Style) Show off cool moves"
    
    rpg_sporty "Yo, man, what's up?"

    rpg_other "Umm... I'm a girl."

    rpg_sporty "What? No way!"
    rpg_sporty "I, uh, didn't mean 'man' like man, I meant it, like, anyone. Ya know?"

    rpg_other "...Not really, no."

    rpg_sporty "Aww, c'mon. Did I really flop that hard?"

    return

label t3_scenario_field_quest_sporty_magic_0_success:
    # "(Magic) Throw a fireball (cost 15 Mana)"
    
    "[preferences.t3_rpg_char_sporty_name] cast Fireball."

    rpg_sporty "Take that, monster!"

    rpg_other "EEEEEEEEK!"
    rpg_other "Wait, wait, please, I'm not a monster! Just help me put out this fire!"

    rpg_sporty "Huh, you're not? You kinda seem like a monster..."
    rpg_sporty "But I guess a [game_state.t3_current_scenario.current_entity.name] can't really pose a threat."

    rpg_other "Yes! NOW PUT OUT THE FIRE BEFORE I DIE!"

    rpg_sporty "Right, of course! Sorry about that."

    rpg_other "Whew... I thought I was done for."
    rpg_other "I don't want to die as a stupid [game_state.t3_current_scenario.current_entity.name], of all things..."

    rpg_sporty "I'm [preferences.t3_rpg_char_sporty_name], by the way. I'm here to help ya."

    rpg_other "If you were here to help, why did you set me on fire?"

    $ game_state.t3_current_scenario.current_entity.update_character_name(game_state.t3_training_dummy_actual_name)

    rpg_other "...Anyway, I'm [game_state.t3_current_scenario.current_entity.name]."
    rpg_other "My memory is hazy, but I think... I think I used to be human."
    rpg_other "But now I'm stuck like this: wooden, lifeless. I don't even have legs."

    rpg_sporty "Geez, that's a bummer."

    $ game_state.t3_current_scenario.keep_going = False

    return

label t3_scenario_field_quest_sporty_magic_0_failure:
    # "(Magic) Throw a fireball (cost 15 Mana)"
    
    "[preferences.t3_rpg_char_sporty_name] cast Fireball."

    rpg_sporty "Huh? I missed?"
    rpg_sporty "Wow, that's so incredibly lame."

    rpg_other "..."

    rpg_sporty "Yeah, yeah, sorry for wasting everybody's time."

    return

label t3_scenario_field_quest_sporty_wisdom_0_success:
    # "(Wisdom) Use the senses"

    rpg_sporty "*looks* Well, it doesn't look too scary."
    rpg_sporty "*pokes* Doesn't seem aggressive or hostile. It's hard to the touch."
    rpg_sporty "*knocks* Yep, that's wood and wood is hard."
    rpg_sporty "IS THERE ANYONE IN THERE?"

    rpg_other "Eep! Why are you yelling all of a sudden?"

    rpg_sporty "I wasn't sure if you could hear me. You don't have ears, do you?"

    rpg_other "Er, well, no. I can still hear you, though..."

    rpg_sporty "Really? Oh, okay!"
    rpg_sporty "I'm [preferences.t3_rpg_char_sporty_name]. What's your name?"

    $ game_state.t3_current_scenario.current_entity.update_character_name(game_state.t3_training_dummy_actual_name)
    rpg_other "H-hello, I'm [game_state.t3_current_scenario.current_entity.name]."

    rpg_other "My memory is hazy, but I think... I think I used to be human."
    rpg_other "But now I'm stuck like this: wooden, lifeless. I don't even have legs."

    rpg_sporty "Geez, that's a bummer."

    $ game_state.t3_current_scenario.keep_going = False

    return

label t3_scenario_field_quest_sporty_wisdom_0_failure:
    # "(Wisdom) Use the senses"
    
    rpg_sporty "*looks* Yep, looks like a [game_state.t3_current_scenario.current_entity.name]."
    rpg_sporty "*pokes* Feels like a [game_state.t3_current_scenario.current_entity.name], too."
    rpg_sporty "Okay, guys, mystery solved: this is definitely a [game_state.t3_current_scenario.current_entity.name]."

    rpg_other "Umm..."
    
    rpg_sporty "What, you don't like that answer?"
    
    rpg_other "..."

    rpg_sporty "C'mon, just tell me your secrets already!"

    return

label t3_scenario_field_quest_perfect_style_0_success:
    # "(Style) Intimidate"
    
    rpg_perfect "A living, talking wooden doll... Could it be animated through magic?"
    rpg_perfect "Perhaps I should take this [game_state.t3_current_scenario.current_entity.name] home for dissection."
    
    rpg_other "Eep!"

    rpg_perfect "Unless, of course, you'd like to give me a reason not to."

    rpg_other "P-please don't cut me open! I'm human, I swear - or at least, I think I used to be."

    $ game_state.t3_current_scenario.current_entity.update_character_name(game_state.t3_training_dummy_actual_name)

    rpg_other "My name was [game_state.t3_current_scenario.current_entity.name]."
    rpg_other "But now I'm stuck like this: wooden, lifeless. I don't even have legs."

    rpg_perfect "Oh my, you used to be human? How did you get like this?"

    rpg_other "...I'm not sure, to be honest."
    rpg_other "I can't remember much about my life before this."

    rpg_perfect "Aww, I'm sorry. You poor thing."

    $ game_state.t3_current_scenario.keep_going = False

    return

label t3_scenario_field_quest_perfect_style_0_failure:
    # "(Style) Intimidate"
    
    rpg_perfect "I have no time to play games with you, creature."
    rpg_perfect "Reveal your true form and give me the answers I seek at once."

    rpg_other "..."

    rpg_perfect "...Pretty please with sugar on top?"

    rpg_other "..."

    return

label t3_scenario_field_quest_perfect_magic_0_success:
    # "(Magic) Cast detection spell (cost 10 Mana)"

    "[preferences.t3_rpg_char_perfect_name] cast Detection."

    rpg_perfect "I sense... a human female soul?"
    rpg_perfect "Oh my, I'm so sorry for mistaking you for something else, Miss [game_state.t3_current_scenario.current_entity.name]."
    rpg_perfect "I'm [preferences.t3_rpg_char_perfect_name]. Would you please tell me your story?"

    $ game_state.t3_current_scenario.current_entity.update_character_name(game_state.t3_training_dummy_actual_name)

    rpg_other "O-oh, hello... I'm [game_state.t3_current_scenario.current_entity.name]."
    rpg_other "I'm surprised you could tell I used to be human. Are you a sorcerer?"

    rpg_perfect "I am indeed."

    rpg_other "Then maybe you can help..."
    rpg_other "My memory is hazy, so I'm not sure what exactly happened."
    rpg_other "But now I'm stuck like this: wooden, lifeless. I don't even have legs."

    rpg_perfect "Aww, you've been through so much, you poor thing."

    $ game_state.t3_current_scenario.keep_going = False

    return

label t3_scenario_field_quest_perfect_magic_0_failure:
    # "(Magic) Cast detection spell (cost 10 Mana)"
    
    "[preferences.t3_rpg_char_perfect_name] cast Detection."

    rpg_perfect "...I don't sense anything."
    rpg_perfect "But that doesn't make sense. Surely I should sense at least some sort of presense."
    rpg_perfect "Tell me, [game_state.t3_current_scenario.current_entity.name], are you capable of blocking my magic?"

    rpg_other "Umm... no?"

    rpg_perfect "Perhaps a problem occurred during the cast, then. That's unfortunate."

    return

label t3_scenario_field_quest_perfect_wisdom_0_success:
    # "(Wisdom) Seek an audience"
    
    rpg_perfect "Excuse me, [game_state.t3_current_scenario.current_entity.name], will you grant me an audience?"
    rpg_perfect "My name is [preferences.t3_rpg_char_perfect_name], the [preferences.t3_rpg_char_perfect_title]."
    rpg_perfect "My companions and I have come to investigate the disappearance of a human village. Do you know anything?"

    rpg_other "O-oh, well, that might explain something..."
    rpg_other "My memory is hazy, but I think... I think I used to be human."
    rpg_other "But as you can see, I'm stuck like this now: wooden, lifeless. I don't even have legs."

    $ game_state.t3_current_scenario.current_entity.update_character_name(game_state.t3_training_dummy_actual_name)

    rpg_other "I'm [game_state.t3_current_scenario.current_entity.name], by the way. It's nice to meet you."

    rpg_perfect "Likewise, dear [game_state.t3_current_scenario.current_entity.name]."
    rpg_perfect "Thank you for telling me your story."

    $ game_state.t3_current_scenario.keep_going = False

    return

label t3_scenario_field_quest_perfect_wisdom_0_failure:
    # "(Wisdom) Seek an audience"
    
    rpg_perfect "I am [preferences.t3_rpg_char_perfect_name], the [preferences.t3_rpg_char_perfect_title]. I request an audience."

    rpg_other "...W-with me?"

    rpg_perfect "Yes, of course."

    rpg_other "Er, I'm not really sure what to say..."

    rpg_perfect "Hmm. Was I too formal?"

    return