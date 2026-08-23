# 🎯 Number Guessing Game

An interactive number guessing game — **"The Secret Signal"** — available in two versions: a themed Python CLI game and a browser-based web app. Guess the hidden number using hot/cold clues, track your score, and rank up from Persistent Explorer to Mind Reader.


## 📌 Project Overview

The Number Guessing Game generates a random number within a specified range and challenges the player to guess the correct number.

The project provides:

- 🎯 Random number generation
- 🔢 User input and validation
- 🔥 Hot/Cold hints
- 🏆 Score and attempt tracking
- 🔄 Replay functionality
- 🌐 Interactive web interface
- 🐍 Python implementation of the game logic
- 
## ✨ Features

- 🎲 Custom number range (you choose the lower and upper bounds)
- 📈📉 Too High / Too Low feedback on every guess
- 🔥❄️ Hot & cold proximity hints that scale with your chosen range
- 🔐 One secret clue per round (odd/even, closer bound, last digit)
- 🏆 Rank system based on attempts used:
  - ≤ 3 attempts → 🏆 Mind Reader
  - ≤ 6 attempts → 🎯 Sharp Shooter
  - ≤ 9 attempts → 🙂 Steady Guesser
  - 10 attempts → 🧭 Persistent Explorer
- 🧮 Score system with points based on speed, plus streak tracking
- 🔁 Replay option without restarting
- 🛡️ Input validation (rejects invalid or repeated guesses)

Two ways to play:
| Version | File | Description |
|---|---|---|
| 🖥️ CLI | `Number_guessing.py` | Terminal game with colored panels and typewriter text |
| 🌐 Web | `index.html` | Browser game with live stats, best score saved locally |

## 🖥️ Demo — CLI Version

```
+----------------------------------------------------------+
|  THE SECRET SIGNAL                                       |
+----------------------------------------------------------+
|  Decode the hidden number before the signal disappears.  |
|  Choose your range, read the clues, and trust your...    |
+----------------------------------------------------------+

Enter the lower bound: 1
Enter the upper bound: 100

Attempt 1/10 | Guess or type 'clue': 50
  📉 Too high!  |  🌤️ Getting warmer

Attempt 2/10 | Guess or type 'clue': 30
🎉 BOOM! You got it — the number was 30!
Rank: 🏆 Mind Reader
```

## 🌐 Demo — Web Version

A dark-themed responsive UI with live attempt counter, score, best score (saved in browser storage), and streak tracking.

## 🚀 How to Run

### CLI Version
**Requirements:** Python 3.x (standard library only)

```bash
git clone https://github.com/24u0669-prog/SCT_SD_2.git
cd SCT_SD_2
python Number_guessing.py
```

### Web Version
Simply open `index.html` in any modern browser — no installation needed.

```bash
git clone https://github.com/24u0669-prog/SCT_SD_2.git
cd SCT_SD_2
# then just open index.html in your browser
```
## 🎮 How the Game Works

1. The game generates a random number.
2. The player enters a guess.
3. The program checks the guess.
4. The player receives a hint such as:
   - 🔥 Hot – The guess is close to the target.
   - ❄️ Cold – The guess is far from the target.
   - ✅ Correct – The player has guessed the number.
5. The number of attempts is tracked.
6. The player can start a new game and try again.

## 📂 Project Structure

```
SCT_SD_2/
├── Number_guessing.py   # Python CLI version
├── index.html            # Web version (HTML/CSS/JS)
├── README.md             # Project documentation
├── .gitignore             # Files ignored by Git
└── LICENSE                # MIT License
```

## 🛠️ Technologies Used

- **Python 3** — `random`, `time` (CLI version)
- **HTML5 / CSS3** — custom dark theme, responsive layout
- **JavaScript (Vanilla)** — game logic, localStorage for best score
- **Google Fonts** — Space Grotesk & DM Mono
- **Git & GitHub* – Version control and project hosting


## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## 👤 Author

Soundarya Umesh Barigidad,

Information Science Engineering Student

**24u0669-prog**
GitHub: [@24u0669-prog](https://github.com/24u0669-prog)

Internship
SkillCraft Technology

