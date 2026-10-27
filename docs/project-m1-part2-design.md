# Module 1 Project Part 2: AI Front Desk Design

**Business:** Crust & Crumb Bakers, bakery, Sheikhupura
**Script:** [code/project_m1_front_desk.py](../code/project_m1_front_desk.py)

## Intents (checked in this order)

| # | Intent | Keywords | Reply |
|---|---|---|---|
| 1 | Exit | `bye` (exact) | Goodbye + session report |
| 2 | Complaint | refund, complaint, late, stale | A manager will call you within 1 hour |
| 3 | Human handover | agent, human | Connecting you to a human... (ends chat) |
| 4 | Quote | `/quote` (exact) | Asks item + quantity, prints the price |
| 5 | Greeting | `hi`, `hello` (exact), starts with salam / assalam | Hello + what the desk can do |
| 6 | Hours | hours, timing, open | Open 8 am to 11 pm, every day |
| 7 | Location | location, where, your address | Lahore Road, near the main chowk |
| 8 | Delivery | deliver | 200 PKR, free from 3,000 PKR |
| 9 | Menu | menu, price, rate | Item prices + bulk discount |
| 10 | Fallback | anything else | AI-ready prompt, routed local or cloud |

Complaint comes before quote, greeting and delivery so "my delivery is late" reaches a manager and not the delivery-fee FAQ.

## Business rules

| Rule | Value |
|---|---|
| Item prices | cupcake 250, brownie 300, pizza bread 400, chocolate cake 1,800 PKR |
| Bulk discount | 10% off for 10 or more of one item |
| Delivery | 200 PKR, free when the total **after discount** is 3,000 PKR or more |
| Private words | phone, cnic, my address → llama3.2 local, 0 PKR |
| Cloud price | 0.1 PKR per 1K tokens (example price) |
| Question limit | 150 characters, tokens ≈ characters / 4 |

## Rule tests

| You type | Expected | Got | Pass? |
|---|---|---|---|
| `  WHAT are your hours  ` | Hours | We are open 8 am to 11 pm, every day. | ✅ |
| `which cake is best?` | Fallback, not a greeting | Routed to small cloud model (~5 tokens) | ✅ |
| `my order is late` | Manager reply | A manager will call you within 1 hour. | ✅ |
| `/quote`, 1 chocolate cake | Delivery fee charged | 1,800 + 200 delivery = 2,000 PKR | ✅ |
| `/quote`, 3 chocolate cakes | Delivery free | 5,400 PKR, delivery 0 | ✅ |
| `/quote`, 12 cupcakes | Discount applied | 3,000 − 300 + 200 = 2,900 PKR (2,700 is below the free limit) | ✅ |
| `/quote`, pizza | Not on our menu, no crash | Sorry, pizza is not on our menu. | ✅ |
| `/quote`, brownie, `twelve` | Polite reply, no crash (bonus) | Please type the quantity as a number, like 12. | ✅ |
| `can I change my phone number on the order?` | Local model, cost 0 | Routed to llama3.2 (local, private) | ✅ |
| Enter with no text | Asks again | Prompt shown again, not counted | ✅ |
| `human` | Connecting you to a human... (bonus) | Connecting you to a human... + report | ✅ |
| `BYE` | Goodbye + report | Goodbye, Ali Raza! + session report | ✅ |
