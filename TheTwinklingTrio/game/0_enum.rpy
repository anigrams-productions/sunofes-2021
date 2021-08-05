## This file initializes an enum() method that can be used to create enumerations, which can be used in the place of "magic strings".
## The linter will complain if the specified property doesn't exist on the Enum, making it easier to catch typos before they cause bugs.
## NOTE: Python 3.4 introduced official Enums, but Ren'py is still on 2.7.

init python:
    ## Usage: MyEnum = emum("One", "Two", "Three")
    ## Retuns an object of type Enum with the following properties and values: { One: 1, Two: 2, Three: 3 }
    ## These values can then be referenced like MyEnum.One
    ## Custom values can also be passed in like enum(One="one", Two="two", Three="three")
    def enum(*sequential, **named):
        enums = dict(zip(sequential, range(len(sequential))), **named)
        return type('Enum'.encode('utf8'), (), enums)

## Advanced Settings Enums
define AutoSelection = enum("On", "Others", "Off")
define Frequency = enum("Low", "Normal", "High")
define Difficulty = enum("Casual", "Easy", "Normal", "Hard", "Nightmare")

define AttributeAllocation = enum("Novice", "Average", "Expert")

## Gameplay Enums
define CharacterType = enum(Nerdy="nerdy", Sporty="sporty", Perfect="perfect")

define Theme = enum(
    Field="field",
    Volcano="volcano",
    Desert="desert",
    Snow="snow",
    Graveyard="grave"
)

define ScenarioType = enum(
    Enemy="enemy",
    Boss="boss",
    Merchant="merchant",
    Priest="priest",
    Bard="bard",
    Quest="quest",
    Special="special",
    Campfire="campfire",
    Treasure="treasure",
    Puzzle="puzzle",
    Trap="trap"
)

define EnemyType = enum(
    Dragon="dragon",
    Orc="orc",
    Fish="fish",
    Reptile="reptile",
    Mammal="mammal",
    Bird="bird",
    Insect="insect",
    Knight="knight",
    Goblin="goblin",
    Spirit="spirit",
    Slime="slime",
    Plant="plant",
    Golem="golem",
    Undead="undead",
    Demon="demon",
    Robot="robot"
)