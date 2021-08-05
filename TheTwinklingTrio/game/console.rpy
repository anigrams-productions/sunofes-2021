## This file adds custom console commands to the ones that already exist by default in Ren'Py.
## It can also be used to override the existing console commands.
## The console can be opened anytime during the game with Shift+O.

## NOTE: Because this code is executed extremely early, none of the normally accessibly global variables are accessible.
## Use renpy.python.py_exec() and renpy.python.py_eval() instead.

init -1500 python in _console:
    def public_command(help=None):
        def wrap(f):
            f.help = help
            f.public = True
            config.console_commands[f.__name__] = f
            return f

        return wrap

    def public_commands():
        filtered_commands = []

        for (key, value) in config.console_commands.items():
            if hasattr(value, 'public') and value.public:
                filtered_commands.append(key)

        return filtered_commands

    def get_character_code_name(char_type, name):
        name = name.lower()
        alt_name_1 = None
        alt_name_2 = None

        if name == char_type.lower():
            return name

        try:
            alt_name_1 = renpy.python.py_eval("preferences.t3_char_" + char_type + "_name")
        except:
            pass

        try:
            alt_name_2 = renpy.python.py_eval("preferences.t3_rpg_char_" + char_type + "_name")
        except:
            pass

        if name == alt_name_1.lower() or name == alt_name_2.lower():
            return char_type
        else:
            return None

    ## Override the default help command
    @command(_("help: List available console commands"))
    def help(l):
        keys = public_commands()
        keys.sort()

        rv = __("commands:\n")

        for k in keys:
            f = config.console_commands[k]
            if f.help is None:
                continue

            rv += " " + __(f.help) + "\n"

        return rv


    ## "Private" (hidden) commands

    @command()
    def foo(l):
        return help("help")

    @command()
    def bar(l):
        return help("help")

    @command()
    def cera(l):
        return "I'm Cera White and this is my favorite game on the Internet."


    ## Public versions of existing commands so they'll show up under the new help() method

    @public_command(_("clear: Clear the console history"))
    def clear(l):
        console.history[:] = [ ]

    @public_command(_("exit: Exit the console and clear the console history"))
    def exit(l):
        clear(l)
        renpy.jump("_console_return")

    @public_command(_("reload: Reload the game, refreshing the scripts"))
    def reload(l):
        store._reload_game()

    @public_command(_("jump <label>: Jump to label"))
    def jump(l):
        label = l.label_name()

        if label is None:
            raise Exception("Could not parse label. (Unqualified local labels are not allowed.)")

        if not console.can_renpy():
            raise Exception("Ren'Py script not enabled. Not jumping.")

        if not renpy.has_label(label):
            raise Exception("Label %s not found." % label)

        renpy.pop_call()
        renpy.jump(label)


    ## New public commands specific to this game

    @public_command(_("list_variables: List the variables that can be accessed"))
    def list_variables(l):
        variables = renpy.python.py_eval("dir(game_state)")

        filtered_variables = filter(lambda variable: variable.startswith('t3_'), variables)

        filtered_variables.sort()

        return "\n".join(filtered_variables)

    @public_command(_("list_settings: List the preferences (settings) variables that can be accessed"))
    def list_settings(l):
        settings = renpy.python.py_eval("dir(preferences)")

        filtered_settings = filter(lambda setting: setting.startswith('t3_'), settings)

        filtered_settings.sort()

        return "\n".join(filtered_settings)

    @public_command(_("list_labels: List the labels that can be accessed and jumped to"))
    def list_labels(l):
        all_labels = []

        for i in renpy.get_all_labels():
            if i.startswith("t3_"):
                all_labels.append(i)

        all_labels.sort()

        return "\n".join(all_labels)

    @public_command(_("set_variable <variable> <value>: Set the designated variable to the designated value"))
    def set_variable(l):
        parameters = l.rest().strip().split()
        var_name = str(parameters[0])
        var_value = str(parameters[1])

        try:
            renpy.python.py_exec(var_name + " = " + var_value)
            result = renpy.python.py_eval(var_name)
            return "Variable '" + var_name + "' now has the value: " + result
        except:
            return "Could not set variable '" + var_name + "'. Check your spelling and try again."

    @public_command(_("get_variable <variable>: Get the value of the designated variable"))
    def get_variable(l):
        name = str(l.rest().strip())

        try:
            result = renpy.python.py_eval(name)
            return "Variable '" + name + "' has the value: " + str(result)
        except:
            return "Could not get variable '" + name + "'. Check your spelling and try again."

    @public_command(_("set_setting <setting> <value>: Set the designated setting to the designated value"))
    def set_setting(l):
        parameters = l.rest().strip().split()
        var_name = str(parameters[0])
        var_value = str(parameters[1])

        try:
            renpy.python.py_exec("preferences." + var_name + " = " + var_value)
            result = renpy.python.py_eval("preferences." + var_name)
            return "Setting '" + var_name + "' now has the value: " + str(result)
        except:
            return "Could not set setting '" + var_name + "'. Check your spelling and try again."

    @public_command(_("get_setting <setting>: Get the value of the designated setting"))
    def get_setting(l):
        name = str(l.rest().strip())

        try:
            result = renpy.python.py_eval("preferences." + name)
            return "Setting '" + name + "' has the value: " + str(result)
        except:
            return "Could not get setting '" + name + "'. Check your spelling and try again."

    @public_command(_("god_mode <name>: Grant infinite health and mana and all actions are guaranteed to succeed"))
    def god_mode(l):
        name = str(l.rest().strip().lower())

        if name == "all":
            return_string = ""

            renpy.python.py_exec("game_state.t3_player_nerdy.god_mode = True")
            result = renpy.python.py_eval("game_state.t3_player_nerdy.god_mode")
            return_string += "Character 'nerdy' now has god_mode value: " + str(result) + "\n"

            renpy.python.py_exec("game_state.t3_player_sporty.god_mode = True")
            result = renpy.python.py_eval("game_state.t3_player_sporty.god_mode")
            return_string += "Character 'sporty' now has god_mode value: " + str(result) + "\n"

            renpy.python.py_exec("game_state.t3_player_perfect.god_mode = True")
            result = renpy.python.py_eval("game_state.t3_player_perfect.god_mode")
            return_string += "Character 'perfect' now has god_mode value: " + str(result)

            return return_string

        name = get_character_code_name("nerdy", name) or get_character_code_name("sporty", name) or get_character_code_name("perfect", name)

        if name == None:
            return "I don't know who that is. Try 'all' to apply to all playable characters."

        renpy.python.py_exec("game_state.t3_player_" + name + ".god_mode = True")
        result = renpy.python.py_eval("game_state.t3_player_" + name + ".god_mode")

        return "Character '" + name + "' now has god_mode value: " + str(result)

    @public_command(_("god_mode_off <name>: Remove god_mode setting from the designated character(s)"))
    def god_mode_off(l):
        name = str(l.rest().strip().lower())

        if name == "all":
            return_string = ""

            renpy.python.py_exec("game_state.t3_player_nerdy.god_mode = False")
            result = renpy.python.py_eval("game_state.t3_player_nerdy.god_mode")
            return_string += "Character 'nerdy' now has god_mode value: " + str(result) + "\n"

            renpy.python.py_exec("game_state.t3_player_sporty.god_mode = False")
            result = renpy.python.py_eval("game_state.t3_player_sporty.god_mode")
            return_string += "Character 'sporty' now has god_mode value: " + str(result) + "\n"

            renpy.python.py_exec("game_state.t3_player_perfect.god_mode = False")
            result = renpy.python.py_eval("game_state.t3_player_perfect.god_mode")
            return_string += "Character 'perfect' now has god_mode value: " + str(result)

            return return_string
        
        name = get_character_code_name("nerdy", name) or get_character_code_name("sporty", name) or get_character_code_name("perfect", name)

        if name == None:
            return "I don't know who that is. Try 'all' to apply to all playable characters."

        renpy.python.py_exec("game_state.t3_player_" + name + ".god_mode = False")
        result = renpy.python.py_eval("game_state.t3_player_" + name + ".god_mode")

        return "Character '" + name + "' now has god_mode value: " + str(result)

    @public_command(_("cursed_mode <name>: All actions for the designated character(s) are guaranteed to fail"))
    def cursed_mode(l):
        name = str(l.rest().strip().lower())

        if name == "all":
            return_string = ""

            renpy.python.py_exec("game_state.t3_player_nerdy.cursed_mode = True")
            result = renpy.python.py_eval("game_state.t3_player_nerdy.cursed_mode")
            return_string += "Character 'nerdy' now has cursed_mode value: " + str(result) + "\n"

            renpy.python.py_exec("game_state.t3_player_sporty.cursed_mode = True")
            result = renpy.python.py_eval("game_state.t3_player_sporty.cursed_mode")
            return_string += "Character 'sporty' now has cursed_mode value: " + str(result) + "\n"

            renpy.python.py_exec("game_state.t3_player_perfect.cursed_mode = True")
            result = renpy.python.py_eval("game_state.t3_player_perfect.cursed_mode")
            return_string += "Character 'perfect' now has cursed_mode value: " + str(result)

            return return_string
        
        name = get_character_code_name("nerdy", name) or get_character_code_name("sporty", name) or get_character_code_name("perfect", name)

        if name == None:
            return "I don't know who that is. Try 'all' to apply to all playable characters."

        renpy.python.py_exec("game_state.t3_player_" + name + ".cursed_mode = True")
        result = renpy.python.py_eval("game_state.t3_player_" + name + ".cursed_mode")

        return "Character '" + name + "' now has cursed_mode value: " + str(result)

    @public_command(_("cursed_mode_off <name>: Remove cursed_mode setting from the designated character(s)"))
    def cursed_mode_off(l):
        name = str(l.rest().strip().lower())

        if name == "all":
            return_string = ""

            renpy.python.py_exec("game_state.t3_player_nerdy.cursed_mode = False")
            result = renpy.python.py_eval("game_state.t3_player_nerdy.cursed_mode")
            return_string += "Character 'nerdy' now has cursed_mode value: " + str(result) + "\n"

            renpy.python.py_exec("game_state.t3_player_sporty.cursed_mode = False")
            result = renpy.python.py_eval("game_state.t3_player_sporty.cursed_mode")
            return_string += "Character 'sporty' now has cursed_mode value: " + str(result) + "\n"

            renpy.python.py_exec("game_state.t3_player_perfect.cursed_mode = False")
            result = renpy.python.py_eval("game_state.t3_player_perfect.cursed_mode")
            return_string += "Character 'perfect' now has cursed_mode value: " + str(result)

            return return_string
        
        name = get_character_code_name("nerdy", name) or get_character_code_name("sporty", name) or get_character_code_name("perfect", name)

        if name == None:
            return "I don't know who that is. Try 'all' to apply to all playable characters."

        renpy.python.py_exec("game_state.t3_player_" + name + ".cursed_mode = False")
        result = renpy.python.py_eval("game_state.t3_player_" + name + ".cursed_mode")

        return "Character '" + name + "' now has cursed_mode value: " + str(result)

    @public_command(_("kaching <name>: Instantly give the designated character(s) 1000 money"))
    def kaching(l):
        name = str(l.rest().strip().lower())
        amount = 1000

        if name == "all":
            return_string = ""

            renpy.python.py_exec("game_state.t3_player_nerdy.money += " + amount)
            result = renpy.python.py_eval("game_state.t3_player_nerdy.money")
            return_string += "Character 'nerdy' now has money value: " + str(result) + "\n"

            renpy.python.py_exec("game_state.t3_player_sporty.money += " + amount)
            result = renpy.python.py_eval("game_state.t3_player_sporty.money")
            return_string += "Character 'sporty' now has money value: " + str(result) + "\n"

            renpy.python.py_exec("game_state.t3_player_perfect.money += " + amount)
            result = renpy.python.py_eval("game_state.t3_player_perfect.money")
            return_string += "Character 'perfect' now has money value: " + str(result)

            return return_string
        
        name = get_character_code_name("nerdy", name) or get_character_code_name("sporty", name) or get_character_code_name("perfect", name)

        if name == None:
            return "I don't know who that is. Try 'all' to apply to all playable characters."

        renpy.python.py_exec("game_state.t3_player_" + name + ".money += " + amount)
        result = renpy.python.py_eval("game_state.t3_player_" + name + ".money")

        return "Character '" + name + "' now has money value: " + str(result)

    @public_command(_("restore_character <name>: Resets the designated character(s) to full health and mana"))
    def restore_character(l):
        name = str(l.rest().strip().lower())

        if name == "all":
            return_string = ""

            renpy.python.py_exec("game_state.t3_player_nerdy.reset_health()")
            renpy.python.py_exec("game_state.t3_player_nerdy.reset_mana()")
            health_result = renpy.python.py_eval("game_state.t3_player_nerdy.health")
            mana_result = renpy.python.py_eval("game_state.t3_player_nerdy.mana")
            return_string += "Character 'nerdy' now has health value: " + str(health_result) + "and mana value: " + str(mana_result) + "\n"

            renpy.python.py_exec("game_state.t3_player_sporty.reset_health()")
            renpy.python.py_exec("game_state.t3_player_sporty.reset_mana()")
            health_result = renpy.python.py_eval("game_state.t3_player_sporty.health")
            mana_result = renpy.python.py_eval("game_state.t3_player_sporty.mana")
            return_string += "Character 'sporty' now has health value: " + str(health_result) + "and mana value: " + str(mana_result) + "\n"

            renpy.python.py_exec("game_state.t3_player_perfect.reset_health()")
            renpy.python.py_exec("game_state.t3_player_perfect.reset_mana()")
            health_result = renpy.python.py_eval("game_state.t3_player_perfect.health")
            mana_result = renpy.python.py_eval("game_state.t3_player_perfect.mana")
            return_string += "Character 'perfect' now has health value: " + str(health_result) + "and mana value: " + str(mana_result) + "\n"

            return return_string
        
        name = get_character_code_name("nerdy", name) or get_character_code_name("sporty", name) or get_character_code_name("perfect", name)

        if name == None:
            return "I don't know who that is. Try 'all' to apply to all playable characters."

        renpy.python.py_exec("game_state.t3_player_" + name + ".reset_health()")
        renpy.python.py_exec("game_state.t3_player_" + name + ".reset_mana()")
        health_result = renpy.python.py_eval("game_state.t3_player_" + name + ".health")
        mana_result = renpy.python.py_eval("game_state.t3_player_" + name + ".mana")

        return "Character '" + name + "' now has cursed_mode value: " + str(health_result) + "and mana value: " + str(mana_result)
