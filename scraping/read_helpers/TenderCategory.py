from enum import Enum


class TenderCategory(Enum):
    NORMAL_PUBLIC = 0
    TARGET_PRICE = 1
    REDUCED_PRICE = 2
    INITIATION_TENDER = 3
    UNSPECIFIED_LOT = 4
    REGISTRATION_LOTTERY = 5
    HOUSE_FOR_RENT = 6
    AMIDAR = 7
    ACO = 8
