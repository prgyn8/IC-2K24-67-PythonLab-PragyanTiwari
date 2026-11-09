# Lab 5 — Menu applications

## 1. ATM simulation

**Question:** Simulate a simple ATM with PIN check, balance, deposit, and withdraw.

**Approach:** PIN is checked once. A `while` loop shows a menu and updates balance on deposit. Withdrawal only happens when the amount is not greater than balance.

File: `atm.py`

## 2. Student grade calculator

**Question:** Enter marks for five subjects and get average and grade from a small menu.

**Approach:** Menu option 1 reads five marks, computes average, and sets grade with `if-elif` on average bands. Option 2 prints the stored average and grade.

File: `grade.py`

## 3. Reverse guessing game

**Question:** The computer guesses a number the user is thinking of between a start and end value.

**Approach:** Binary search: each guess is the middle of the current range. User says high, low, or correct, and I shrink `low` or `high` until the number is found.

File: `rev_guessing.py`

## 4. Guessing game with hints and scoring

**Question:** Guess a random number; lose points on wrong guesses and get even/odd and multiple-of-5 hints.

**Approach:** Score starts at 100 and drops by 10 after each wrong guess. After every miss I print hints using `% 2` and `% 5`. The game stops on correct guess or after 10 attempts.

File: `hint.py`

## 5. Combined application

**Question:** One main menu to open ATM, grade calculator, or guessing game.

**Approach:** Three functions handle each program. The main `while` loop calls the chosen function and returns to the menu when that program exits; choice 4 ends everything.

File: `combined.py`
