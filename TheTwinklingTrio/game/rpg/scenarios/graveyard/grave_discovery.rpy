## This file contains Graveyard theme-specific discovery scenarios.
## Until they're fully implemented, they'll just call the common scenario scripts instead.

label t3_scenario_grave_campfire:
    call t3_scenario_campfire from _call_t3_scenario_campfire_1

    return

label t3_scenario_grave_treasure:
    call t3_scenario_treasure from _call_t3_scenario_treasure_1

    return

label t3_scenario_grave_puzzle:
    call t3_scenario_puzzle from _call_t3_scenario_puzzle_1

    return

label t3_scenario_grave_trap:
    call t3_scenario_trap from _call_t3_scenario_trap_1

    return