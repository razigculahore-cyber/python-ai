"""Task 1.7: Smart Model Router.

Sends private data to a free local model, code questions to a strong cloud
model and everything else to a cheap one, then estimates the cost.
"""

task = input("Task (code / private / chat): ").strip().lower()
tokens = int(input("Estimated tokens: "))
paid_user = input("Is this a paid user? (yes/no): ").strip().lower() == "yes"

# Private data is checked first so it can never leak to a cloud model by accident
if task == "private":
    model = "llama3.2 (local, Ollama)"
    price = 0
elif task == "code":
    model = "claude (cloud, strong at code)"
    price = 0.8
else:
    # Anything unknown falls back to the cheap model, the safest choice for the bill
    model = "small cloud model (cheap)"
    price = 0.1

if tokens > 4000:
    print("Warning: long request, consider shortening it.")
else:
    print("Length is fine.")

# Free users are limited so long requests don't eat the company's budget
if not paid_user and tokens > 2000:
    print("Upgrade to send long requests.")

cost = tokens / 1000 * price
print(f"Chosen model: {model}")
print(f"Estimated cost: {cost:.2f} PKR")
