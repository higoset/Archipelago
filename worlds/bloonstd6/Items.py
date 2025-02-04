from typing import Dict, List, Optional
from BaseClasses import Item, ItemClassification
from worlds.bloonstd6.Locations import BloonsLocations
from .Utils import Utils


class BTD6MedalItem(Item):
    game: str = "Bloons TD6"

    def __init__(self, name: str, code: Optional[int], player: int):
        super().__init__(
            name,
            ItemClassification.progression_skip_balancing,
            code,
            player,
        )


class BTD6MapUnlock(Item):
    game: str = "Bloons TD6"

    def __init__(self, name: str, code: Optional[int], player: int):
        super().__init__(name, ItemClassification.progression, code, player)

class BTD6MonkeyUnlock(Item):
    game: str = "Bloons TD6"

    def __init__(self, name: str, code: Optional[int], player: int):
        super().__init__(name, ItemClassification.useful, code, player)

class BTD6FillerItem(Item):
    game: str = "Bloons TD6"

    def __init__(self, name: str, code: Optional[int], player: int):
        super().__init__(name, ItemClassification.filler, code, player)


class BloonsItems:
    MEDAL_NAME: str = "Medal"
    MEDAL_CODE: int = Utils.BASE_OFFSET

    KNOWLEDGE_NAME: str = "Monkey Knowledge"
    KNOWLEDGE_CODE: int = Utils.BASE_OFFSET + 1

    item_offset = 2 + Utils.BASE_OFFSET

    items: Dict[str, int] = {}

    monkeyIDs: List[str] = [
        "DartMonkey",
        "BoomerangMonkey",
        "BombShooter",
        "TackShooter",
        "IceMonkey",
        "GlueGunner",
        "SniperMonkey",
        "MonkeySub",
        "MonkeyBuccaneer",
        "MonkeyAce",
        "HeliPilot",
        "MortarMonkey",
        "DartlingGunner",
        "WizardMonkey",
        "SuperMonkey",
        "NinjaMonkey",
        "Alchemist",
        "Druid",
        "BananaFarm",
        "SpikeFactory",
        "MonkeyVillage",
        "EngineerMonkey",
        "BeastHandler",
    ]

    def __init__(self) -> None:
        mapdata = BloonsLocations()
        maplist = mapdata.get_maps()

        self.items[self.MEDAL_NAME] = self.MEDAL_CODE
        self.items[self.KNOWLEDGE_NAME] = self.KNOWLEDGE_CODE

        index = self.item_offset
        for name in maplist:
            self.items[f"{name}-MUnlock"] = index
            index += 1
        for name in self.monkeyIDs:
            self.items[f"{name}-TUnlock"] = index
            index += 1

    level_rewards = [
        "Boomerang Monkey",
        "Bomb Shooter",
        "Tack Shooter",
        "Ice Monkey",
        "Glue Gunner",
        "Sniper Monkey",
        "Monkey Sub",
        "Monkey Buccaneer",
        "Monkey Ace",
        "Mortar Monkey",
        "Gwendolin",
        "Wizard Monkey",
        "Super Monkey",
        "Ninja Monkey",
        "Alchemist",
        "Druid",
        "Striker Jones",
        "Banana Farm",
        "Spike Factory",
        "Monkey Village",
        "Engineer Monkey",
        "Obyn Greenfoot",
    ]
