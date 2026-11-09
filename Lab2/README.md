# Lab 2 — Loops and logic

## 1. Armstrong number

**Question:** Check if a number is Armstrong, and list all Armstrong numbers in a given range.

**Approach:** I counted digits, raised each digit to that power using a `while` loop, and compared the sum to the original. The same logic runs inside a `for` loop over the range.

File: `armstrong.py`

## 2. Prime number

**Question:** Check if a number is prime and print all primes up to a limit.

**Approach:** I used a loop from 2 to `num - 1` to test divisibility with a flag. For the limit, I repeated this check for every number from 2 to the limit.

File: `prime.py`

## 3. Perfect number

**Question:** Check if a number is perfect and list perfect numbers up to a limit.

**Approach:** I wrote a function that adds all proper divisors with a `for` loop and compares the total to `n`. I call it for one number and again in a loop up to the limit.

File: `perfect_no.py`

## 4. Palindrome

**Question:** Check whether a number and a string are palindromes.

**Approach:** For the number I built the reverse with `% 10` and `// 10` in a loop. For the string I compared it to `[::-1]`.

File: `palindrome.py`

## 5. Fibonacci series

**Question:** Print the Fibonacci series for a given number of terms.

**Approach:** I kept two variables `a` and `b`, printed `a` each step, then updated them to the next pair in a `for` loop.

File: `fibonacci.py`

## 6. Pattern printing

**Question:** Print star triangle, number pattern, and pyramid for `n` rows.

**Approach:** Nested `for` loops control rows and columns. The pyramid adds leading spaces before stars.

Files: `pattern/right_triangle.py`, `pattern/number_pattern.py`, `pattern/pyramid.py`

## 7. Menu-driven application

**Question:** Run Armstrong, prime, perfect, palindrome, Fibonacci, and patterns from one menu.

**Approach:** Each task is a function. A `while True` loop shows the menu and calls the matching function until the user picks exit.

File: `menu_driven.py`

## 8. Number guessing game

**Question:** Guess a random number between 1 and 100 within a limited number of tries.

**Approach:** `random.randint` picks the secret number. A `while` loop compares the guess and prints too high or too low until correct or attempts run out.

File: `guess_the_number.py`
