"""Task 1.5: AI Model Profile Card.

Shows one model's profile using all 4 basic types (str, int, float, bool)
and estimates what a chat costs, per chat and per month.
"""

model_name = "llama3.2"
# Context window from ollama.com/library; stored as int because it is a whole token count
context_window = 128000
# Example price only: llama3.2 runs locally for free, this shows what a cloud plan might charge
price_per_1k_tokens = 0.5
runs_locally = True

print("--- AI Model Profile Card ---")
print(f"Model: {model_name} {type(model_name)}")
print(f"Context window: {context_window} tokens {type(context_window)}")
print(f"Price per 1K tokens: {price_per_1k_tokens} PKR {type(price_per_1k_tokens)}")
print(f"Runs locally: {runs_locally} {type(runs_locally)}")

# input() returns text, so int() is needed before we can multiply with it
tokens_per_chat = int(input("Tokens per chat: "))
chat_cost = tokens_per_chat / 1000 * price_per_1k_tokens
print(f"Estimated cost: {round(chat_cost, 2)} PKR")

chats_per_day = int(input("Chats per day: "))
# 30 days is a simple monthly estimate the client can check by hand
monthly_cost = chat_cost * chats_per_day * 30
print(f"Estimated monthly cost: {round(monthly_cost, 2)} PKR")
