## This file contains Field theme-specific discovery scenarios.
## Until they're fully implemented, they'll just call the common scenario scripts instead.

label t3_scenario_field_campfire:
    call t3_scenario_campfire from _call_t3_scenario_campfire

    return

label t3_scenario_field_treasure:
    call t3_scenario_treasure from _call_t3_scenario_treasure

    return

label t3_scenario_field_puzzle:
    call t3_scenario_puzzle from _call_t3_scenario_puzzle

    return

label t3_scenario_field_trap:
    call t3_scenario_trap from _call_t3_scenario_trap

    return