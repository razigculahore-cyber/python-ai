"""Task 1.8: Business Helper Bot (Module 1 Final).

A rule-based chatbot for Crust & Crumb Bakers, Sheikhupura. It answers the
questions customers ask all day (timings, location, delivery, prices,
custom cakes) and counts the ones it cannot answer yet, so the owner knows
what to add next.
"""

BOT = "Crust & Crumb Bot"

message_count = 0
unanswered_count = 0
complaint_count = 0

print(f"{BOT}: Hi! Ask about timings, location, delivery, prices or custom cakes. Type 'bye' to exit.")
# Asked once before the loop so every reply can use the name without asking again
name = input(f"{BOT}: What is your name?  ").strip().title()

while True:
    message = input(f"{name}: ").strip().lower()
    if message == "":
        continue
    message_count += 1

    if message == "bye":
        print(f"{BOT}: Take care, {name}!")
        break
    # Complaints are checked first so an unhappy customer is never answered with an FAQ
    # (e.g. "my cake delivery is late" must not get the delivery-fee reply)
    elif "late" in message or "complaint" in message or "refund" in message or "stale" in message:
        complaint_count += 1
        print(f"{BOT}: Sorry about that, {name}. The manager will call you within 1 hour.")
    elif "agent" in message or "human" in message:
        print(f"{BOT}: Connecting you to a human...")
        break
    # "hi" hides inside words like "which" and "this", so greetings use == and startswith, not in
    elif message == "hi" or message == "hello" or message.startswith("salam") or message.startswith("assalam"):
        print(f"{BOT}: Hello {name}! How can I help you today?")
    elif "timing" in message or "open" in message or "hours" in message:
        print(f"{BOT}: We are open 8 am to 11 pm, every day.")
    elif "location" in message or "address" in message or "where" in message:
        print(f"{BOT}: We are on Lahore Road, near the main chowk, Sheikhupura.")
    elif "deliver" in message:
        print(f"{BOT}: Delivery is 150 PKR, free on orders of 3,000 PKR or more.")
    elif "price" in message or "rate" in message or "cost" in message or "how much" in message:
        print(f"{BOT}: Cupcake 200 PKR, brownie 250 PKR, 1 kg chocolate cake 1,800 PKR.")
    elif "custom" in message or "birthday" in message or "order" in message:
        print(f"{BOT}: Custom cakes need 24 hours notice. Send your design on WhatsApp.")
    else:
        unanswered_count += 1
        print(f"{BOT}: I am not sure yet. In Module 2, an AI will answer: You are the friendly assistant of Crust & Crumb Bakers. Answer in 2 lines: {message}")

print("========================================")
print(f"Chat summary: {message_count} messages, {unanswered_count} unanswered, {complaint_count} complaints.")
