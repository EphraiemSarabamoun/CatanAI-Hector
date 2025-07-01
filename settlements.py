from enum import Enum, auto
from typing import Dict
from resources import Resource

class SettlementType(Enum):
    """Enumeration of possible settlement types."""
    TOWN = auto()
    CITY = auto()

# Resources required to construct each settlement type
BUILD_COSTS: Dict[SettlementType, Dict[Resource, int]] = {
    SettlementType.TOWN: {
        Resource.BRICK: 1,
        Resource.WOOD: 1,
        Resource.WHEAT: 1,
        Resource.SHEEP: 1,
    },
    SettlementType.CITY: {
        Resource.ORE: 3,
        Resource.WHEAT: 2,
    },
}

# Resource production multiplier given by each settlement type
PRODUCTION_MULTIPLIER: Dict[SettlementType, int] = {
    SettlementType.TOWN: 1,   # towns collect 1 resource
    SettlementType.CITY: 2,   # cities collect 2 resources (double)
}

class Settlement:
    def __init__(self, settlement_type: SettlementType = SettlementType.TOWN):
        self.type = settlement_type

    def build_cost(self) -> Dict[Resource, int]:
        return BUILD_COSTS[self.type]

    def production_multiplier(self) -> int:
        return PRODUCTION_MULTIPLIER[self.type]

    def upgrade_to_city(self):
        if self.type == SettlementType.CITY:
            raise ValueError("Settlement is already a city")
        self.type = SettlementType.CITY
