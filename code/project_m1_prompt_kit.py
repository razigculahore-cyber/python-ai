"""Module 1 Project: AI Prompt Kit for a Local Business.

Asks a small business owner 5 quick questions and prints 4 ready-to-use AI
prompts (marketing, customer service, growth, WhatsApp auto-reply) that they
can paste into Ollama, Claude or ChatGPT. Built for shop owners who want AI
help but don't know what to type.
"""

business_name = input("Business name: ")
business_type = input("Business type: ")
city = input("City: ")
customers = input("Main customers: ")
# input() always gives text; int() turns the budget into a number so it reads as an amount, not a label
budget = int(input("Monthly budget (PKR): "))

# A blank line separates the questions from the results so the owner sees where the prompts start
print()
print("=========================================")
print(f"   AI Prompt Kit for {business_name}")
print("=========================================")

# Each prompt names a role, a task, the audience and a number, because vague prompts get vague answers
print()
print("[1] Marketing")
print(f"You are a social media manager. Write a short Instagram post for {business_name}, a {business_type} in {city}.")
print(f"Target {customers}. Friendly tone, under 60 words, 3 hashtags and 1 call to action.")

print()
print("[2] Customer Service")
print(f"You are the manager of {business_name}. Write a polite reply to a customer")
print("whose order arrived late. Apologise, give no excuses, offer 10% off the next order. Max 4 lines.")

# The budget is in the prompt so the AI only suggests tools the owner can actually afford
print()
print("[3] Growth")
print(f"Suggest 3 low-cost AI tools a {business_type} in {city} can use")
print(f"to attract {customers} with a budget of {budget} PKR per month.")
print("For each tool give the name, what it does and the monthly cost in PKR.")

print()
print("[4] WhatsApp Auto-Reply")
print(f"Write a WhatsApp auto-reply for {business_name}, a {business_type} in {city}, sent when the owner is busy.")
print("Thank the customer, say we reply within 30 minutes, and ask for their order and pickup time. Max 3 lines, English and Roman Urdu.")
