import random
import pandas as pd

from configs.settings import *
from src.data_generation.distributions import *
from src.data_generation.risk_rules import calculate_risk

def generate_row():
    page_stage = sample_page()

    delivery_zone = sample_zone()

    device_type = sample_device()

    cart_items_count = random.randint(1, 5)

    cart_value = random.randint(
        300,
        cart_items_count * 1200
    )

    if delivery_zone == "remote":
        delivery_eta_days = random.randint(3, 5)
    elif delivery_zone == "tier2":
        delivery_eta_days = random.randint(2, 4)
    else:
        delivery_eta_days = random.randint(1, 3)

    if page_stage == "checkout":
        idle_seconds = random.randint(5, 25)
    else:
        idle_seconds = random.randint(0, 18)

    row = {
        "time_spent_sec": random.randint(10, 120),

        "page_stage": page_stage,

        "device_type": device_type,

        "delivery_zone": delivery_zone,

        "cart_value": cart_value,

        "cart_items_count": cart_items_count,

        "delivery_eta_days": delivery_eta_days,

        "coupon_status": sample_coupon(),

        "is_returning_user": random.choice([0, 1]),

        "idle_seconds": idle_seconds,
    }

    risk = calculate_risk(row)

    row["abandoned"] = (
        1 if random.random() < risk else 0
    )

    return row


def generate_dataset():
    rows = [
        generate_row()
        for _ in range(DATASET_SIZE)
    ]

    df = pd.DataFrame(rows)

    df.to_csv(
        RAW_DATA_PATH,
        index=False
    )

    return df