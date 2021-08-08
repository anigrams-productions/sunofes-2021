init python:
    class Npc(Entity):
        def __init__(self, theme, npc_type, name, health, mana, style, magic, wisdom):
            self.theme = theme
            self.npc_type = npc_type
            self.icon = self.get_icon()

            # NPCs don't really need money...
            self.money = 0

            Entity.__init__(self, npc_type, name, self.icon, health, mana, self.money, style, magic, wisdom, None, None)

        def get_icon(self):
            # Ren'Py doesn't like Python string interpolation, so we'll use concatenation instead
            return "npc " + self.theme + " " + self.npc_type

define SpecialNpcs = [
    Npc(Theme.Field, ScenarioType.Special, "Creepy 'Buddy'", 100, 100, 6, 12, 11),
    Npc(Theme.Volcano, ScenarioType.Special, "Priceless Relic", 100, 100, 12, 4, 8),
    Npc(Theme.Desert, ScenarioType.Special, "Regretful Dragon", 100, 100, 8, 11, 10),
    Npc(Theme.Snow, ScenarioType.Special, "Heroic Spirit", 100, 100, 16, 10, 8),
    Npc(Theme.Graveyard, ScenarioType.Special, "Suspicious Cat", 100, 100, 12, 11, 10)
]

define BardNpcs = [
    Npc(Theme.Field, ScenarioType.Bard, "Aspiring Rooster", 100, 100, 5, 8, 9),
    Npc(Theme.Volcano, ScenarioType.Bard, "Gruff Goat", 100, 100, 11, 6, 16),
    Npc(Theme.Desert, ScenarioType.Bard, "Pessimistic Elephant", 100, 100, 11, 9, 10),
    Npc(Theme.Snow, ScenarioType.Bard, "Indifferent Ox", 100, 100, 7, 8, 9),
    Npc(Theme.Graveyard, ScenarioType.Bard, "Obnoxious Crow", 100, 100, 11, 9, 11)
]

define QuestNpcs = [
    Npc(Theme.Field, ScenarioType.Quest, "Training Dummy", 100, 100, 9, 10, 7),
    Npc(Theme.Volcano, ScenarioType.Quest, "Brave Diver", 100, 100, 13, 11, 16),
    Npc(Theme.Desert, ScenarioType.Quest, "Angry Madman", 100, 100, 9, 13, 17),
    Npc(Theme.Snow, ScenarioType.Quest, "Gentle Horse", 100, 100, 7, 12, 11),
    Npc(Theme.Graveyard, ScenarioType.Quest, "Frenzied Skeleton", 100, 100, 8, 10, 15)
]

define MerchantNpcs = [
    Npc(Theme.Field, ScenarioType.Merchant, "Clever Frog", 100, 100, 10, 10, 13),
    Npc(Theme.Volcano, ScenarioType.Merchant, "Smiling Pig", 100, 100, 10, 17, 12),
    Npc(Theme.Desert, ScenarioType.Merchant, "Cheerful Gremlin", 100, 100, 9, 10, 5),
    Npc(Theme.Snow, ScenarioType.Merchant, "Charming Golem", 100, 100, 14, 12, 9),
    Npc(Theme.Graveyard, ScenarioType.Merchant, "Grumpy Wolf", 100, 100, 11, 12, 12)
]

define PriestNpcs = [
    Npc(Theme.Field, ScenarioType.Priest, "Shrewd Sheep", 100, 100, 8, 11, 7),
    Npc(Theme.Volcano, ScenarioType.Priest, "Clunky Robot", 100, 100, 13, 13, 15),
    Npc(Theme.Desert, ScenarioType.Priest, "Handsome Lion", 100, 100, 9, 13, 13),
    Npc(Theme.Snow, ScenarioType.Priest, "Elderly Turtle", 100, 100, 10, 14, 15),
    Npc(Theme.Graveyard, ScenarioType.Priest, "Sleazy Rat", 100, 100, 12, 8, 13)
]