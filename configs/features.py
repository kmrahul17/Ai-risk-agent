FEATURE_COLUMNS = [
    "time_spent_sec",
    "page_stage",
    "device_type",
    "delivery_zone",
    "cart_value",
    "cart_items_count",
    "delivery_eta_days",
    "coupon_status",
    "is_returning_user",
    "idle_seconds",
]

TARGET_COLUMN = "abandoned"

PAGE_STAGES = [
    "home",
    "product",
    "cart",
    "checkout"
]

DEVICE_TYPES = [
    "iphone",
    "android",
    "windows",
    "macbook",
    "tablet"
]

DELIVERY_ZONES = [
    "metro",
    "tier2",
    "remote"
]

COUPON_STATUS = [
    "none",
    "available",
    "applied"
]