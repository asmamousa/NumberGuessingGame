# 🎯 Number Guessing Game (CLI)

A simple command-line Number Guessing Game written in **Python**. The player selects a difficulty level and tries to guess a randomly generated number within a limited number of attempts. After failing a round, the player can choose to try again.

This project is built as part of the **roadmap.sh backend learning path assignment**.

🔗 **Assignment link:** https://roadmap.sh/projects/number-guessing-game

---

## 📌 Features

- Three difficulty levels: Easy, Medium, Hard
- Different number of attempts per difficulty
- Random number generation (1–100) per round
- Input validation (prevents crashes on invalid input)
- Replay option after running out of attempts
- Clear user feedback for each guess

---

## 🛠 Requirements

- Python **3.8+**
- No external dependencies (standard library only)

---

## ▶️ How to Run

Clone the repository and run the script:

```bash
python main.py
```

> Replace `main.py` with the actual filename if different.

---

## 🎮 How to Play (User Guide)

### 1️⃣ Select Difficulty Level

When the game starts, you will be prompted to choose a difficulty level:

```
1. Easy   (10 chances)
2. Medium (5 chances)
3. Hard   (3 chances)
```

Enter **1**, **2**, or **3**.

---

### 2️⃣ Guess the Number

- The game will randomly choose a number between **1 and 100**.
- Enter your guess when prompted.

Example:
```
Enter your guess: 42
```

The game will guide you:
- `The number is greater than X`
- `The number is less than X`

---

### 3️⃣ Attempts & Last Chance

- Each difficulty has a limited number of attempts.
- When you reach the final attempt, the game will warn you:

```
This is your last chance
```

---

### 4️⃣ Running Out of Attempts

If you exceed the allowed attempts, you will be asked:

```
You have exceeded the chances to guess, would you like another round?
Enter y or n:
```

- Enter **y** → start a new round with a new number
- Enter **n** → exit the game

---

### 5️⃣ Winning the Game 🎉

If you guess the correct number:

```
Congratulations! You won in round 2 with 3 attempt(s).
```

The game will then exit.

---

## ⚙️ Game Logic Overview

- **Rounds**: Each failed game can start a new round
- **Attempts**: Reset every round
- **Difficulty**: Determines maximum attempts per round
- **Random Number**: Regenerated every round

---





