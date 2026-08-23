# 🎮 Number Guessing Game

A fun, interactive command-line number guessing game built in Python. The program generates a random number within a user-defined range and challenges the player to guess it — complete with hot/cold hints, a ranking system, and replayability.

## ✨ Features

- 🎲 Custom number range (you choose the lower and upper bounds)
- 📈📉 Too High / Too Low feedback on every guess
- 🔥❄️ Hot & Cold proximity hints to guide your guesses
- 🏆 Rank system based on how many attempts it took you
  - ≤ 3 attempts → 🏆 Mind Reader
  - ≤ 6 attempts → 🎯 Sharp Shooter
  - ≤ 9 attempts → 🙂 Steady Guesser
  - 10 attempts → 🐢 Persistent Soul
- ⌨️ Typewriter-style text effect for a more engaging feel
- 🛡️ Input validation (won't crash on invalid input)
- 🔁 Replay option without restarting the script

## 🖥️ Demo

```
==================================================
   🎮 WELCOME TO THE NUMBER GUESSING GAME 🎮
==================================================

Enter the lower bound: 1
Enter the upper bound: 100

🎲 I'm thinking of a number between 1 and 100...
You have 10 attempts. Let's see how sharp you are!

Attempt 1/10 — Your guess: 50
📉 Too high! ❄️  Cold.

Attempt 2/10 — Your guess: 25
📈 Too low! ♨️  Warm...

Attempt 3/10 — Your guess: 30
🎉 BOOM! You got it — the number was 30!
You nailed it in 3 attempt(s). Rank: 🏆 Mind Reader
```

## 🚀 How to Run

**Requirements:** Python 3.x (no external libraries needed)

```bash
git clone https://github.com/24u0669-prog/SCT_SD_2.git
cd SCT_SD_2
python Number_guessing.py
```

## 📂 Project Structure

```
SCT_SD_2/
├── Number_guessing.py   # Main game script
├── README.md            # Project documentation
├── .gitignore            # Files ignored by Git
└── LICENSE               # MIT License
```

## 🛠️ Built With

- Python 3 — Standard library only (`random`, `time`)

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## 👤 Author

**24u0669-prog**
GitHub: [@24u0669-prog](https://github.com/24u0669-prog)
