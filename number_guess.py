import random
import sys

BANNER = """
===============================
     NUMBER  GUESS  GAME
===============================
I picked a number between {low} and {high}.
You have {tries} tries. Good luck!
"""

def play(low=1, high=100, tries=7):
    print(BANNER.format(low=low, high=high, tries=tries))
    secret = random.randint(low, high)

    for attempt in range(1, tries + 1):
        while True:
            raw = input(f"[Try {attempt}/{tries}] Guess a number: ").strip()
            if raw.lower() in {"q", "quit", "exit"}:
                print("Bye! 👋")
                sys.exit(0)
            if raw.isdigit():
                guess = int(raw)
                break
            print("Please type a whole number (or 'q' to quit).")

        if guess < low or guess > high:
            print(f"Out of range! Enter between {low} and {high}.")
            continue

        if guess == secret:
            print(f"🎉 Correct! {guess} is the number. You won in {attempt} tries!")
            return True
        elif guess < secret:
            print("Too low ⬇️")
        else:
            print("Too high ⬆️")

    print(f"😬 Out of tries. The number was {secret}.")
    return False


def menu():
    print("Choose difficulty:")
    print("1) Easy   (1–50,   8 tries)")
    print("2) Normal (1–100,  7 tries)")
    print("3) Hard   (1–200,  7 tries)")
    print("4) Insane (1–500,  9 tries)")
    choice = input("Enter 1/2/3/4: ").strip()

    if choice == "1":
        return dict(low=1, high=50, tries=8)
    if choice == "2":
        return dict(low=1, high=100, tries=7)
    if choice == "3":
        return dict(low=1, high=200, tries=7)
    if choice == "4":
        return dict(low=1, high=500, tries=9)
    print("Defaulting to Normal.")
    return dict(low=1, high=100, tries=7)


if __name__ == "__main__":
    while True:
        settings = menu()
        play(**settings)
        again = input("Play again? (y/n): ").strip().lower()
        if again not in {"y", "yes"}:
            print("Thanks for playing!")
            break
