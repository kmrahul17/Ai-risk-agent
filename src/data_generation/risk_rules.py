def calculate_risk(row):
    risk = 0.18

    if row["delivery_eta_days"] >= 4:
        risk += 0.22

    if row["idle_seconds"] > 15:
        risk += 0.18

    if row["cart_value"] > 2500:
        risk += 0.12

    if row["cart_items_count"] >= 4:
        risk += 0.08

    if (
        row["page_stage"] == "checkout"
        and row["idle_seconds"] > 10
    ):
        risk += 0.20

    if row["delivery_zone"] == "remote":
        risk += 0.10

    if row["coupon_status"] == "applied":
        risk -= 0.12

    if row["is_returning_user"] == 1:
        risk -= 0.08

    return max(0.05, min(risk, 0.95))