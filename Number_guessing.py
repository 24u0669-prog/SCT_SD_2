import random
import time


MAX_ATTEMPTS = 10

RESET = "\033[0m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
DIM = "\033[2m"


def paint(text, color):
    """Apply a terminal color to text."""
    return f"{color}{text}{RESET}"


def panel(title, lines, color=CYAN):
    """Print a clean information panel."""
    width = 58
    print(paint("+" + "-" * width + "+", color))
    print(paint(f"|  {title:<{width - 2}}|", color))
    print(paint("+" + "-" * width + "+", color))
    for line in lines:
        print(paint(f"|  {line:<{width - 2}}|", color))
    print(paint("+" + "-" * width + "+", color))


def typewriter(text, delay=0.02):
    """Print text with a typewriter effect for flair."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def show_banner():
    """Display the game's secret-agent themed title."""
    panel("THE SECRET SIGNAL", [
        "Decode the hidden number before the signal disappears.",
        "Choose your range, read the clues, and trust your instincts.",
    ])


def get_rank(attempts):
    if attempts <= 3:
        return "🏆 Mind Reader"
    elif attempts <= 6:
        return "🎯 Sharp Shooter"
    elif attempts <= 9:
        return "🙂 Steady Guesser"
    else:
        return "🧭 Persistent Explorer"


def get_heat(secret, guess, low, high):
    """Create a hot/cold hint that scales with the selected range."""
    distance = abs(secret - guess)
    range_size = high - low
    ratio = distance / range_size

    if ratio <= 0.05:
        return "🔥 BLAZING HOT"
    if ratio <= 0.15:
        return "🌡️ Very warm"
    if ratio <= 0.30:
        return "🌤️ Getting warmer"
    if ratio <= 0.50:
        return "🌬️ Cool breeze"
    return "❄️ Ice cold"


def show_meter(attempts):
    """Show remaining attempts as a small visual meter."""
    remaining = MAX_ATTEMPTS - attempts
    meter = "#" * remaining + "." * attempts
    meter_color = GREEN if remaining > 3 else YELLOW
    print(f"{paint('SIGNAL', CYAN)}  {paint(meter, meter_color)}  {remaining}/{MAX_ATTEMPTS} left\n")


def give_clue(secret, low, high):
    """Offer a random clue to make each round more surprising."""
    clues = [
        f"🔐 Clue: the number is {'even' if secret % 2 == 0 else 'odd'}.",
        f"🔐 Clue: it is {'closer to the lower' if secret - low < high - secret else 'closer to the upper'} bound.",
        f"🔐 Clue: its last digit is {secret % 10}.",
    ]
    return random.choice(clues)


def play_round(low, high, score, streak):
    """Play one round and return the updated score and streak."""
    secret = random.randint(low, high)
    attempts = 0
    guesses = []
    clue_used = False

    panel("ROUND BRIEFING", [
        f"Target range : {low} to {high}",
        f"Attempts     : {MAX_ATTEMPTS}",
        "Special move : type 'clue' for one secret hint",
    ])
    print()

    while attempts < MAX_ATTEMPTS:
        show_meter(attempts)
        try:
            raw_guess = input(
                f"Attempt {attempts + 1}/{MAX_ATTEMPTS} | Guess or type 'clue': "
            ).strip().lower()
            if raw_guess == "clue":
                if clue_used:
                    print("🕵️ You already used your clue this round.\n")
                else:
                    print(give_clue(secret, low, high) + "\n")
                    clue_used = True
                continue
            guess = int(raw_guess)
        except ValueError:
            print("⚠️ That's not a number. Enter a number or type 'clue'.\n")
            continue

        if not low <= guess <= high:
            print(f"📡 Stay inside the signal range: {low} to {high}.\n")
            continue

        if guess in guesses:
            print("🔁 You already tested that number. Try a new frequency.\n")
            continue

        guesses.append(guess)
        attempts += 1

        if guess == secret:
            typewriter(paint(f"\n🎉 BOOM! You got it — the number was {secret}!", GREEN))
            points = (MAX_ATTEMPTS - attempts + 1) * 10
            score += points
            streak += 1
            panel("MISSION COMPLETE", [
                f"Solved in    : {attempts} attempt(s)",
                f"Rank         : {get_rank(attempts)}",
                f"Points earned: +{points}",
                f"Total score  : {score}   |   Streak: {streak}",
            ], GREEN)
            return score, streak

        if guess < secret:
            direction = "📈 Too low!"
        else:
            direction = "📉 Too high!"

        print(paint(f"  {direction}  |  {get_heat(secret, guess, low, high)}", YELLOW))
        print(paint(f"  Guess logged: {guess}", DIM) + "\n")

    streak = 0
    typewriter(paint(f"\n💀 Signal lost! The number was {secret}.", RED))
    panel("MISSION DEBRIEF", [
        "The target escaped this time.",
        f"Score        : {score}",
        "Streak       : reset to 0",
    ], RED)
    return score, streak


def get_bounds():
    """Keep asking until the player supplies a usable range."""
    while True:
        try:
            low = int(input("Enter the lower bound: "))
            high = int(input("Enter the upper bound: "))
            if low >= high:
                print("⚠️  Lower bound must be less than upper bound.")
                continue
            return low, high
        except ValueError:
            print("⚠️  Please enter valid numbers.")


def ask_to_replay():
    """Accept only yes or no; repeat the question for anything else."""
    while True:
        answer = input("\nPlay again with the same range? (yes/no): ").strip().lower()
        if answer in {"yes", "y"}:
            return True
        if answer in {"no", "n"}:
            return False
        print("Please enter only 'yes' or 'no'.")


def main():
    show_banner()
    score = 0
    streak = 0

    low, high = get_bounds()
    while True:
        score, streak = play_round(low, high, score, streak)
        if ask_to_replay():
            continue
        typewriter(f"\n👋 Final score: {score}. Thanks for playing, Signal Seeker!")
        return

if __name__ == "__main__":
    main()