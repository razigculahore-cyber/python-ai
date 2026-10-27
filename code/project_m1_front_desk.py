"""Module 1 Project: AI Front Desk for Crust & Crumb Bakers, Sheikhupura.

A front desk assistant for a local bakery. It answers common questions with
free rules, gives exact price quotes with /quote (bulk discount + delivery),
turns everything else into a cost-checked AI prompt (private questions go to
a free local model), and ends with a session report for the owner.
"""

BOT_NAME = "Crust & Crumb Desk"
BUSINESS = "Crust & Crumb Bakers"
DELIVERY_FEE = 200
FREE_DELIVERY_LIMIT = 3000
BULK_QUANTITY = 10
BULK_DISCOUNT_RATE = 0.10
CLOUD_PRICE_PER_1K = 0.1  # example price in PKR, not a real quote

message_count = 0
rule_answers = 0
unanswered_count = 0
quote_count = 0
quoted_value = 0
ai_cost = 0.0
complaint_count = 0

print("==================================================")
print(f"   {BOT_NAME}: rules, quotes and AI-ready prompts")
print("==================================================")
print("Ask anything, type /quote for a price, or bye to exit.")
# Asked once before the loop so every reply and prompt can be personal
customer = input(f"{BOT_NAME}: What is your name? ").strip().title()

while True:
    message = input(f"{customer}: ").strip().lower()
    # Empty input is not a message, so it is not counted and we simply ask again
    if message == "":
        continue
    message_count += 1

    if message == "bye":
        rule_answers += 1
        print(f"{BOT_NAME}: Goodbye, {customer}!")
        break
    # Complaints come first so an unhappy customer always reaches a person,
    # even if the message also contains words like "order" or "delivery"
    elif "refund" in message or "complaint" in message or "late" in message or "stale" in message:
        rule_answers += 1
        complaint_count += 1
        print(f"{BOT_NAME}: Sorry about that. A manager will call you within 1 hour.")
    elif "agent" in message or "human" in message:
        print(f"{BOT_NAME}: Connecting you to a human...")
        break
    elif message == "/quote":
        item = input(f"{BOT_NAME}: Which item? ").strip().lower()
        quantity_text = input(f"{BOT_NAME}: How many? ").strip()
        # isdigit() stops a crash when someone types "twelve" instead of 12
        if not quantity_text.isdigit() or quantity_text == "0":
            print(f"{BOT_NAME}: Please type the quantity as a number, like 12.")
            continue
        quantity = int(quantity_text)

        if item == "cupcake":
            unit_price = 250
        elif item == "brownie":
            unit_price = 300
        elif item == "chocolate cake":
            unit_price = 1800
        elif item == "pizza bread":
            unit_price = 400
        else:
            unit_price = 0

        if unit_price == 0:
            print(f"{BOT_NAME}: Sorry, {item} is not on our menu.")
        else:
            subtotal = unit_price * quantity
            if quantity >= BULK_QUANTITY:
                discount = round(subtotal * BULK_DISCOUNT_RATE)
            else:
                discount = 0
            # Free delivery is judged on the price after discount, because that is what the customer really pays
            if subtotal - discount >= FREE_DELIVERY_LIMIT:
                delivery = 0
            else:
                delivery = DELIVERY_FEE
            total = subtotal - discount + delivery
            quote_count += 1
            quoted_value += total
            print(f"{BOT_NAME}: {quantity} x {item} = {subtotal:,} PKR")
            print(f"     Discount: -{discount:,} PKR | Delivery: {delivery:,} PKR")
            print(f"     Total: {total:,} PKR")
    # "hi" hides inside "which" and "this", so greetings use == and startswith instead of in
    elif message == "hi" or message == "hello" or message.startswith("salam") or message.startswith("assalam"):
        rule_answers += 1
        print(f"{BOT_NAME}: Hello {customer}! Ask about hours, location, delivery or menu, or type /quote.")
    elif "hours" in message or "timing" in message or "open" in message:
        rule_answers += 1
        print(f"{BOT_NAME}: We are open 8 am to 11 pm, every day.")
    elif "location" in message or "where" in message or "your address" in message:
        rule_answers += 1
        print(f"{BOT_NAME}: Lahore Road, near the main chowk, Sheikhupura.")
    elif "deliver" in message:
        rule_answers += 1
        print(f"{BOT_NAME}: Delivery is {DELIVERY_FEE} PKR, free on orders of {FREE_DELIVERY_LIMIT:,} PKR or more.")
    elif "menu" in message or "price" in message or "rate" in message:
        rule_answers += 1
        print(f"{BOT_NAME}: Cupcake 250, brownie 300, pizza bread 400, chocolate cake 1,800 PKR. 10% off for 10 or more.")
    else:
        unanswered_count += 1
        # Cut to 150 characters so one long message cannot run up the AI bill
        question = message.capitalize()[:150]
        tokens = round(len(question) / 4)
        # Private details never leave the shop's computer, so they go to the free local model
        if "phone" in message or "cnic" in message or "my address" in message:
            model = "llama3.2 (local, private)"
            cost = 0
        else:
            model = "small cloud model (cheap)"
            cost = tokens / 1000 * CLOUD_PRICE_PER_1K
        ai_cost += cost
        prompt = f"""You are the assistant of {BUSINESS}, a bakery in Sheikhupura.
     Answer {customer} in 2 short lines. Question: {question}"""
        print(f"{BOT_NAME}: Good question! Routed to: {model} (~{tokens} tokens)")
        print(f"     Prompt: {prompt}")

print("==================================================")
print("Session report")
print(f"Messages: {message_count} | Answered by rules: {rule_answers} | Unanswered: {unanswered_count}")
print(f"Quotes: {quote_count} | Quoted value: {quoted_value:,} PKR")
print(f"Complaints: {complaint_count}")
print(f"Estimated AI cost for unanswered questions: {ai_cost:.4f} PKR")
print("==================================================")
