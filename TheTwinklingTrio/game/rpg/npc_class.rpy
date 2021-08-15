init python:
    class Npc(Entity):
        def __init__(self, theme, npc_type, name, health, mana, style, magic, wisdom, npc_font):
            self.theme = theme
            self.npc_type = npc_type
            self.icon = self.get_icon()

            # NPCs don't really need money...
            self.money = 0
            name_color = "#999999"
            self.npc_font = npc_font

            Entity.__init__(self, npc_type, name, self.icon, health, mana, self.money, style, magic, wisdom, None, None, name_color, npc_font)

        def get_icon(self):
            # Ren'Py doesn't like Python string interpolation, so we'll use concatenation instead
            return "npc " + self.theme + " " + self.npc_type

define ObjectiveNpcs = [
    Npc(Theme.Field, ScenarioType.Objective, "Egg Man", 100, 100, 6, 12, 11, "fonts/monster/PrincessSofia-Regular.ttf"),
    Npc(Theme.Volcano, ScenarioType.Objective, "Priceless Relic", 100, 100, 12, 4, 8, "fonts/monster/VT323-Regular.ttf"),
    Npc(Theme.Desert, ScenarioType.Objective, "Regretful Dragon", 100, 100, 8, 11, 10, "fonts/monster/Macondo-Regular.ttf"),
    Npc(Theme.Snow, ScenarioType.Objective, "Heroic Spirit", 100, 100, 16, 10, 8, "fonts/monster/PrincessSofia-Regular.ttf"),
    Npc(Theme.Graveyard, ScenarioType.Objective, "Suspicious Cat", 100, 100, 12, 11, 10, "fonts/monster/Gaegu-Regular.ttf")
]

define BardNpcs = [
    Npc(Theme.Field, ScenarioType.Bard, "Aspiring Rooster", 100, 100, 5, 8, 9, "fonts/monster/TheGirlNextDoor-Regular.ttf"),
    Npc(Theme.Volcano, ScenarioType.Bard, "Gruff Goat", 100, 100, 11, 6, 16, "fonts/monster/Gaegu-Regular.ttf"),
    Npc(Theme.Desert, ScenarioType.Bard, "Pessimistic Elephant", 100, 100, 11, 9, 10, "fonts/monster/Gaegu-Regular.ttf"),
    Npc(Theme.Snow, ScenarioType.Bard, "Indifferent Ox", 100, 100, 7, 8, 9, "fonts/monster/Gaegu-Regular.ttf"),
    Npc(Theme.Graveyard, ScenarioType.Bard, "Obnoxious Crow", 100, 100, 11, 9, 11, "fonts/monster/TheGirlNextDoor-Regular.ttf")
]

define QuestNpcs = [
    Npc(Theme.Field, ScenarioType.Quest, "Training Dummy", 100, 100, 9, 10, 7, "fonts/monster/VT323-Regular.ttf"),
    Npc(Theme.Volcano, ScenarioType.Quest, "Brave Diver", 100, 100, 13, 11, 16, "fonts/monster/TheGirlNextDoor-Regular.ttf"),
    Npc(Theme.Desert, ScenarioType.Quest, "Angry Madman", 100, 100, 9, 13, 17, "fonts/monster/Lacquer-Regular.ttf"),
    Npc(Theme.Snow, ScenarioType.Quest, "Gentle Horse", 100, 100, 7, 12, 11, "fonts/monster/Gaegu-Regular.ttf"),
    Npc(Theme.Graveyard, ScenarioType.Quest, "Frenzied Skeleton", 100, 100, 8, 10, 15, "fonts/monster/NovaCut-Regular.ttf")
]

define MerchantNpcs = [
    Npc(Theme.Field, ScenarioType.Merchant, "Clever Frog", 100, 100, 10, 10, 13, "fonts/monster/Lacquer-Regular.ttf"),
    Npc(Theme.Volcano, ScenarioType.Merchant, "Smiling Pig", 100, 100, 10, 17, 12, "fonts/monster/Gaegu-Regular.ttf"),
    Npc(Theme.Desert, ScenarioType.Merchant, "Cheerful Gremlin", 100, 100, 9, 10, 5, "fonts/monster/PrincessSofia-Regular.ttf"),
    Npc(Theme.Snow, ScenarioType.Merchant, "Charming Golem", 100, 100, 14, 12, 9, "fonts/monster/SnowburstOne-Regular.ttf"),
    Npc(Theme.Graveyard, ScenarioType.Merchant, "Grumpy Wolf", 100, 100, 11, 12, 12, "fonts/monster/Gaegu-Regular.ttf")
]

define PriestNpcs = [
    Npc(Theme.Field, ScenarioType.Priest, "Shrewd Sheep", 100, 100, 8, 11, 7, "fonts/monster/Gaegu-Regular.ttf"),
    Npc(Theme.Volcano, ScenarioType.Priest, "Clunky Robot", 100, 100, 13, 13, 15, "fonts/monster/VT323-Regular.ttf"),
    Npc(Theme.Desert, ScenarioType.Priest, "Handsome Lion", 100, 100, 9, 13, 13, "fonts/monster/Gaegu-Regular.ttf"),
    Npc(Theme.Snow, ScenarioType.Priest, "Elderly Turtle", 100, 100, 10, 14, 15, "fonts/monster/Lacquer-Regular.ttf"),
    Npc(Theme.Graveyard, ScenarioType.Priest, "Sleazy Rat", 100, 100, 12, 8, 13, "fonts/monster/Gaegu-Regular.ttf")
]