label encounter_field_start:

    nerdy "I will now explain how to play the game. It all started on a dark, dreary night..."

    sporty "Wait, that's too dull. Let's do something bright and colorful!"

    perfect "How about a nice, green field? I've heard of games starting with peaceful scenery."

    nerdy "Very well. It all started in a peaceful, fantastical field..."

    "The current encounter's theme is [rpg_current_encounter.theme]. It's expected to have this many scenarios: [rpg_current_encounter.number_of_scenarios]."
    $ actual_number_of_scenarios = len(rpg_current_encounter.scenarios)
    "It actually has this many scenarios: [actual_number_of_scenarios]"

    $ i = 0
    while i < actual_number_of_scenarios:
        call expression rpg_current_encounter.scenarios[i].script

        $ remaining_players = rpg_current_encounter.get_active_players()
        
        # check if anyone is still alive
        if len(remaining_players) <= 0:
            jump encounter_field_failure

        $ i += 1
        
    jump encounter_field_success

label encounter_field_success:
    "You won!"

    return

label encounter_field_failure:
    "You lost..."

    return