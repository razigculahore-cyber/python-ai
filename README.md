# Python for AI

**Student:** Raza (Sheikhupura) · **Course:** Python for AI, The School of AI

**AI goal:** become an Applied AI Engineer who automates real business operations, starting with a smart card delivery system.

## How to run

```bash
uv run main.py
cd code
uv run lesson_01_intro.py
```

## Lessons done

| Lesson | Task | File |
|---|---|---|
| 1.1 | AI career intro | [code/lesson_01_intro.py](code/lesson_01_intro.py) |
| 1.2 | Toolkit proof | [code/lesson_02_toolkit.py](code/lesson_02_toolkit.py), [docs/ollama-first-chat.md](docs/ollama-first-chat.md), [docs/setup-check.png](docs/setup-check.png) |
| 1.3 | Client-ready repo | this README |
| 1.4 | Business prompt builder | [code/lesson_04_print_input.py](code/lesson_04_print_input.py), [docs/prompt-test.md](docs/prompt-test.md) |
| 1.5 | AI model profile card | [code/lesson_05_variables.py](code/lesson_05_variables.py) |
| 1.6 | Prompt cleaner | [code/lesson_06_strings_prompts.py](code/lesson_06_strings_prompts.py) |
| 1.7 | Smart model router | [code/lesson_07_conditions.py](code/lesson_07_conditions.py) |
| 1.8 | Business helper bot | [code/lesson_08_mini_chatbot.py](code/lesson_08_mini_chatbot.py) |

## Task 1.8: Business Helper Bot design

A rule-based chatbot for Crust & Crumb Bakers, Sheikhupura. Rules are checked top to bottom.

| Intent | Keywords | Reply |
|---|---|---|
| Exit | `bye` (exact) | Take care, {name}! + chat summary |
| Complaint (first) | late, complaint, refund, stale | Sorry, the manager will call you within 1 hour |
| Human handover | agent, human | Connecting you to a human... |
| Greeting | `hi`, `hello` (exact), starts with salam / assalam | Hello {name}! How can I help? |
| Timings | timing, open, hours | Open 8 am to 11 pm, every day |
| Location | location, address, where | Lahore Road, near the main chowk, Sheikhupura |
| Delivery | deliver | 150 PKR, free from 3,000 PKR |
| Prices | price, rate, cost, how much | Cupcake 200, brownie 250, 1 kg chocolate cake 1,800 PKR |
| Custom cakes | custom, birthday, order | 24 hours notice, send design on WhatsApp |
| Fallback | anything else | Counted as unanswered + the AI prompt for Module 2 |

**Run:** `cd code` then `uv run lesson_08_mini_chatbot.py`
