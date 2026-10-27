"""Task 1.6: Prompt Cleaner.

Cleans a customer's messy name and question, measures it in characters and
tokens, and builds a safely sized prompt for an AI tutor.
"""

PRICE_PER_1K_TOKENS = 0.5

raw_name = input("Your name: ")
raw_question = input("Your question: ")

# Customers type random spaces and capitals; cleaning first keeps the prompt tidy and the counts honest
name = raw_name.strip().title()
question = raw_question.strip().capitalize()
# Mask rude words before anything is sent to an AI or stored in logs
question = question.replace("stupid", "***")

characters = len(question)
# About 4 characters make one token, a rough rule good enough for cost estimates
tokens = round(characters / 4)
cost = tokens / 1000 * PRICE_PER_1K_TOKENS

print("========================================")
print(f"Cleaned question: {question}")
print(f"Characters: {characters}, about {tokens} tokens")
print(f"Estimated cost: {cost:.2f} PKR")
# .lower() first so "Python", "PYTHON" and "python" all match
print(f"Mentions Python: {'python' in question.lower()}")
print("========================================")

# [:150] caps the question so one very long message cannot blow up the token bill
prompt = f"""You are a friendly Python tutor.
Greet {name} by name and answer in 3 short lines.
Question: {question[:150]}"""
print(prompt)
