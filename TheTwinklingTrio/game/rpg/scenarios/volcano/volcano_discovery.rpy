## This file contains Volcano theme-specific discovery scenarios.
## Until they're fully implemented, they'll just call the common scenario scripts instead.

label t3_scenario_volcano_campfire:
    call t3_scenario_campfire from _call_t3_scenario_campfire_4

    return

label t3_scenario_volcano_treasure:
    call t3_scenario_treasure from _call_t3_scenario_treasure_4

    return

label t3_scenario_volcano_puzzle:
    call t3_scenario_puzzle from _call_t3_scenario_puzzle_4

    return

label t3_scenario_volcano_trap:
    call t3_scenario_trap from _call_t3_scenario_trap_4

    return