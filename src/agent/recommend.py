import os
import json

from groq import Groq
from dotenv import load_dotenv


load_dotenv()


client = Groq(
    api_key=os.getenv(
        "GROQ_API_KEY"
    )
)


def recommend_offer(
    risk_score,
    reasons,
    rules,
    session,
):
    prompt = f"""
You are an AI conversion recovery agent for an ecommerce website.

Goal:
Prevent customer abandonment and improve conversion.

You are given:

1. Customer session
2. Predicted abandonment risk
3. Top risk reasons
4. Retrieved business rules

IMPORTANT:

The retrieved business rules are the ONLY source of truth.

You MUST:
- use only offers available in retrieved rules
- never invent discounts
- never invent cashback
- never invent delivery options
- never exceed allowed values
- select the best offer based on:
  - page_stage
  - risk_score
  - top reasons

Page-specific behavior:

If page_stage = "home":
- use homepage offers only
- focus on getting user to browse or start shopping

If page_stage = "product":
- focus on product urgency or new user coupon

If page_stage = "cart":
- focus on delivery / cart discount

If page_stage = "checkout":
- focus on payment completion

If no rule applies:
return action = "none"

Customer session:
{json.dumps(session, indent=2)}

Risk score:
{risk_score}

Top reasons:
{json.dumps(reasons, indent=2)}

Retrieved rules:
{json.dumps(rules, indent=2)}

Return ONLY valid JSON.

Format:

{{
  "action": "...",
  "message": "..."
}}
"""
    response = (
        client.chat.completions.create(
            model="llama-3.1-8b-instant",

            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],

            temperature=0.4,
        )
    )

    content = (
        response.choices[0]
        .message.content
    )

    return json.loads(
        content
    )