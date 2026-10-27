"""Task 1.4: Business Prompt Builder.

Asks for a name, business type, problem and monthly budget, then prints a
ready-to-paste AI prompt for that business.
"""

name = input("Your name: ")
business = input("Business type: ")
problem = input("Biggest problem: ")

# input() always returns text, so int() converts it to a real number we can do maths with later.
# Keep asking until the user types a valid whole number, instead of crashing on bad input.
while True:
    try:
        budget = int(input("Monthly budget (PKR): "))
        break
    except ValueError:
        print("Please enter a whole number, e.g. 50000")

# Empty print adds a blank line so the output is easier to read after typing
print()
print(f"Welcome, {name}!")

# Including the budget stops the AI from suggesting solutions the client can't afford
prompt = (
    f"Suggest 3 AI solutions for a {business} that struggles with {problem}. "
    f"Budget: {budget} PKR per month."
)

print("--- Your AI Prompt ---")
print(prompt)