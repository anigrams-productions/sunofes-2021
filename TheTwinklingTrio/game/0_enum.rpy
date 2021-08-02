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
