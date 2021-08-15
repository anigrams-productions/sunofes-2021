# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define nerdy = Character(preferences.t3_char_nerdy_name, color="#827281")
define sporty = Character(preferences.t3_char_sporty_name, color="#e5914f")
define perfect = Character(preferences.t3_char_perfect_name, color="#e3848e")

define rpg_nerdy_character = Character(preferences.t3_rpg_char_nerdy_name, color="#827281")
define rpg_sporty_character = Character(preferences.t3_rpg_char_sporty_name, color="#e5914f")
define rpg_perfect_character = Character(preferences.t3_rpg_char_perfect_name, color="#e3848e")

define rpg_villain_character_unknown = Character(preferences.t3_rpg_char_villain_title, color="#93aeaf", what_font="fonts/monster/Macondo-Regular.ttf")
define rpg_villain_character_known = Character(preferences.t3_rpg_char_villain_name, color="#93aeaf", what_font="fonts/monster/Macondo-Regular.ttf")

# get capitalized versions of pronouns because Ren'Py can't handle .capitalize() in a say block
define t3_pronoun_nerdy_sub_cap = preferences.t3_pronoun_nerdy_sub.capitalize()
define t3_pronoun_nerdy_obj_cap = preferences.t3_pronoun_nerdy_obj.capitalize()
define t3_pronoun_nerdy_pos_cap = preferences.t3_pronoun_nerdy_pos.capitalize()
define t3_pronoun_nerdy_poss_cap = preferences.t3_pronoun_nerdy_poss.capitalize()
define t3_pronoun_nerdy_ref_cap = preferences.t3_pronoun_nerdy_ref.capitalize()

define t3_rpg_pronoun_nerdy_sub_cap = preferences.t3_rpg_pronoun_nerdy_sub.capitalize()
define t3_rpg_pronoun_nerdy_obj_cap = preferences.t3_rpg_pronoun_nerdy_obj.capitalize()
define t3_rpg_pronoun_nerdy_pos_cap = preferences.t3_rpg_pronoun_nerdy_pos.capitalize()
define t3_rpg_pronoun_nerdy_poss_cap = preferences.t3_rpg_pronoun_nerdy_poss.capitalize()
define t3_rpg_pronoun_nerdy_ref_cap = preferences.t3_rpg_pronoun_nerdy_ref.capitalize()

define t3_rpg_pronoun_sporty_sub_cap = preferences.t3_rpg_pronoun_sporty_sub.capitalize()

define t3_rpg_pronoun_perfect_sub_cap = preferences.t3_rpg_pronoun_perfect_sub.capitalize()
define t3_rpg_pronoun_perfect_obj_cap = preferences.t3_rpg_pronoun_perfect_obj.capitalize()
define t3_rpg_pronoun_perfect_pos_cap = preferences.t3_rpg_pronoun_perfect_pos.capitalize()
define t3_rpg_pronoun_perfect_poss_cap = preferences.t3_rpg_pronoun_perfect_poss.capitalize()
define t3_rpg_pronoun_perfect_ref_cap = preferences.t3_rpg_pronoun_perfect_ref.capitalize()

image dice_1 = ConditionSwitch(
    "game_state.t3_dice_roll_1 == 1", "dice 1",
    "game_state.t3_dice_roll_1 == 2", "dice 2",
    "game_state.t3_dice_roll_1 == 3", "dice 3",
    "game_state.t3_dice_roll_1 == 4", "dice 4",
    "game_state.t3_dice_roll_1 == 5", "dice 5",
    "game_state.t3_dice_roll_1 == 6", "dice 6"
)

image dice_2 = ConditionSwitch(
    "game_state.t3_dice_roll_2 == 1", "dice 1",
    "game_state.t3_dice_roll_2 == 2", "dice 2",
    "game_state.t3_dice_roll_2 == 3", "dice 3",
    "game_state.t3_dice_roll_2 == 4", "dice 4",
    "game_state.t3_dice_roll_2 == 5", "dice 5",
    "game_state.t3_dice_roll_2 == 6", "dice 6"
)

image dice_3 = ConditionSwitch(
    "game_state.t3_dice_roll_3 == 1", "dice 1",
    "game_state.t3_dice_roll_3 == 2", "dice 2",
    "game_state.t3_dice_roll_3 == 3", "dice 3",
    "game_state.t3_dice_roll_3 == 4", "dice 4",
    "game_state.t3_dice_roll_3 == 5", "dice 5",
    "game_state.t3_dice_roll_3 == 6", "dice 6"
)

image nerdy_icon = Composite(
    (315, 315),
    (0,0), ConditionSwitch(
        "game_state.t3_current_speaker == game_state.t3_player_nerdy", "active speaker background",
        "True", Null()
    ),
    (30, 29), "nerdy icon"
)

image sporty_icon = Composite(
    (315, 315),
    (0,0), ConditionSwitch(
        "game_state.t3_current_speaker == game_state.t3_player_sporty", "active speaker background",
        "True", Null()
    ),
    (30, 29), "sporty icon"
)

image perfect_icon = Composite(
    (315, 315),
    (0,0), ConditionSwitch(
        "game_state.t3_current_speaker == game_state.t3_player_perfect", "active speaker background",
        "True", Null()
    ),
    (30, 29), "perfect icon"
)

image villain_icon = Composite(
    (315, 315),
    (0,0), ConditionSwitch(
        "game_state.t3_current_speaker == game_state.t3_villain", "active speaker background",
        "True", Null()
    ),
    (30, 29), "boss grave knight"
)

image other_icon = Composite(
    (315, 315),
    (0,0), ConditionSwitch(
        "game_state.t3_current_speaker == game_state.t3_current_scenario.current_entity", "active speaker background",
        "True", Null()
    ),
    (30, 29), "[game_state.t3_current_scenario.current_entity.icon]"
)

init:
    transform centerleft:
        xalign 0.1
        yalign 0.5

    transform centerright:
        xalign 0.9
        yalign 0.5

    transform diceleft:
        xalign 0.4
        yalign 0.3

    transform dicecenter:
        xalign 0.5
        yalign 0.3

    transform diceright:
        xalign 0.6
        yalign 0.3

    transform topleftcenter:
        yalign 0
        xalign 0.35

    transform toprightcenter:
        yalign 0
        xalign 0.65

init python:
    def rpg_nerdy(what, **kwargs):
        game_state.t3_current_speaker = game_state.t3_player_nerdy
        rpg_nerdy_character(what, **kwargs)
        game_state.t3_current_speaker = None

    def rpg_sporty(what, **kwargs):
        game_state.t3_current_speaker = game_state.t3_player_sporty
        rpg_sporty_character(what, **kwargs)
        game_state.t3_current_speaker = None

    def rpg_perfect(what, **kwargs):
        game_state.t3_current_speaker = game_state.t3_player_perfect
        rpg_perfect_character(what, **kwargs)
        game_state.t3_current_speaker = None

    def rpg_villain(what, **kwargs):
        game_state.t3_current_speaker = game_state.t3_villain

        if game_state.t3_villain_known_name == game_state.t3_villain_actual_name:
            rpg_villain_character_known(what, **kwargs)
        else:
            rpg_villain_character_unknown(what, **kwargs)

        game_state.t3_current_speaker = None

    def rpg_other(what, **kwargs):
        game_state.t3_current_speaker = game_state.t3_current_scenario.current_entity
        game_state.t3_current_speaker.character(what, **kwargs)
        game_state.t3_current_speaker = None

# The game starts here.

label start:
    # Initialize the game state
    $ game_state = GameState()

label after_load:
    if game_state.t3_current_scenario and game_state.t3_current_scenario.current_entity:
        $ game_state.t3_current_scenario.current_entity.update_character_name(game_state.t3_current_scenario.current_entity.name)

label t3_introduction:
    # $ game_state.t3_current_scenario = game_state.t3_current_encounter.scenario_boss
    # jump expression game_state.t3_current_encounter.scenario_boss.script
    # $ game_state.t3_current_scenario = game_state.t3_current_encounter.scenario_quest
    # jump t3_scenario_field_quest
    $ game_state.t3_current_scenario = game_state.t3_current_encounter.scenario_objective
    jump t3_scenario_field_objective

    scene bg sunny

    pause 1.5

    sporty "Ugh... {p=0.5}So hot..."
    sporty "With that sun, you'd never believe summer's almost over."

    pause 1.5

    perfect "Is this it, [preferences.t3_char_nerdy_name]? The game you wanted to show us?"

    scene bg room day open

    show nerdy casual 8 at topleft with dissolve

    nerdy "Yes. I wrote it so we can play together."

    show sporty casual 49 at top with dissolve

    sporty "So cool!"
    sporty "I can't wait to find out what it's about."

    show perfect casual 3 at topright with dissolve

    perfect "Indeed."
    perfect "It's really impressive you were able to pull everything together so quickly. That's our [preferences.t3_char_nerdy_name] for you."

    show nerdy casual 1

    nerdy "Thank you."
    nerdy "Is it okay if we get started now?"

    show sporty casual 3
    
    sporty "Sure, I'm game. Just don't cry when I beat the pants off you two."

    show perfect casual 37

    perfect "Oh my, you sure do sound confident, [preferences.t3_char_sporty_name]."
    perfect "Overconfident, some might say."

    show nerdy casual 8

    nerdy "It's not really that kind of game."

    show sporty casual 10

    sporty "Oh, really? What kind of game is it, then?"

    nerdy "A cooperative game."

    show perfect casual 2

    perfect "Oh! Of course, that would be perfect for the three of us."
    
    show sporty casual 1

    sporty "Right, since we're best friends and all."

    show nerdy casual 1

    nerdy "I'll explain the game now."

    show sporty casual 1
    show perfect casual 1

    show nerdy casual 8

    nerdy "This is a role-playing game in a fantasy setting with humans, monsters, fairies, and sorcerers."
    nerdy "Entire human villages have started disappearing off the map and no one knows why."
    nerdy "We have to work together to uncover what's happening and put a stop to it before more innocent lives are lost."

    show nerdy casual 1

    nerdy "Each of us will create a character with set attributes. One attribute will be a strength and one will be a weakness."
    nerdy "The available attributes are {color=#6684a3}Style{/color}, {color=#6684a3}Magic{/color}, and {color=#6684a3}Wisdom{/color}."
    nerdy "These attributes determine what actions we can take in the world."

    show sporty casual 26

    sporty "Ooh, I already know which one I'm gonna pick."

    show perfect casual 3

    perfect "Indeed, I'm already thinking about the perfect character."

    show nerdy casual 8

    nerdy "Each time you perform an action, you roll the dice."
    nerdy "If you roll higher than the attribute you have, you get to perform the action."
    nerdy "If you don't, you fail."

    show sporty casual 16

    sporty "Uh oh, how much failure are we talking about here?"

    show perfect casual 1

    perfect "It just means you should try to play to your strengths and minimize your weaknesses."
    perfect "That's the basis of any good strategy."

    show nerdy casual 1

    nerdy "Let's create our characters now."
    nerdy "Give yourself a name, a backstory, a strong attribute, and a weak attribute."

label t3_introduction_sporty_character_creation:
    $ game_state.t3_attribute_points_to_allocate = preferences.t3_rpg_attribute_total_points
    $ game_state.t3_attribute_novice_chosen = False
    $ game_state.t3_attribute_average_chosen = False
    $ game_state.t3_attribute_expert_chosen = False

    show nerdy casual 1 at topleft
    show sporty casual 1 at top
    show perfect casual 1 at topright

    sporty "Let's see..."
    sporty "I'll be... um... wait, I know! I'll be {color=#6684a3}[preferences.t3_rpg_char_sporty_name]{/color}. That's a cool name, right?"

    show sporty casual 35

    sporty "And my strength is definitely {color=#6684a3}Style.{/color}"
    sporty "I'll be a super rad [preferences.t3_rpg_char_sporty_title], riding my skateboard around and doing sweet tricks only I can do."

    show perfect casual 4

    perfect "A [preferences.t3_rpg_char_sporty_title] on a skateboard? Is that even allowed?"

    show nerdy casual 8

    nerdy "It's fine. There are no rules against it."

    show sporty casual 66

    sporty "Yay! This is gonna be awesome!"

    show sporty casual 1

    sporty "Oh, and my weakness will be..."

    show perfect casual 3

    perfect "It should be {color=#6684a3}Wisdom{/color}, don't you think?"
    perfect "Considering your grades, I mean."

    show sporty casual 15

    sporty "...Sure, we'll go with that."

    show nerdy casual 1

    nerdy "Okay."
    nerdy "Other than your designated strength and weakness, you can allocate up to {color=#6684a3}[preferences.t3_rpg_attribute_total_points]{/color} points on individual attributes."

    show sporty casual 11

    sporty "What's the point of that when I just told you what I'm good at?"

    show nerdy casual 8

    nerdy "The points are what dice rolls are checked against."
    nerdy "The strength you chose will apply an extra point to the attribute value when checked, while the weakness you chose will subtract a point."

    show perfect casual 1

    perfect "So you could allocate more points to the same attribute as your weakness to offset the effect?"
    perfect "That's interesting."

    show nerdy casual 1
    nerdy "How would you like to allocate your points, [preferences.t3_char_sporty_name]?"

    show sporty casual 1

    # TODO: Implement automatic attribute allocation

    sporty "Hmm... I'm honestly not so good with these kinds of games."
    sporty "Will you help me choose, [preferences.t3_char_nerdy_name]?"

    menu:
        "How much {color=#6684a3}Style{/color} should [preferences.t3_char_sporty_name]'s character {color=#6684a3}[preferences.t3_rpg_char_sporty_name]{/color} have?"
        
        "Novice":
            $ game_state.t3_player_sporty.style = int(game_state.calculate_attribute_allocation(AttributeAllocation.Novice))
            $ game_state.t3_attribute_points_to_allocate -= game_state.t3_player_sporty.style
            $ game_state.t3_attribute_novice_chosen = True

            show nerdy casual 8

            nerdy "You should choose a {color=#6684a3}Novice{/color} amount of {color=#6684a3}Style{/color}."

            show perfect casual 4

            perfect "But [preferences.t3_pronoun_sporty_pos] character's strength is {color=#6684a3}Style{/color}, right? Are you sure you want to do that?"

            show sporty casual 3

            sporty "Of course, it makes perfect sense!"
            sporty "If my strength is {color=#6684a3}Style{/color}, I get a bonus, right? So I don't need to allocate as many points to it."

            show perfect casual 1

            perfect "If you say so, but that seems like a risky strategy to me."
        "Average":
            $ game_state.t3_player_sporty.style = int(game_state.calculate_attribute_allocation(AttributeAllocation.Average))
            $ game_state.t3_attribute_points_to_allocate -= game_state.t3_player_sporty.style
            $ game_state.t3_attribute_average_chosen = True

            show nerdy casual 8

            nerdy "You should choose an {color=#6684a3}Average{/color} amount of {color=#6684a3}Style{/color}."

            show perfect casual 9

            perfect "But [preferences.t3_pronoun_sporty_pos] character's strength is {color=#6684a3}Style{/color}, right? Why only Average?"

            show sporty casual 3

            sporty "For a [preferences.t3_rpg_char_sporty_title], even an average amount of {color=#6684a3}Style{/color} is still way more than anyone else."
            sporty "I'm sure I'll be fine."

            show perfect casual 3

            perfect "You really are confident, aren't you?"
        "Expert":
            $ game_state.t3_player_sporty.style = int(game_state.calculate_attribute_allocation(AttributeAllocation.Expert))
            $ game_state.t3_attribute_points_to_allocate -= game_state.t3_player_sporty.style
            $ game_state.t3_attribute_expert_chosen = True

            show nerdy casual 8

            nerdy "You should choose an {color=#6684a3}Expert{/color} amount of {color=#6684a3}Style{/color}."

            show perfect casual 2

            perfect "Of course, that makes perfect sense."
            perfect "All that {color=#6684a3}Style{/color} will play to [preferences.t3_pronoun_sporty_pos] strengths quite nicely."

            show sporty casual 3

            sporty "I know, right? I'm gonna be unstoppable with my amazing {color=#6684a3}Style{/color}!"

    show nerdy casual 1

    nerdy "{color=#6684a3}[preferences.t3_rpg_char_sporty_name]{/color} now has [game_state.t3_player_sporty.style] {color=#6684a3}Style{/color} points and {color=#6684a3}[game_state.t3_attribute_points_to_allocate]{/color} points left to allocate."
    nerdy "Next is {color=#6684a3}Magic{/color}."

    show sporty casual 1

    menu:
        "How much {color=#6684a3}Magic{/color} should [preferences.t3_char_sporty_name]'s character {color=#6684a3}[preferences.t3_rpg_char_sporty_name]{/color} have?"
        
        "Novice" if game_state.t3_attribute_points_to_allocate >= int(game_state.calculate_attribute_allocation(AttributeAllocation.Novice)):
            $ game_state.t3_player_sporty.magic = int(game_state.calculate_attribute_allocation(AttributeAllocation.Novice))
            $ game_state.t3_attribute_points_to_allocate -= game_state.t3_player_sporty.magic

            show nerdy casual 8

            nerdy "You should choose a {color=#6684a3}Novice{/color} amount of {color=#6684a3}Magic{/color}."

            show perfect casual 1
            
            perfect "Don't you think a [preferences.t3_rpg_char_sporty_title] should have more {color=#6684a3}Magic{/color} than that?"

            show sporty casual 14

            sporty "I'm not sure what I'd do with a bunch of magic, anyway."

            show sporty casual 9

            sporty "I'd rather just punch and kick my way out of things, ya know?"

            show perfect casual 9

            perfect "That sounds rather violent..."
            
        "Average" if game_state.t3_attribute_points_to_allocate >= int(game_state.calculate_attribute_allocation(AttributeAllocation.Average)):
            $ game_state.t3_player_sporty.magic = int(game_state.calculate_attribute_allocation(AttributeAllocation.Average))
            $ game_state.t3_attribute_points_to_allocate -= game_state.t3_player_sporty.magic

            show nerdy casual 8

            nerdy "You should choose an {color=#6684a3}Average{/color} amount of {color=#6684a3}Magic{/color}."

            show perfect casual 2

            perfect "That would make sense, wouldn't it?"
            perfect "A [preferences.t3_rpg_char_sporty_title] should have at least an {color=#6684a3}Average{/color} amount of {color=#6684a3}Magic{/color}."

            show sporty casual 26

            sporty "That's right! I can't wait to show off some cool magic spells."
            
        "Expert" if game_state.t3_attribute_points_to_allocate >= int(game_state.calculate_attribute_allocation(AttributeAllocation.Expert)):
            $ game_state.t3_player_sporty.magic = int(game_state.calculate_attribute_allocation(AttributeAllocation.Expert))
            $ game_state.t3_attribute_points_to_allocate -= game_state.t3_player_sporty.magic

            show nerdy casual 8

            nerdy "You should choose an {color=#6684a3}Expert{/color} amount of {color=#6684a3}Magic{/color}."

            show perfect casual 37

            perfect "Oh my, sounds like I might have some competition."

            show sporty casual 6

            sporty "Planning on making a {color=#6684a3}Magic{/color}-based character, huh?"

            show sporty casual 2

            sporty "Alrighty then, let the best magician win!"

    show nerdy casual 1

    nerdy "{color=#6684a3}[preferences.t3_rpg_char_sporty_name]{/color} now has [game_state.t3_player_sporty.magic] {color=#6684a3}Magic{/color} points and {color=#6684a3}[game_state.t3_attribute_points_to_allocate]{/color} points left to allocate."

    nerdy "Let's go ahead and allocate your remaining points to {color=#6684a3}Wisdom{/color}."

    $ game_state.t3_player_sporty.wisdom = game_state.t3_attribute_points_to_allocate

    nerdy "{color=#6684a3}[preferences.t3_rpg_char_sporty_name]{/color} now has [game_state.t3_player_sporty.wisdom] {color=#6684a3}Wisdom{/color} points."

    show perfect casual 1
    show sporty casual 32

    sporty "Yay, thank you! I'm so excited!"

label t3_introduction_perfect_character_creation:
    $ game_state.t3_attribute_points_to_allocate = preferences.t3_rpg_attribute_total_points

    show nerdy casual 1 at topleft
    show sporty casual 1 at top
    show perfect casual 1 at topright

    sporty "Now it's your turn, right, [preferences.t3_char_perfect_name]?"

    show perfect casual 2

    perfect "Sure, I can go next."
    perfect "My character will be {color=#6684a3}[preferences.t3_rpg_char_perfect_name]{/color}, an elegant [preferences.t3_rpg_char_perfect_title] whose strength is {color=#6684a3}Magic{/color}."

    show perfect casual 3

    perfect "[t3_rpg_pronoun_perfect_sub_cap] has no equal and no weakness."

    show sporty casual 29

    sporty "No weakness? Hey, that's no fair. [preferences.t3_char_nerdy_name] said everybody has to have a weakness."

    show nerdy casual 8

    nerdy "It's fine. I'll allow it."

    show sporty casual 21

    sporty "Huh? Is that seriously okay?"

    show nerdy casual 1

    nerdy "The penalty for a weakness is small, and {color=#6684a3}Magic{/color} is more limited in its use than the other attributes."
    nerdy "It balances out. Are you okay with that?"

    show perfect casual 9

    perfect "Sorry, I didn't mean to cause such a fuss. I can take it back if you want me to, [preferences.t3_char_sporty_name]."

    show sporty casual 15

    sporty "Nah, I guess it's fine."

    show sporty casual 1

    sporty "It's just a game, right? The important thing is for everybody to have fun."

    show perfect casual 2

    perfect "Thank you! I promise not to make myself too over-powered."

    show nerdy casual 8

    nerdy "Let's allocate your character's points, [preferences.t3_char_perfect_name]."

    show perfect casual 1

    # TODO: Implement automatic attribute allocation

    perfect "Actually, could you help me, [preferences.t3_char_nerdy_name]?"
    perfect "You did such a good job of helping [preferences.t3_char_sporty_name] decide on [preferences.t3_pronoun_sporty_poss]."

    menu:
        "How much {color=#6684a3}Style{/color} should [preferences.t3_char_perfect_name]'s character {color=#6684a3}[preferences.t3_rpg_char_perfect_name]{/color} have?"
        
        "Novice":
            $ game_state.t3_player_perfect.style = int(game_state.calculate_attribute_allocation(AttributeAllocation.Novice))
            $ game_state.t3_attribute_points_to_allocate -= game_state.t3_player_perfect.style

            show nerdy casual 1

            nerdy "You should choose a {color=#6684a3}Novice{/color} amount of {color=#6684a3}Style{/color}."

            show perfect casual 30

            perfect "Oh, that's... an interesting choice."

            show sporty casual 57

            sporty "Ha. Sounds like your super-powerful character is going to be super boring."

            show perfect casual 15

            perfect "Not at all! It just means I have more points to spend on more important things."

            show perfect casual 2

            perfect "Excellent choice, [preferences.t3_char_nerdy_name]. Thank you."
            
        "Average":
            $ game_state.t3_player_perfect.style = int(game_state.calculate_attribute_allocation(AttributeAllocation.Average))
            $ game_state.t3_attribute_points_to_allocate -= game_state.t3_player_perfect.style

            show nerdy casual 1

            nerdy "You should choose an {color=#6684a3}Average{/color} amount of {color=#6684a3}Style{/color}."

            show sporty casual 6

            sporty "Hey, just like real life."

            show perfect casual 2

            perfect "I'm fine with that. My [preferences.t3_rpg_char_perfect_title] doesn't need to be flashy in order to make a powerful entrance."
            
        "Expert":
            $ game_state.t3_player_perfect.style = int(game_state.calculate_attribute_allocation(AttributeAllocation.Expert))
            $ game_state.t3_attribute_points_to_allocate -= game_state.t3_player_perfect.style

            show nerdy casual 1

            nerdy "You should choose an {color=#6684a3}Expert{/color} amount of {color=#6684a3}Style{/color}."

            show perfect casual 3

            perfect "Oh, you really think I'm that stylish?"

            show sporty casual 16

            sporty "Not you, your character."

            show perfect casual 2

            perfect "I know, but it makes me happy all the same."

    show nerdy casual 8

    nerdy "{color=#6684a3}[preferences.t3_rpg_char_perfect_name]{/color} now has [game_state.t3_player_perfect.style] {color=#6684a3}Style{/color} points and {color=#6684a3}[game_state.t3_attribute_points_to_allocate]{/color} points left to allocate."
    nerdy "Next is {color=#6684a3}Magic{/color}."

    show perfect casual 1

    menu:
        "How much {color=#6684a3}Magic{/color} should [preferences.t3_char_perfect_name]'s character {color=#6684a3}[preferences.t3_rpg_char_perfect_name]{/color} have?"
        
        "Novice" if game_state.t3_attribute_points_to_allocate >= int(game_state.calculate_attribute_allocation(AttributeAllocation.Novice)):
            $ game_state.t3_player_perfect.magic = int(game_state.calculate_attribute_allocation(AttributeAllocation.Novice))
            $ game_state.t3_attribute_points_to_allocate -= game_state.t3_player_perfect.magic

            show nerdy casual 1

            nerdy "You should choose a {color=#6684a3}Novice{/color} amount of {color=#6684a3}Magic{/color}."

            show perfect casual 33

            perfect "Wait, what? But my strength is {color=#6684a3}Magic{/color}! Surely I should have more {color=#6684a3}Magic{/color} points than that."

            show sporty casual 15

            sporty "Don't tell me you're questioning the wisdom of the great [preferences.t3_char_nerdy_name]."

            show perfect casual 26

            perfect "...Of course not. Forgive me, [preferences.t3_char_nerdy_name]."
            
        "Average" if game_state.t3_attribute_points_to_allocate >= int(game_state.calculate_attribute_allocation(AttributeAllocation.Average)):
            $ game_state.t3_player_perfect.magic = int(game_state.calculate_attribute_allocation(AttributeAllocation.Average))
            $ game_state.t3_attribute_points_to_allocate -= game_state.t3_player_perfect.magic

            show nerdy casual 1

            nerdy "You should choose an {color=#6684a3}Average{/color} amount of {color=#6684a3}Magic{/color}."

            show perfect casual 8

            perfect "I would have expected a little more {color=#6684a3}Magic{/color}, but I suppose having a well-rounded character is a sound strategy."

            show sporty casual 10

            sporty "Now that you mention it, that's not a bad idea."
            
            show perfect casual 2

            perfect "That's right. If you allocated the same amount of points to every attribute, you'd be able to handle any situation."
            
        "Expert" if game_state.t3_attribute_points_to_allocate >= int(game_state.calculate_attribute_allocation(AttributeAllocation.Expert)):
            $ game_state.t3_player_perfect.magic = int(game_state.calculate_attribute_allocation(AttributeAllocation.Expert))
            $ game_state.t3_attribute_points_to_allocate -= game_state.t3_player_perfect.magic

            show nerdy casual 1

            nerdy "You should choose an {color=#6684a3}Expert{/color} amount of {color=#6684a3}Magic{/color}."

            show perfect casual 3

            perfect "Naturally. Since my strength is {color=#6684a3}Magic{/color}, it makes sense for me to have a lot of {color=#6684a3}Magic{/color} points."

            show sporty casual 11

            sporty "Just don't go overboard with all the {color=#6684a3}Magic{/color} stuff, alright?"

            show perfect casual 2

            perfect "Of course not. I promised to play fair."

    show nerdy casual 8
    show sporty casual 1

    nerdy "{color=#6684a3}[preferences.t3_rpg_char_perfect_name]{/color} now has [game_state.t3_player_perfect.magic] {color=#6684a3}Magic{/color} points and {color=#6684a3}[game_state.t3_attribute_points_to_allocate]{/color} points left to allocate."

    nerdy "Let's go ahead and allocate your remaining points to {color=#6684a3}Wisdom{/color}."

    $ game_state.t3_player_perfect.wisdom = game_state.t3_attribute_points_to_allocate

    nerdy "{color=#6684a3}[preferences.t3_rpg_char_perfect_name]{/color} now has [game_state.t3_player_perfect.wisdom] {color=#6684a3}Wisdom{/color} points."

    show perfect casual 3

    perfect "Perfect! Thank you so much for your help."

    show sporty casual 24

    sporty "Now we're ready to start, right? I can't wait! Let's go!"

label t3_introduction_nerdy_character_creation:
    $ game_state.t3_attribute_points_to_allocate = preferences.t3_rpg_attribute_total_points

    show nerdy casual 8 at topleft
    show sporty casual 24 at top
    show perfect casual 1 at topright

    perfect "Not so fast. What about your character, [preferences.t3_char_nerdy_name]?"

    show nerdy casual 1

    nerdy "My character will be {color=#6684a3}[preferences.t3_rpg_char_nerdy_name]{/color}, more commonly known as the [preferences.t3_rpg_char_nerdy_title]."
    nerdy "[t3_rpg_pronoun_nerdy_pos_cap] strength is {color=#6684a3}Wisdom{/color} and [preferences.t3_rpg_pronoun_nerdy_pos] weakness is {color=#6684a3}Style{/color}."

    show sporty casual 6

    sporty "[preferences.t3_rpg_char_nerdy_title], huh? That does seem like the kinda thing you'd come up with."

    show perfect casual 3

    perfect "Indeed. It seems very fitting for our [preferences.t3_char_nerdy_name]."

    show nerdy casual 8

    nerdy "For my character's attributes..."

    menu:
        "How much {color=#6684a3}Style{/color} should my character {color=#6684a3}[preferences.t3_rpg_char_nerdy_name]{/color} have?"
        
        "Novice":
            $ game_state.t3_player_nerdy.style = int(game_state.calculate_attribute_allocation(AttributeAllocation.Novice))
            $ game_state.t3_attribute_points_to_allocate -= game_state.t3_player_nerdy.style

            show nerdy casual 1

            nerdy "I'll choose a {color=#6684a3}Novice{/color} amount of {color=#6684a3}Style{/color}."

            show perfect casual 3

            perfect "Well, that does make sense considering your character's strength and weakness."

            show sporty casual 3

            sporty "Don't worry, my character's got enough {color=#6684a3}Style{/color} for all three of us."
            
        "Average":
            $ game_state.t3_player_nerdy.style = int(game_state.calculate_attribute_allocation(AttributeAllocation.Average))
            $ game_state.t3_attribute_points_to_allocate -= game_state.t3_player_nerdy.style

            show nerdy casual 1

            nerdy "I'll choose an {color=#6684a3}Average{/color} amount of {color=#6684a3}Style{/color}."

            show perfect casual 2

            perfect "That makes sense. Not too high, not too low."

            show sporty casual 14

            sporty "You don't have to react to every single choice, ya know."

            show perfect casual 1

            perfect "How else will [preferences.t3_pronoun_nerdy_sub] know whether I approve of [preferences.t3_pronoun_nerdy_pos] choices or not?"

            show sporty casual 16

            sporty "Why does it matter if you approve or not? It's [preferences.t3_pronoun_nerdy_pos] character."
            
        "Expert":
            $ game_state.t3_player_nerdy.style = int(game_state.calculate_attribute_allocation(AttributeAllocation.Expert))
            $ game_state.t3_attribute_points_to_allocate -= game_state.t3_player_nerdy.style

            show nerdy casual 1

            nerdy "I'll choose an {color=#6684a3}Expert{/color} amount of {color=#6684a3}Style{/color}."

            show perfect casual 2

            perfect "I've never heard of a [preferences.t3_rpg_char_nerdy_title] with a lot of {color=#6684a3}Style{/color}, but if anyone can make it work, you can."

            show sporty casual 36

            sporty "We can be the Stylish Duo!"

            show perfect casual 4

            perfect "And what am I? Chopped liver?"

            show sporty casual 15

            sporty "Fine, fine, we'll the Stylish Trio."

            show perfect casual 3

            perfect "That's better."

    show nerdy casual 8

    nerdy "{color=#6684a3}[preferences.t3_rpg_char_nerdy_name]{/color} now has [game_state.t3_player_nerdy.style] {color=#6684a3}Style{/color} points and {color=#6684a3}[game_state.t3_attribute_points_to_allocate]{/color} points left to allocate."
    nerdy "Next is {color=#6684a3}Magic{/color}."

    menu:
        "How much {color=#6684a3}Magic{/color} should my character {color=#6684a3}[preferences.t3_rpg_char_nerdy_name]{/color} have?"
        
        "Novice" if game_state.t3_attribute_points_to_allocate >= int(game_state.calculate_attribute_allocation(AttributeAllocation.Novice)):
            $ game_state.t3_player_nerdy.magic = int(game_state.calculate_attribute_allocation(AttributeAllocation.Novice))
            $ game_state.t3_attribute_points_to_allocate -= game_state.t3_player_nerdy.magic

            show nerdy casual 1

            nerdy "I'll choose a {color=#6684a3}Novice{/color} amount of {color=#6684a3}Magic{/color}."

            show perfect casual 9

            perfect "Really? Somehow I expected you to choose a higher level of {color=#6684a3}Magic{/color}."

            show sporty casual 30

            sporty "I mean, it's [preferences.t3_pronoun_nerdy_pos] character. [t3_pronoun_nerdy_sub_cap] can do whatever [preferences.t3_pronoun_nerdy_sub] wants."

            show perfect casual 1

            perfect "Yes, sorry, I didn't mean to imply that [preferences.t3_pronoun_nerdy_sub] did something wrong."
            
        "Average" if game_state.t3_attribute_points_to_allocate >= int(game_state.calculate_attribute_allocation(AttributeAllocation.Average)):
            $ game_state.t3_player_nerdy.magic = int(game_state.calculate_attribute_allocation(AttributeAllocation.Average))
            $ game_state.t3_attribute_points_to_allocate -= game_state.t3_player_nerdy.magic

            show nerdy casual 1

            nerdy "I'll choose an {color=#6684a3}Average{/color} amount of {color=#6684a3}Magic{/color}."

            show perfect casual 2

            perfect "Yes, going for a balanced amount of {color=#6684a3}Magic{/color} seems like the sensible choice."

            show sporty casual 15

            sporty "I bet you just want to keep all the {color=#6684a3}Magic{/color} to yourself."

            show perfect casual 9

            perfect "Nothing of the sort! I just think it's nice that [preferences.t3_pronoun_nerdy_pos] character has some {color=#6684a3}Magic{/color}."
            
        "Expert" if game_state.t3_attribute_points_to_allocate >= int(game_state.calculate_attribute_allocation(AttributeAllocation.Expert)):
            $ game_state.t3_player_nerdy.magic = int(game_state.calculate_attribute_allocation(AttributeAllocation.Expert))
            $ game_state.t3_attribute_points_to_allocate -= game_state.t3_player_nerdy.magic

            show nerdy casual 1

            nerdy "I'll choose an {color=#6684a3}Expert{/color} amount of {color=#6684a3}Magic{/color}."

            show perfect casual 3

            perfect "I see you, too, understand the value and potential of great {color=#6684a3}Magic{/color}."

            show sporty casual 9

            sporty "Just don't turn me into a frog or something, m'kay?"

    show nerdy casual 8
    show sporty casual 1
    show perfect casual 1

    nerdy "{color=#6684a3}[preferences.t3_rpg_char_nerdy_name]{/color} now has [game_state.t3_player_nerdy.magic] {color=#6684a3}Magic{/color} points and {color=#6684a3}[game_state.t3_attribute_points_to_allocate]{/color} points left to allocate."

    nerdy "Let's go ahead and allocate my remaining points to {color=#6684a3}Wisdom{/color}."

    $ game_state.t3_player_nerdy.wisdom = game_state.t3_attribute_points_to_allocate

    nerdy "{color=#6684a3}[preferences.t3_rpg_char_nerdy_name]{/color} now has [game_state.t3_player_nerdy.wisdom] {color=#6684a3}Wisdom{/color} points."

    show nerdy casual 3

    nerdy "I think we have a well-rounded party. I'm happy."

    show sporty casual 22

    sporty "Finally! I'm ready to kick the crap out of some monsters."

    show perfect casual 3

    perfect "Indeed. I'm excited to get started as well."

    show nerdy casual 8

    nerdy "Okay, let's begin."

label t3_start_game:
    # Start the RPG portion of the game

    call expression game_state.t3_current_encounter.script

    "We're back at the start label."

    # This ends the game.

    return
