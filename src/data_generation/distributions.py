import random
from configs.features import *

def weighted_choice(items, weights):
    return random.choices(items, weights=weights, k=1)[0]


def sample_page():
    return weighted_choice(
        PAGE_STAGES,
        [0.20, 0.35, 0.25,0.20]
    )


def sample_device():
    return weighted_choice(
        DEVICE_TYPES,
        [0.25, 0.4, 0.2, 0.1, 0.05]
    )


def sample_zone():
    return weighted_choice(
        DELIVERY_ZONES,
        [0.5, 0.3, 0.2]
    )


def sample_coupon():
    return weighted_choice(
        COUPON_STATUS,
        [0.4, 0.3, 0.3]
    )