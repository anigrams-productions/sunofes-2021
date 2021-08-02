init python:
    class Enemy(Entity):
        def __init__(self, theme, enemy_type, name, id, health, mana, style, magic, wisdom):
            self.theme = theme
            self.enemy_type = enemy_type
            self.id = id
            self.icon = self.get_icon()

            # randomize monetary reward
            # TODO: make the max and min configurable
            money = renpy.random.randint(100, 1000)

            Entity.__init__(self, enemy_type, name, icon, health, mana, money, style, magic, wisdom)

        def get_icon(self):
            return "enemy {self.theme} {self.enemy_type}_{self.id}"

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
    Enemy(Theme.Field, EnemyType.Dragon, "Earth Dragon", "", 200, 200, 11, 11, 8),
    Enemy(Theme.Field, EnemyType.Orc, "Orc Boss", "", 200, 200, 15, 13, 13)
]