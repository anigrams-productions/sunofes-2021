# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define nerdy = Character(preferences.t3_char_nerdy_name, color="#827281")
define sporty = Character(preferences.t3_char_sporty_name, color="#e5914f")
define perfect = Character(preferences.t3_char_perfect_name, color="#e3848e")

define rpg_nerdy = Character(preferences.t3_rpg_char_nerdy_name, color="#827281")
define rpg_sporty = Character(preferences.t3_rpg_char_sporty_name, color="#e5914f")
define rpg_perfect = Character(preferences.t3_rpg_char_perfect_name, color="#e3848e")

# The game starts here.

label start:
    # Initialize the game state
    $ game_state = GameState()

label t3_introduction:
    scene bg sunny

    sporty "So hot..."
    sporty "From this heat, you'd never guess summer's almost over."

    perfect "Is this it, [preferences.t3_char_nerdy_name]? The game you wanted to show us?"

    scene bg room day open

    show nerdy casual 8 at topleft

    nerdy "Yes. I wrote it so we can play together."

    show sporty casual 49 at top

    sporty "So cool!"
    sporty "I can't wait to find out what it's about."

    show perfect casual 3 at topright

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

    show nerdy casual 1

    nerdy "Good. I'll explain the game now."

    show sporty casual 1
    show perfect casual 1

    show nerdy casual 8

    nerdy "This is a role-playing game in a fantasy setting with humans, monsters, fairies, and sorcerers."
    nerdy "[preferences.t3_rpg_char_villain_title] has cursed the humans of the land, turning them into monsters."
    nerdy "We have to work together to defeat [preferences.t3_rpg_char_villain_title] and break the curse."

    show nerdy casual 1

    nerdy "Each of us will create a character with set attributes. One attribute will be a strength and one will be a weakness."
    nerdy "The available attributes are Style, Magic, and Wisdom."
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

    nerdy "Yes. Let's create our characters."
    nerdy "Give yourself a name, a backstory, a strong attribute, and a weak attribute."

    show sporty casual 1

    sporty "Let's see..."
    sporty "I'll be... um... wait, I know! I'll be [preferences.t3_rpg_char_sporty_name]. That's a cool name, right?"

    show sporty casual 35

    sporty "And my strength is definitely Style."
    sporty "I'll be a super rad [preferences.t3_rpg_char_sporty_title], riding my skateboard around and doing sweet tricks only a fairy can do."

    show perfect casual 4

    perfect "A [preferences.t3_rpg_char_sporty_title] on a skateboard? Is that even allowed?"

    show nerdy casual 8

    nerdy "It's fine. There are no rules against it."

    show sporty casual 66

    sporty "Yay! This is gonna be awesome!"

    show sporty casual 1

    sporty "Oh, and my weakness will be..."

    show perfect casual 3

    perfect "It should be Wisdom, don't you think?"
    perfect "Considering your grades, I mean."

    show sporty casual 15

    sporty "...Sure, we'll go with that."

    show nerdy casual 1

    nerdy "Okay."
    nerdy "Other than your designated strength and weakness, you can allocate up to [preferences.t3_rpg_attribute_total_points] points on individual attributes."

    show sporty casual 11

    sporty "What's the point of that when I just told you what I'm good at?"

    show nerdy casual 8

    nerdy "The points are what dice rolls are checked against."
    nerdy "The strength you chose will apply an extra point to the attribute value when checked, while the weakness you chose will subtract a point."

    show perfect casual 1

    perfect "So you could allocate more points to the attribute you're weak to in order to offset the weakness?"
    perfect "That's interesting."

    show nerdy casual 1
    nerdy "Yes. How would you like to allocate your points, [preferences.t3_char_sporty_name]?"

    show sporty casual 1

    menu:
        "How much Style should [preferences.t3_char_sporty_name]'s character [preferences.t3_rpg_char_sporty_name] have?"
        
        "Novice":
            $ game_state.t3_player_sporty.style = int(game_state.calculate_attribute_allocation(AttributeAllocation.Novice))
            $ game_state.t3_attribute_points_to_allocate -= game_state.t3_player_sporty.style
            $ game_state.t3_attribute_novice_chosen = True

            sporty "I think I'll choose a Novice amount of Style."

            show perfect casual 4

            perfect "But your character's strength is Style, right? Are you sure you want to do that?"

            show sporty casual 3

            sporty "Of course, it makes perfect sense!"
            sporty "If my strength is Style, I get a bonus, right? So I don't need to allocate as many points to it."

            show perfect casual 1

            perfect "If you say so, but that seems like a risky strategy to me."
        "Average":
            $ game_state.t3_player_sporty.style = int(game_state.calculate_attribute_allocation(AttributeAllocation.Average))
            $ game_state.t3_attribute_points_to_allocate -= game_state.t3_player_sporty.style
            $ game_state.t3_attribute_average_chosen = True

            sporty "I think I'll choose an Average amount of Style."

            show perfect casual 9

            perfect "Your character's strength is Style, right? Why only Average?"

            show sporty casual 3

            sporty "For a [preferences.t3_rpg_char_sporty_title], even an average amount of Style is still way more than anyone else."
            sporty "I'm sure I'll be fine."

            show perfect casual 3

            perfect "You really are confident, aren't you?"
        "Expert":
            $ game_state.t3_player_sporty.style = int(game_state.calculate_attribute_allocation(AttributeAllocation.Expert))
            $ game_state.t3_attribute_points_to_allocate -= game_state.t3_player_sporty.style
            $ game_state.t3_attribute_expert_chosen = True

            sporty "I think I'll choose an Expert amount of Style."

            show perfect casual 2

            perfect "Of course, that makes perfect sense."
            perfect "All that Style will play to your strengths quite nicely."

            show sporty casual 3

            sporty "I know, right? I'm gonna be unstoppable with my amazing Style!"

    show nerdy casual 8

    nerdy "[preferences.t3_rpg_char_sporty_name] now has [game_state.t3_player_sporty.style] Style points and [game_state.t3_attribute_points_to_allocate] points left to allocate."
    nerdy "Next is Magic."

    show sporty casual 1

    ## Start the RPG portion of the game

    # call expression game_state.t3_current_encounter.script

    # "We're back at the start label."

    # This ends the game.

    return
