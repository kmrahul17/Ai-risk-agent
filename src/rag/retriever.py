import json


RULES_PATH = (
    "data/rules/store_rules.json"
)


def load_rules():
    with open(
        RULES_PATH,
        "r",
        encoding="utf-8",
    ) as f:
        return json.load(f)


def retrieve_rules(
    reasons,
    page_stage,
):
    rules = load_rules()

    relevant = {}

    # delivery related
    if (
        "delivery_eta_days"
        in reasons
    ):
        relevant["shipping"] = (
            rules["shipping"]
        )

    # cart value
    if (
        "cart_value"
        in reasons
    ):
        relevant["discounts"] = (
            rules["discounts"]
        )

    # payment page
    if page_stage == "checkout":
        relevant["payment"] = (
            rules["payment"]
        )

    # new user
    if (
        "is_returning_user"
        in reasons
    ):
        relevant[
            "customer_rules"
        ] = rules[
            "customer_rules"
        ]

    # page offers
    relevant["offers"] = (
        rules["offers"]
    )
    # homepage
    if page_stage == "home":
        relevant[
        "customer_rules"
    ] = rules[
        "customer_rules"
    ]

    relevant[
        "offers"
    ] = {
        "home":
        rules["offers"]["home"]
    }

    return relevant