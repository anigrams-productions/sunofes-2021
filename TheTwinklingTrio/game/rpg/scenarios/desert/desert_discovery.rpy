## This file contains Desert theme-specific discovery scenarios.
## Until they're fully implemented, they'll just call the common scenario scripts instead.

label t3_scenario_desert_campfire:
    call t3_scenario_campfire from _call_t3_scenario_campfire_2

    return

label t3_scenario_desert_treasure:
    call t3_scenario_treasure from _call_t3_scenario_treasure_2

    return

label t3_scenario_desert_puzzle:
    call t3_scenario_puzzle from _call_t3_scenario_puzzle_2

    return

label t3_scenario_desert_trap:
    call t3_scenario_trap from _call_t3_scenario_trap_2

    return