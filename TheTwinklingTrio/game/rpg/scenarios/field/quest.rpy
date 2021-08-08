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
    "The meadow was eerily quiet."
    "No animals, no monsters, no humans. Only silence."

    show nerdy_icon at centerleft
    show sporty_icon at truecenter
    show perfect_icon at centerright
    with dissolve

    "The party looked around in confusion as they discussed their next move."

    rpg_nerdy "The intell I gathered pointed to this place, but it would seem there's nothing here."

    rpg_sporty "So, what do we do now?"

    rpg_perfect "We should look around for clues. Perhaps we'll find something to point us in the right direction."

    rpg_sporty "Uh... what about that over there? Do you think that's a clue?"

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
    "Some actions may cost Mana, Money, or even Health to perform, so be careful not to run out."
    "[preferences.t3_rpg_char_nerdy_name] will go first to demonstrate."

    # Make sure nerdy is the current player
    $ game_state.t3_current_player = game_state.t3_player_nerdy

    call t3_scenario_player_action_select

    rpg_other "To be honest, I had a fight with my best friend just before my village disappeared."
    rpg_other "It was such a silly, pointless fight. All I want to do is find him and tell him how sorry I am, but I can't look for him like this."
    rpg_other "I just want to know if he's okay. Will you help me?"

    rpg_sporty "Of course we'll help, right?"

    rpg_perfect "Indeed, I believe we should."
    rpg_perfect "[game_state.t3_current_scenario.current_entity.name], can you think of anything else you can tell us? Did anything unusual happen before the village disappeared?"

    rpg_other "Hmm... let me think."
    rpg_other "Now that you mention it, a strange traveler arrived in town just before it happened. A knight."

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
    rpg_other "He always goes there when he's upset. The village looks so tiny from up there, and it makes all your problems seem so unimportant."

    rpg_sporty "Nice! Sounds like we're going hiking."

    rpg_perfect "I'm detecting the presence of monsters in that direction..."
    rpg_perfect "We should probably be prepared to fight."

    rpg_other "Thank you so much for helping me! Please come back safely."

    hide other_icon with dissolve

    rpg_nerdy "We should get going."

    hide nerdy_icon
    hide sporty_icon
    hide perfect_icon
    with dissolve

    return

label t3_scenario_field_quest_nerdy_style_0_success:
    # "(Style) Approach confidently"
    
    rpg_nerdy "Hello, strange being. My name is [preferences.t3_rpg_char_nerdy_name]. I've come to help."
    rpg_nerdy "Do you know what happened here?"

    $ game_state.t3_current_scenario.current_entity.name = "Rembi"

    rpg_other "O-oh, hello. I'm, uh, Rembi."

    rpg_other "I'm sorry, it's just been such a long time since I've talked to someone."

    rpg_nerdy "That's alright. There's no need to be worried."

    rpg_other "Are you... are you a sorcerer, by any chance? Maybe you really can help."
    rpg_other "I used to be human, you see. There used to be a village here, but now it's gone along with everyone else."
    rpg_other "And yet I'm stuck here... wooden, lifeless, with no legs."

    rpg_nerdy "I see."
    
    $ game_state.t3_current_scenario.keep_going = False

    return

label t3_scenario_field_quest_nerdy_style_0_failure:
    # "(Style) Approach confidently"
    
    rpg_nerdy "Hello, I'm the [preferences.t3_rpg_char_nerdy_title] and I'm here to solve all your problems."
    rpg_nerdy "Would you like some linseed oil? I've heard it can do wonders for a wooden finish as fine as yours."

    rpg_other "Umm... no, thanks."

    rpg_nerdy "Hm. Perhaps I overdid it."

    return

label t3_scenario_field_quest_nerdy_magic_0_success:
    # "(Magic) Read its mind (cost 10 Mana)"
    
    "[preferences.t3_rpg_char_nerdy_name] cast Telepathy."

    rpg_nerdy "...Yes, I see."
    rpg_nerdy "Hello, Rembi. My name is [preferences.t3_rpg_char_nerdy_name]. I've come to help."

    $ game_state.t3_current_scenario.current_entity.name = "Rembi"

    rpg_other "H-how did you know my name? Are you a sorcerer?"

    rpg_nerdy "Of a sort. Could you tell me what happened?"

    rpg_other "Um, well, there used to be a human village here."
    rpg_other "But now it's gone along with everyone else, and I've been turned into the thing you see before you."

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

    rpg_nerdy "Hmm... maybe in this world, inanimate objects talk and move."
    rpg_nerdy "Does that mean I'm an inanimate object? Am I a puppet being given words by some higher force?"
    rpg_nerdy "I'll have to ponder this."

    return

label t3_scenario_field_quest_nerdy_wisdom_0_success:
    # "(Wisdom) Analyze from afar"
    
    rpg_nerdy "Based on the information I received, there used to be a human village here."
    rpg_nerdy "Yet, now there is nothing but a lone [game_state.t3_current_scenario.current_entity.name] left behind."
    rpg_nerdy "We also know there is a curse afflicting humans, turning them into monsters."
    rpg_nerdy "Maybe this [game_state.t3_current_scenario.current_entity.name] is actually an unfortunate human being."
    rpg_nerdy "Excuse me, [game_state.t3_current_scenario.current_entity.name], could you tell me your name?"

    $ game_state.t3_current_scenario.current_entity.name = "Rembi"

    rpg_other "O-oh, right, yes, hello. I'm, uh, Rembi."

    rpg_other "You're right, I used to be a human from the village that used to here."
    rpg_other "But now I'm stuck here... wooden, lifeless, with no legs."

    rpg_nerdy "I see."
    
    $ game_state.t3_current_scenario.keep_going = False

    return

label t3_scenario_field_quest_nerdy_wisdom_0_failure:
    # "(Wisdom) Analyze from afar"

    rpg_nerdy "Based on the information I received, there used to be a human village here."
    rpg_nerdy "Yet, now there is nothing but a lone [game_state.t3_current_scenario.current_entity.name] left behind."
    rpg_nerdy "Whatever caused the human village to disappear must not have worked on the [game_state.t3_current_scenario.current_entity.name]."
    rpg_nerdy "Maybe the [game_state.t3_current_scenario.current_entity.name] was blessed by a powerful priest, which repelled the curse and kept it safe."

    rpg_other "Pretty sure if I were blessed, I wouldn't be a [game_state.t3_current_scenario.current_entity.name] in the first place..."

    rpg_nerdy "Hmm... It seems I've analyzed the situation poorly."

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

    $ game_state.t3_current_scenario.current_entity.name = "Rembi"

    rpg_other "I'm Rembi. I used to be human, but now I'm stuck like this."
    rpg_other "And the village that used to be here is gone, along with everyone else who lived there."

    rpg_sporty "Geez, that's a bummer."

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
    rpg_sporty "Oh, I know! You must be one of those humans that got cursed, huh?"

    rpg_other "Yes! NOW PUT OUT THE FIRE BEFORE I DIE!"

    rpg_sporty "Right, of course! Sorry about that."

    rpg_other "Whew... I thought I was done for."
    rpg_other "I don't want to die as a stupid [game_state.t3_current_scenario.current_entity.name], of all things..."

    rpg_sporty "I'm [preferences.t3_rpg_char_sporty_name], by the way. I'm here to help ya."

    rpg_other "If you were here to help, why did you set me on fire?"

    $ game_state.t3_current_scenario.current_entity.name = "Rembi"

    rpg_other "...Anyway, I'm Rembi."
    rpg_other "I used to be human, but now I'm stuck like this. The village I used to live in disappeared, along with all of its residents."

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

    rpg_other "Er, well, no, not in this form. I used to be human, though..."

    rpg_sporty "Really? Oh, okay!"
    rpg_sporty "I'm [preferences.t3_rpg_char_sporty_name]. What's your name?"

    $ game_state.t3_current_scenario.current_entity.name = "Rembi"
    rpg_other "H-hello, I'm Rembi."

    rpg_other "I used to live in the village here, but now it's gone along with all of its residents."
    rpg_other "I don't know what happened, but I ended up stuck like this."

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

    rpg_other "P-please don't cut me open! I'm human, I swear - or at least, I used to be."

    $ game_state.t3_current_scenario.current_entity.name = "Rembi"

    rpg_other "My name is Rembi. I used to live in the village here, but now it's gone and so is everyone else."
    rpg_other "I don't know what happened, but I ended up stuck like this."

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

    $ game_state.t3_current_scenario.current_entity.name = "Rembi"

    rpg_other "O-oh, hello... I'm Rembi."
    rpg_other "I'm surprised you could tell I used to be human. Are you a sorcerer?"
    rpg_other "Maybe you can help..."
    rpg_other "The village I lived in disappeared, and no one else is anywhere to be found."

    rpg_perfect "I am, indeed. You've been through so much, you poor thing."

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
    rpg_perfect "My companions and I have come to help the residents of a human village, but there doesn't seem to be one here."

    rpg_other "O-oh, well, that's because the village disappeared, along with everyone that lived there."
    rpg_other "...Except me, that is. I'm stuck here."

    $ game_state.t3_current_scenario.current_entity.name = "Rembi"

    rpg_other "I'm Rembi, by the way. It's nice to meet you."

    rpg_perfect "Likewise, dear [game_state.t3_current_scenario.current_entity.name]."
    rpg_perfect "Thank you for telling me your story."

    return

label t3_scenario_field_quest_perfect_wisdom_0_failure:
    # "(Wisdom) Seek an audience"
    
    rpg_perfect "I am [preferences.t3_rpg_char_perfect_name], the [preferences.t3_rpg_char_perfect_title]. I request an audience."

    rpg_other "...W-with me?"

    rpg_perfect "Yes, of course."

    rpg_other "Er, I'm not really sure what to say..."

    rpg_perfect "Hmm. Was I too formal?"

    return