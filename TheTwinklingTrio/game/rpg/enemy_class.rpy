init python:
    class Enemy(Entity):
        def __init__(self, theme, enemy_type, name, enemy_id, health, mana, style, magic, wisdom):
            self.theme = theme
            self.enemy_type = enemy_type
            self.enemy_id = enemy_id
            self.icon = self.get_icon()
            self.aggression = preferences.t3_rpg_attribute_starting_health
            self.max_aggression = self.aggression

            # randomize monetary reward

            money = renpy.random.randint(preferences.t3_rpg_random_min_money_reward, preferences.t3_rpg_random_max_money_reward)
            name_color = "#999999"
            enemy_font = self.get_font()

            Entity.__init__(self, enemy_type, name, self.icon, health, mana, money, style, magic, wisdom, None, None, name_color, enemy_font)

        def get_icon(self):
            # Ren'Py doesn't like Python string interpolation, so we'll use concatenation instead
            if self.enemy_id:
                return "enemy " + self.theme + " " + self.enemy_type + "_" + self.enemy_id
            else:
                return "boss " + self.theme + " " + self.enemy_type

        def get_font(self):
            if self.enemy_type == EnemyType.Dragon:
                return "fonts/monster/Macondo-Regular.ttf"
            elif self.enemy_type == EnemyType.Orc:
                return "fonts/monster/Lacquer-Regular.ttf"
            elif self.enemy_type == EnemyType.Fish:
                return "fonts/monster/TheGirlNextDoor-Regular.ttf"
            elif self.enemy_type == EnemyType.Reptile:
                return "fonts/monster/Lacquer-Regular.ttf"
            elif self.enemy_type == EnemyType.Mammal:
                return "fonts/monster/Gaegu-Regular.ttf"
            elif self.enemy_type == EnemyType.Bird:
                return "fonts/monster/TheGirlNextDoor-Regular.ttf"
            elif self.enemy_type == EnemyType.Insect:
                return "fonts/monster/SnowburstOne-Regular.ttf"
            elif self.enemy_type == EnemyType.Knight:
                return "fonts/monster/Macondo-Regular.ttf"
            elif self.enemy_type == EnemyType.Goblin:
                return "fonts/monster/Lacquer-Regular.ttf"
            elif self.enemy_type == EnemyType.Spirit:
                return "fonts/monster/PrincessSofia-Regular.ttf"
            elif self.enemy_type == EnemyType.Slime:
                return "fonts/monster/Bonbon-Regular.ttf"
            elif self.enemy_type == EnemyType.Plant:
                return "fonts/monster/Bonbon-Regular.ttf"
            elif self.enemy_type == EnemyType.Golem:
                return "fonts/monster/SnowburstOne-Regular.ttf"
            elif self.enemy_type == EnemyType.Undead:
                return "fonts/monster/NovaCut-Regular.ttf"
            elif self.enemy_type == EnemyType.Undead:
                return "fonts/monster/NovaCut-Regular.ttf"
            elif self.enemy_type == EnemyType.Demon:
                return "fonts/monster/NovaCut-Regular.ttf"
            elif self.enemy_type == EnemyType.Robot:
                return "fonts/monster/VT323-Regular.ttf"

        def update_aggression(self, amount):
            if (self.aggression + amount) > self.max_aggression:
                self.aggression = self.max_aggression
            else:
                self.aggression += amount

            # can't have negative aggression
            if self.aggression < 0:
                self.aggression = 0

        def is_pacified(self):
            return self.aggression > 0

define DesertEnemies = [
    Enemy(Theme.Desert, EnemyType.Mammal, "Angry Bear", "01", 100, 75, 5, 6, 11),
    Enemy(Theme.Desert, EnemyType.Insect, "Demolition Ant", "01", 75, 125, 5, 17, 6),
    Enemy(Theme.Desert, EnemyType.Dragon, "Lightning Dragon", "01", 100, 125, 11, 14, 9),
    Enemy(Theme.Desert, EnemyType.Insect, "Giant Grub", "03", 100, 100, 16, 8, 13),
    Enemy(Theme.Desert, EnemyType.Demon, "Creepy Eyeworm", "02", 75, 100, 16, 11, 15),
    Enemy(Theme.Desert, EnemyType.Slime, "Ugly Snail", "01", 100, 100, 9, 12, 15),
    Enemy(Theme.Desert, EnemyType.Insect, "Wolf Spider", "04", 100, 75, 8, 5, 9),
    Enemy(Theme.Desert, EnemyType.Mammal, "Cursed Werewolf", "02", 125, 100, 17, 9, 4)
]

define DesertBosses = [
    Enemy(Theme.Desert, EnemyType.Dragon, "Bone Dragon", "", 200, 200, 8, 6, 14),
    Enemy(Theme.Desert, EnemyType.Golem, "Stone Golem", "", 200, 200, 12, 7, 11)
]

define FieldEnemies = [
    Enemy(Theme.Field, EnemyType.Fish, "Floppy Fish", "01", 75, 100, 10, 10, 15),
    Enemy(Theme.Field, EnemyType.Dragon, "Derpy Dragon", "01", 100, 100, 7, 10, 16),
    Enemy(Theme.Field, EnemyType.Reptile, "Magical Turtle", "01", 75, 125, 11, 16, 5),
    Enemy(Theme.Field, EnemyType.Mammal, "Boring Bear", "01", 100, 100, 6, 11, 9),
    Enemy(Theme.Field, EnemyType.Bird, "Purple Bird", "01", 100, 75, 13, 4, 12),
    Enemy(Theme.Field, EnemyType.Reptile, "Snappy Crocodile", "02", 100, 125, 8, 16, 10),
    Enemy(Theme.Field, EnemyType.Knight, "Wise Knight", "01", 125, 100, 7, 11, 16),
    Enemy(Theme.Field, EnemyType.Spirit, "Shy Guy", "01", 100, 75, 11, 3, 10),
    Enemy(Theme.Field, EnemyType.Knight, "Holy Knight", "02", 125, 100, 5, 7, 15),
    Enemy(Theme.Field, EnemyType.Spirit, "Masked Vigilante", "03", 100, 100, 10, 10, 14),
    Enemy(Theme.Field, EnemyType.Orc, "Slimy Orc", "01", 125, 100, 7, 10, 14),
    Enemy(Theme.Field, EnemyType.Plant, "Plant Trap", "01", 100, 125, 8, 15, 11),
    Enemy(Theme.Field, EnemyType.Plant, "Demonic Pumpkin", "02", 100, 125, 9, 14, 7),
    Enemy(Theme.Field, EnemyType.Slime, "Skull Slime", "02", 100, 100, 15, 8, 7)
]

define FieldBosses = [
    Enemy(Theme.Field, EnemyType.Dragon, "Earth Dragon", "", 200, 200, 11, 11, 8)
    # Enemy(Theme.Field, EnemyType.Orc, "Orc Boss", "", 200, 200, 15, 13, 13)
]

define GraveyardEnemies = [
    Enemy(Theme.Graveyard, EnemyType.Undead, "Radioactive Ghoul", "01", 100, 100, 14, 9, 7),
    Enemy(Theme.Graveyard, EnemyType.Mammal, "Floppy Bat", "01", 75, 100, 16, 7, 14),
    Enemy(Theme.Graveyard, EnemyType.Undead, "Skeleton Bear", "02", 125, 100, 7, 12, 5),
    Enemy(Theme.Graveyard, EnemyType.Spirit, "Cursed Doll", "02", 75, 125, 12, 17, 9),
    Enemy(Theme.Graveyard, EnemyType.Mammal, "Grey Wolf", "02", 100, 125, 6, 15, 13),
    Enemy(Theme.Graveyard, EnemyType.Undead, "Archaic Mummy", "04", 100, 125, 13, 14, 8),
    Enemy(Theme.Graveyard, EnemyType.Undead, "Skeleton Hunter", "09", 100, 75, 6, 6, 14),
    Enemy(Theme.Graveyard, EnemyType.Undead, "Skeleton Knight", "10", 100, 125, 13, 18, 13),
    Enemy(Theme.Graveyard, EnemyType.Insect, "Evil Spider", "02", 100, 75, 9, 6, 17),
    Enemy(Theme.Graveyard, EnemyType.Undead, "Fleshy Zombie", "11", 100, 100, 16, 13, 15)
]

define GraveyardBosses = [
    Enemy(Theme.Graveyard, EnemyType.Knight, preferences.t3_rpg_char_villain_title, "", 200, 250, 17, 16, 13),
    Enemy(Theme.Graveyard, EnemyType.Undead, "Immortal Dragon", "", 250, 200, 12, 9, 4)
]

define SnowEnemies = [
    Enemy(Theme.Snow, EnemyType.Mammal, "Polar Bear", "02", 125, 75, 12, 6, 12),
    Enemy(Theme.Snow, EnemyType.Fish, "Sea Creature", "01", 100, 125, 10, 14, 8),
    Enemy(Theme.Snow, EnemyType.Golem, "Crystal Golem", "01", 100, 125, 12, 14, 8),
    Enemy(Theme.Snow, EnemyType.Knight, "Horned Knight", "01", 100, 125, 13, 14, 12),
    Enemy(Theme.Snow, EnemyType.Dragon, "Elegant Dragon", "02", 100, 100, 12, 9, 5),
    Enemy(Theme.Snow, EnemyType.Dragon, "Spikey Dragon", "04", 100, 100, 3, 7, 15),
    Enemy(Theme.Snow, EnemyType.Demon, "Eye Demon", "03", 100, 100, 13, 11, 16),
    Enemy(Theme.Snow, EnemyType.Goblin, "Grumpy Goblin", "02", 100, 125, 9, 14, 8),
    Enemy(Theme.Snow, EnemyType.Golem, "Ice Golem", "02", 100, 75, 5, 6, 13),
    Enemy(Theme.Snow, EnemyType.Insect, "Skilled Pinchers", "01", 100, 125, 13, 14, 13),
    Enemy(Theme.Snow, EnemyType.Demon, "Spooky Nightmare", "04", 100, 125, 13, 18, 9),
    Enemy(Theme.Snow, EnemyType.Reptile, "Silver Snake", "01", 100, 125, 10, 14, 9),
    Enemy(Theme.Snow, EnemyType.Goblin, "Angry Goblin", "03", 125, 100, 15, 12, 8)
]

define SnowBosses = [
    Enemy(Theme.Snow, EnemyType.Dragon, "Mystical Dragon", "", 200, 200, 11, 9, 5),
    Enemy(Theme.Snow, EnemyType.Orc, "Frost Giant", "", 200, 200, 9, 13, 12)
]

define VolcanoEnemies = [
    Enemy(Theme.Volcano, EnemyType.Undead, "Ash Zombie", "01", 100, 125, 12, 14, 9),
    Enemy(Theme.Volcano, EnemyType.Knight, "Golden Knight", "01", 100, 125, 11, 15, 11),
    Enemy(Theme.Volcano, EnemyType.Demon, "Grinning Demon", "01", 100, 100, 12, 9, 14),
    Enemy(Theme.Volcano, EnemyType.Demon, "Spikey Demon", "02", 100, 125, 6, 15, 10),
    Enemy(Theme.Volcano, EnemyType.Demon, "Rhino Demon", "05", 100, 125, 12, 14, 11),
    Enemy(Theme.Volcano, EnemyType.Golem, "Mountain Golem", "01", 125, 100, 6, 8, 6),
    Enemy(Theme.Volcano, EnemyType.Knight, "Golem Knight", "02", 100, 125, 11, 15, 13),
    Enemy(Theme.Volcano, EnemyType.Knight, "Glowing Knight", "03", 125, 100, 14, 13, 5),
    Enemy(Theme.Volcano, EnemyType.Orc, "Astute Madman", "01", 100, 100, 11, 8, 15),
    Enemy(Theme.Volcano, EnemyType.Bird, "Magic Phoenix", "01", 100, 125, 12, 16, 9),
    Enemy(Theme.Volcano, EnemyType.Insect, "Hungry Spider", "01", 100, 125, 9, 17, 13)
]

define VolcanoBosses = [
    Enemy(Theme.Volcano, EnemyType.Demon, "Ember Giant", "", 200, 200, 6, 8, 10),
    Enemy(Theme.Volcano, EnemyType.Dragon, "Flame Dragon", "", 200, 200, 10, 13, 12)
]