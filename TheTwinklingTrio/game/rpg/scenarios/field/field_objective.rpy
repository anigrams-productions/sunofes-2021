define t3_scenario_field_objective_round_0_actions = [
    ActionMenuOption("(Style) Dodge his attacks", CharacterType.Nerdy, AttributeType.Style),
    ActionMenuOption("(Magic) Restrain him (cost 10 Mana)", CharacterType.Nerdy, AttributeType.Magic, 10),
    ActionMenuOption("(Wisdom) Use reason", CharacterType.Nerdy, AttributeType.Wisdom),
    ActionMenuOption("(Style) Dance party?", CharacterType.Sporty, AttributeType.Style),
    ActionMenuOption("(Magic) Blind him (cost 10 Mana)", CharacterType.Sporty, AttributeType.Magic, 10),
    ActionMenuOption("(Wisdom) Appeal to his emotions", CharacterType.Sporty, AttributeType.Wisdom),
    ActionMenuOption("(Style) Prove superiority", CharacterType.Perfect, AttributeType.Style),
    ActionMenuOption("(Magic) Summon familiar (cost 10 Mana)", CharacterType.Perfect, AttributeType.Magic, 10),
    ActionMenuOption("(Wisdom) Be gentle", CharacterType.Perfect, AttributeType.Wisdom)
]

label t3_scenario_field_objective:
    jump t3_scenario_field_objective_encounter

    scene bg rpg field

    "After surviving the fearsome boss fight, the party finally reached the top of the tall, green hill that [game_state.t3_training_dummy_known_name] mentioned."
    "What they found was..."

    scene black

    perfect "Wait!"
    perfect "Before we continue the story, what do you think their fight was about?"
    
    scene bg room day open

    show nerdy casual 8 at topleft
    show sporty casual 1 at top
    show perfect casual 1 at topright
    with dissolve

    perfect "You know, the fight between [game_state.t3_training_dummy_known_name] and the so-called 'friend'?"

    show perfect casual 3

    perfect "{i}I{/i} think her friend publicly, passionately proposed marriage to her."

    show perfect casual 9

    perfect "But she was so surprised, she didn't know how to respond."

    show perfect casual 8

    perfect "So, he got the wrong idea and thought she didn't love him enough to marry him."

    show perfect casual 15

    perfect "He ran off in tears, regretting ever asking the question."

    show sporty casual 11

    sporty "No way it was something so gross and dramatic."
    sporty "[game_state.t3_training_dummy_known_name] said it was a 'silly' fight, remember?"

    show sporty casual 6

    sporty "I bet they were fighting over something like whether slushies are better with or without ice cream."

    show sporty casual 3

    sporty "Of course, the only correct answer is with ice cream."

    show perfect casual 4

    perfect "You really think something so trivial would make the poor guy run off like that?"

    show sporty casual 17

    sporty "Don't tell me you think slushies are better without ice cream, [preferences.t3_char_perfect_name]!"

    show perfect casual 6

    perfect "Well... I do think the sweetness of the ice cream can sometimes distract from the fruity flavor slushies are known for."

    show perfect casual 1

    perfect "What do you think, [preferences.t3_char_nerdy_name]?"

    show nerdy casual 1

    nerdy "I like both."

    show perfect casual 3

    perfect "I meant about the story, silly."

    show sporty casual 1

    sporty "Yeah, [preferences.t3_char_nerdy_name], what do {i}you{/i} think their fight was about?"

    show perfect casual 1

    menu:
        "What should I choose?"

        "Romance":
            show nerdy casual 8

            nerdy "I agree with [preferences.t3_char_perfect_name]."

            show perfect casual 3

            perfect "I knew you'd see things my way, my dear."
            perfect "Romantic drama is the perfect plot device to spice up this story."

            show sporty casual 16

            sporty "Oh, great. Here we go again..."

            show nerdy casual 1

            nerdy "Let's continue."

            jump t3_scenario_field_objective_romance

        "Slushies":
            show nerdy casual 8

            nerdy "I agree with [preferences.t3_char_sporty_name]."

            show sporty casual 35

            sporty "Yes, I knew it! Let the slushie discourse begin!"

            show perfect casual 6

            perfect "Well, no harm done, I suppose."

            show nerdy casual 1

            nerdy "Let's continue."

            jump t3_scenario_field_objective_slushies
        "Something else":
            show nerdy casual 12

            nerdy "[game_state.t3_training_dummy_known_name] told her friend that she was leaving and going far away, knowing they'd probably never see each other again."

            show perfect casual 19

            perfect "..."

            show sporty casual 53

            sporty "..."

            show sporty casual 12

            sporty "...I mean, if he blames her for that, then he sounds like a bad friend."

            show perfect casual 53

            perfect "Yes, a terrible friend indeed."

            show sporty casual 1

            sporty "But [game_state.t3_training_dummy_known_name] asked us to help him anyway, so that's what we're going to do, right?"

            show perfect casual 7

            perfect "That's right."
            perfect "If she's willing to forgive him, then perhaps their friendship can still be salvaged."

            show sporty casual 64

            sporty "What d'ya say, [preferences.t3_char_nerdy_name]? Ready to go help them be friends again?"

            show nerdy casual 3

            nerdy "Yes. Let's go."

            jump t3_scenario_field_objective_friendship

    return

label t3_scenario_field_objective_encounter:

    scene black

    "As I was saying..."

    scene bg rpg field

    "The party finally reached the top of the tall, green hill that [game_state.t3_training_dummy_known_name] mentioned."

    call t3_scenario_show_trio

    rpg_perfect "Hmm... it seems pretty quiet here."
    rpg_perfect "Is it possible [game_state.t3_training_dummy_known_name]'s friend is already dead? Maybe he got eaten or killed..."

    rpg_sporty "No way, that can't be! We promised [game_state.t3_training_dummy_known_name] that we'd find him and bring him back."

    rpg_nerdy "Look there."

    show other_icon at top with dissolve

    "A creepy [game_state.t3_current_scenario.current_entity.name] waddled towards them, eyes wide and unblinking."

    rpg_perfect "Er... you don't think that's him, do you? [game_state.t3_training_dummy_known_name]'s friend?"
    rpg_perfect "Not that I'm judging, but... uh... he doesn't have a nose."

    rpg_sporty "There's only one way to find out, yeah?"
    rpg_sporty "YO, UGLY!"
    rpg_sporty "Do you know [game_state.t3_training_dummy_known_name], by any chance?"

    "The creepy [game_state.t3_current_scenario.current_entity.name] cackled maniacally."

    rpg_perfect "Uh, I don't think he liked you calling him ugly."

    if game_state.t3_training_dummy_known_name != game_state.t3_training_dummy_actual_name:
        rpg_perfect "And it probably doesn't help that we never learned poor [game_state.t3_training_dummy_known_name]'s real name, either..."

    rpg_other "Keh keh keh!"
    rpg_other "Humpty Dumpty sat on a wall. Humpty Dumpty had a great fall."
    rpg_other "And now it's {i}your{/i} turn to fall!"

    rpg_sporty "Yikes! Was that a threat?"
    rpg_sporty "Look, dude, I'm really sorry for calling you ugly. I didn't mean it, I swear!"

    rpg_perfect "Everyone, prepare yourselves. We have to find some way to get through to him."

    call t3_scenario_player_action_select

    "[game_state.t3_current_scenario.current_entity.name] suddenly grabbed his head and lurched forward, screaming as he dropped to his knees."

    hide other_icon with dissolve

    rpg_sporty "Woah, dude, are you okay? What's wrong?"

    rpg_perfect "Quick, we have to help him! [preferences.t3_rpg_char_nerdy_name], can you use your healing magic?"

    "???" "{font=fonts/monster/Macondo-Regular.ttf}I'm afraid that won't help him.{/font}"

    rpg_nerdy "Why not?"

    show villain_icon at top with dissolve

    rpg_villain "Bright-eyed young [game_state.t3_egg_man_actual_name] is no more. Only this hideous monster remains."
    rpg_villain "Such is the true nature of his heart."

    $ game_state.t3_current_scenario.current_entity.update_character_name(game_state.t3_egg_man_actual_name)

    rpg_sporty "You! I bet you're that weird knight [game_state.t3_training_dummy_known_name] mentioned, aren't you?"

    rpg_perfect "...Oh."
    rpg_perfect "Oh no."
    rpg_perfect "No no no."
    rpg_perfect "All those monsters we fought..."
    rpg_perfect "They were the residents of the village, weren't they?"

    $ have_players_killed = game_state.have_players_killed()

    if have_players_killed:
        rpg_perfect "And we..."
        rpg_perfect "Oh no, what have we done?"

    rpg_sporty "Huh? No way..."
    rpg_sporty "What the heck did you do to them, you armored freak?"

    rpg_villain "I merely revealed their true natures, that's all."
    rpg_villain "Humans are cruel, greedy, selfish, disgusting creatures. They are unrepentant, irredeemable."
    rpg_villain "And now, their outsides finally match their insides. The ugly truth has been revealed for all to see."

    if have_players_killed:
        rpg_villain "I must thank you for putting the wretched things out of their misery."

    rpg_sporty "So, what, you're some kind of religious zealot?"
    rpg_sporty "Definitely the holier than thou type of knight, then."

    rpg_nerdy "We'll stop you."

    rpg_perfect "That's right, we won't let you get away with this!"
    rpg_perfect "Everyone, prepare for a fight!"

    rpg_villain "A fight? With me? Ha! Surely, you must be joking."
    rpg_villain "You three aren't even worth my time. You're no better than those worthless human pests."
    rpg_villain "It's only a matter of time before your true natures are revealed, as well, and then you will see how truly shallow your 'friendship' is."

    rpg_sporty "Never! We're best friends for life. Nothing can tear us apart, you'll see!"

    hide villain_icon
    show villain_icon at topleftcenter
    show other_icon at toprightcenter
    with dissolve

    rpg_other "[t3_rpg_pronoun_sporty_sub_cap]'s...right..."
    rpg_other "Your curse... I'll break free. I have to... [game_state.t3_training_dummy_actual_name]'s waiting for me!"

    $ game_state.t3_training_dummy_known_name = game_state.t3_training_dummy_actual_name

    rpg_perfect "See? You're not wrong that people can be mean and selfish sometimes, but that doesn't mean they're all bad."
    rpg_perfect "Friends stick together, no matter what, through the good {i}and{/i} the bad."

    rpg_villain "Ha! Is that so? We'll see about that soon enough..."

    hide villain_icon
    show other_icon at top
    with dissolve
    
    "The [preferences.t3_rpg_char_villain_title] laughed and disappeared in a cloud of smoke and ash."

    rpg_sporty "Hey, [game_state.t3_current_scenario.current_entity.name], you alright?"

    rpg_other "Yes... I will be, thanks to you three."

    return

label t3_scenario_field_objective_romance:
    call t3_scenario_field_objective_encounter

    "Romance ending"

    return

label t3_scenario_field_objective_slushies:
    call t3_scenario_field_objective_encounter

    "Slushy ending"

    return

label t3_scenario_field_objective_friendship:
    call t3_scenario_field_objective_encounter

    "Friendship ending"

    return

label t3_scenario_field_objective_nerdy_style_0_success:
    # "(Style) Dodge attack"

    "[preferences.t3_rpg_char_nerdy_name] deftly stepped aside as the [game_state.t3_current_scenario.current_entity.name] came barreling towards [preferences.t3_rpg_pronoun_nerdy_obj]."

    rpg_other "Grrr. Stay still, you!"

    rpg_nerdy "I'd rather not."

    "The [game_state.t3_current_scenario.current_entity.name] rolled towards [preferences.t3_rpg_char_nerdy_name] with even more speed."
    "But [preferences.t3_rpg_char_nerdy_name] once again dodged the attack, letting the [game_state.t3_current_scenario.current_entity.name] run into the wall with a loud thud."

    rpg_other "Ow, Humpty Dumpty hit a wall..."

    rpg_nerdy "Are you okay? I can heal you."

    rpg_other "You would do that for me? But I... I tried to hurt you."
    rpg_other "Keh keh keh! I see what you're trying to do - you're trying to trick me!"
    rpg_other "But I, the [game_state.t3_current_scenario.current_entity.name], won't fall for it."

    rpg_nerdy "I'm not trying to trick you. I just want to help you."
    rpg_nerdy "You're not really a monster, are you?"

    rpg_other "I... I'm..."
    
    $ game_state.t3_current_scenario.keep_going = False

    return

label t3_scenario_field_objective_nerdy_style_0_failure:
    # "(Style) Dodge attack"
    
    "The [game_state.t3_current_scenario.current_entity.name] came barreling towards [preferences.t3_rpg_char_nerdy_name] as [preferences.t3_rpg_pronoun_nerdy_sub] stepped to the side."
    "Unfortunately, [preferences.t3_rpg_pronoun_nerdy_sub] stepped the wrong way, right into the oncoming [game_state.t3_current_scenario.current_entity.name]."

    rpg_nerdy "Ouch..."
    rpg_nerdy "That was less than ideal."

    rpg_other "Keh keh keh! Looks like your shell got cracked."

    return

label t3_scenario_field_objective_nerdy_magic_0_success:
    # "(Magic) Restrain (cost 10 Mana)"
    
    "[preferences.t3_rpg_char_nerdy_name] cast Restrain."

    rpg_other "KEH?! What is this sorcery?"

    rpg_nerdy "Vines. They'll keep you from hurting anyone else."

    rpg_other "You think you can stop me? I'm the [game_state.t3_current_scenario.current_entity.name]!"

    rpg_nerdy "That's not a very intimidating name."

    rpg_other "What?! You mean to say the idea of eggs cracking doesn't make you quiver in your boots?"

    rpg_nerdy "Not really."

    rpg_other "That can't be. My entire existence is flawed..."

    rpg_nerdy "Are you sure you're really a monster?"

    rpg_other "Of course! I... I'm..."

    $ game_state.t3_current_scenario.keep_going = False

    return

label t3_scenario_field_objective_nerdy_magic_0_failure:
    # "(Magic) Restrain (cost 10 Mana)"

    "[preferences.t3_rpg_char_nerdy_name] cast Restrain."
    "It wasn't very effective..."

    rpg_other "Keh keh keh! You thought some silly vines could stop me, the Incredible Edible [game_state.t3_current_scenario.current_entity.name]?"
    rpg_other "Time to get crackin'!"

    rpg_nerdy "Ugh... these egg puns are painful."

    return

label t3_scenario_field_objective_nerdy_wisdom_0_success:
    # "(Wisdom) Use reason"
    
    rpg_nerdy "You're [game_state.t3_training_dummy_known_name]'s friend, aren't you?"
    rpg_nerdy "Why are you doing this? Do you not remember her?"

    rpg_other "Keh keh keh! [game_state.t3_training_dummy_known_name] who?"
    rpg_other "I need no friends. I'm the [game_state.t3_current_scenario.current_entity.name]!"

    rpg_nerdy "She wanted us to tell you that she's sorry."
    rpg_nerdy "She just wants to know that you're okay. Are you okay, [game_state.t3_current_scenario.current_entity.name]?"

    rpg_other "Am I...okay? I've never thought about it."
    rpg_other "Is this [game_state.t3_training_dummy_known_name] really that worried about...me?"
    
    $ game_state.t3_current_scenario.keep_going = False

    return

label t3_scenario_field_objective_nerdy_wisdom_0_failure:
    # "(Wisdom) Use reason"

    rpg_nerdy "If you calm down, we can talk about-"

    rpg_other "Keh keh keh! No talking, only cracking!"

    rpg_nerdy "But-"

    rpg_other "No buts, either! Only cracking, I said."

    rpg_nerdy "Yes, I got it the first time."

    return

label t3_scenario_field_objective_sporty_style_0_success:
    # "(Style) Dance party"
    
    rpg_sporty "You and me, bro. Right here, right now. {i}Dance party{/i}."

    rpg_other "Keh keh keh?"

    rpg_sporty "Dunst dunst dunst dunst. Hear that beat? C'mon, start movin'."
    rpg_sporty "Just shake this here, shake that there. It's easy, I promise."

    rpg_other "...Like this?"

    rpg_sporty "Yeah, exactly! You got it! Look at you go, you're a dancing machine!"

    rpg_other "But what if I fall and crack?"

    rpg_sporty "Then we'll help you get back up again. That's what friends are for, right?"

    rpg_other "Friends? Is that... what this feeling is?"

    $ game_state.t3_current_scenario.keep_going = False

    return

label t3_scenario_field_objective_sporty_style_0_failure:
    # "(Style) Dance party"
    
    rpg_sporty "Hey, wanna have a dance party with me?"

    rpg_other "Keh? A what?"

    rpg_sporty "A dance party. Ya know, where you dance with friends."

    rpg_other "Keh keh keh! I need no friends, I'm the [game_state.t3_current_scenario.current_entity.name]!"

    rpg_sporty "Umm...okay. Whatever, dude."

    return

label t3_scenario_field_objective_sporty_magic_0_success:
    # "(Magic) Blind (cost 10 Mana)"
    
    "[preferences.t3_rpg_char_sporty_name] cast Blind."

    rpg_sporty "Got a little sun in your eyes there, buddy?"

    rpg_other "Keh?! What did you do?"

    rpg_sporty "Don't worry, it'll wear off soon."
    rpg_sporty "In the meantime, I'd really appreciate it if you stopped trying to kill us."
    rpg_sporty "Are you still mad about me calling you ugly? 'Cause I really am sorry..."

    rpg_other "No, no, I know I'm ugly."
    rpg_other "I get the feeling I wasn't always like this..."

    rpg_sporty "Huh? What do you mean?"

    $ game_state.t3_current_scenario.keep_going = False

    return

label t3_scenario_field_objective_sporty_magic_0_failure:
    # "(Magic) Blind (cost 10 Mana)"
    
    "[preferences.t3_rpg_char_sporty_name] cast Blind."

    rpg_other "Keh keh keh! You cannot blind me, I'm the [game_state.t3_current_scenario.current_entity.name]!"

    rpg_sporty "Huh, seriously?"
    rpg_sporty "Man, I thought for sure that trick would work."

    return

label t3_scenario_field_objective_sporty_wisdom_0_success:
    # "(Wisdom) Appeal to his emotions"

    rpg_sporty "Hey, don't you remember [game_state.t3_training_dummy_known_name]?"
    rpg_sporty "She's been waiting for you all alone, all this time."
    rpg_sporty "She's scared. And cursed. And she needs your help."

    rpg_other "Keh? My help?"

    rpg_sporty "You're her best friend, aren't you? You're the only one who can help her."

    rpg_other "Me? ...Help?"

    rpg_other "But I'm the [game_state.t3_current_scenario.current_entity.name]. I'm just a monster."

    rpg_sporty "Not to her! You're her favorite person in the whole world! That's what it means to be someone's best friend."

    rpg_other "Best friend... I..."

    $ game_state.t3_current_scenario.keep_going = False

    return

label t3_scenario_field_objective_sporty_wisdom_0_failure:
    # "(Wisdom) Appeal to his emotions"
    
    rpg_sporty "Hey, remember [game_state.t3_training_dummy_known_name]?"
    rpg_sporty "Ya know, your best friend? The one you ran off and left all alone?"

    rpg_other "Keh keh keh! [game_state.t3_training_dummy_known_name] who?"
    rpg_other "I need no friends. I'm the [game_state.t3_current_scenario.current_entity.name]!"

    rpg_sporty "Well, that's not the answer I was hoping for..."

    return

label t3_scenario_field_objective_perfect_style_0_success:
    # "(Style) Prove superiority"
    
    rpg_perfect "Mr. [game_state.t3_current_scenario.current_entity.name], I understand you have a penchant for children's nursery rhymes."
    rpg_perfect "But can you handle these eggs-traordinary jokes?"

    rpg_other "Keh keh keh! Don't yolk with me, I'm the master of egg jokes!"

    rpg_perfect "Alright, then, why was the egg late for school?"

    rpg_other "Wait, what's school?"

    rpg_perfect "He didn't study for the eggs-am."
    rpg_perfect "What's an egg's favorite type of coffee?"

    rpg_other "What's coffee? Hey, this isn't fair!"

    rpg_perfect "An eggspresso!"
    rpg_perfect "What did the egg say to the clown?"

    rpg_other "WHAT'S A CLOWN?"

    rpg_perfect "You crack me up."
    rpg_perfect "Ready to admit defeat yet, Mr. [game_state.t3_current_scenario.current_entity.name]?"

    rpg_other "I have to admit, that last one was kind of funny..."
    rpg_other "Fine, I'll lay down my egg puns and hear what you have to say."

    rpg_perfect "Good, that's what I like to hear."
    rpg_perfect "Now, about [game_state.t3_training_dummy_known_name]..."

    $ game_state.t3_current_scenario.keep_going = False

    return

label t3_scenario_field_objective_perfect_style_0_failure:
    # "(Style) Prove superiority"

    rpg_perfect "Mr. [game_state.t3_current_scenario.current_entity.name], I understand you're upset, but you would do well to fear us."
    rpg_perfect "I am [preferences.t3_rpg_char_perfect_name], the [preferences.t3_rpg_char_perfect_title]. I'm one of the most powerful sorceresses known to man."

    rpg_other "Keh keh keh! I've never heard of you. Your name holds no weight here, witch!"

    rpg_perfect "Excuse me, did you just call me a witch?"
    rpg_perfect "I'm gonna show you what {i}really{/i} happened to Humpty Dumpty, you egg-shaped freak."

    rpg_sporty "Um, hey, we're supposed to be trying {i}not{/i} to kill him, right?"

    rpg_perfect "Humph. He deserves it, though."

    return

label t3_scenario_field_objective_perfect_magic_0_success:
    # "(Magic) Summon familiar (cost 10 Mana)"

    "[preferences.t3_rpg_char_perfect_name] cast Summon Familiar."

    rpg_perfect "This is my familiar, Roxi. Isn't she cute?"
    rpg_perfect "Roxi, mind helping me out here?"

    rpg_other "Keh? I feel the cat's cuteness calling to me..."
    rpg_other "May I pet her?"

    rpg_perfect "Of course, as long as you're gentle."
    rpg_perfect "She's such a sweet kitty, as well as a good judge of character."
    rpg_perfect "If she lets you pet her, you must be a good person."

    rpg_other "Really? Me? A good person?"
    rpg_other "But I'm just a monster..."

    rpg_perfect "Roxi doesn't think so. Look how happy she is letting you pet her, see?"

    rpg_other "I... I'm..."

    $ game_state.t3_current_scenario.keep_going = False

    return

label t3_scenario_field_objective_perfect_magic_0_failure:
    # "(Magic) Summon familiar (cost 10 Mana)"
    
    "[preferences.t3_rpg_char_perfect_name] cast Summon Familiar."

    rpg_perfect "This is my familiar, Epona. Isn't she amazing?"
    rpg_perfect "A unicorn with such a radiant coat is only born once every 1,000 years. She's truly one of a kind."
    rpg_perfect "Doesn't it make you green with envy?"

    rpg_other "Keh keh keh! You won't crack this shell so easily!"
    rpg_other "I have no need for your fancy unicorns. I'm the [game_state.t3_current_scenario.current_entity.name]!"

    rpg_perfect "But she's so amazing and beautiful! How can you not be impressed?"

    return

label t3_scenario_field_objective_perfect_wisdom_0_success:
    # "(Wisdom) Be gentle"
    
    rpg_perfect "It's alright, Mr. [game_state.t3_current_scenario.current_entity.name], we're not here to hurt you."
    rpg_perfect "[game_state.t3_training_dummy_known_name] asked us to look for you. Do you remember her?"

    rpg_other "Keh keh keh! [game_state.t3_training_dummy_known_name] who?"
    rpg_other "I don't need help, I'm the [game_state.t3_current_scenario.current_entity.name]!"

    rpg_perfect "Of course, I wouldn't dare suggest otherwise."
    rpg_perfect "But [game_state.t3_training_dummy_known_name] believed that you were her best friend, and that somehow the two of you got separated."
    rpg_perfect "She seemed very distraught about the whole thing. She's really worried about you."

    rpg_other "Worried? About me?"

    rpg_perfect "Indeed. But I suppose I'll just have to tell her you're too important to talk to her..."

    rpg_other "Wait, I... I'll talk to her."

    $ game_state.t3_current_scenario.keep_going = False

    return

label t3_scenario_field_objective_perfect_wisdom_0_failure:
    # "(Wisdom) Be gentle"
    
    rpg_perfect "Calm down. We're here to help you, Mr. [game_state.t3_current_scenario.current_entity.name]."

    rpg_other "Keh keh keh! I don't need help, I'm the [game_state.t3_current_scenario.current_entity.name]!"

    rpg_perfect "Um, yes, but-"

    rpg_other "It'll take more than that to crack this shell."

    return