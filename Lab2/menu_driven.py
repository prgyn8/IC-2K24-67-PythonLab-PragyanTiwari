def armstrong(n):
    digits = len(str(n))
    total = 0
    temp = n

    while temp > 0:
        digit = temp % 10
        total += digit**digits
        temp //= 10

    return total == n


def prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def perfect(n):
    if n <= 1:
        return False

    total = 0

    for i in range(1, n):
        if n % i == 0:
            total += i

    return total == n


def number_palindrome(n):
    original = n
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n //= 10

    return original == reverse


def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b


def patterns(n):
    print("\nStar Pattern:")
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end=" ")
        print()

    print("\nNumber Pattern:")
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

    print("\nPyramid Pattern:")
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        for j in range(i):
            print("* ", end="")
        print()


while True:
    print("\n----- MENU -----")
    print("1. Armstrong Number")
    print("2. Prime Number")
    print("3. Perfect Number")
    print("4. Palindrome")
    print("5. Fibonacci Series")
    print("6. Pattern Printing")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        n = int(input("Enter a number: "))

        if armstrong(n):
            print(n, "is an Armstrong number.")
        else:
            print(n, "is not an Armstrong number.")

    elif choice == "2":
        n = int(input("Enter a number: "))

        if prime(n):
            print(n, "is a prime number.")
        else:
            print(n, "is not a prime number.")

    elif choice == "3":
        n = int(input("Enter a number: "))

        if perfect(n):
            print(n, "is a perfect number.")
        else:
            print(n, "is not a perfect number.")

    elif choice == "4":
        n = int(input("Enter a number: "))

        if number_palindrome(n):
            print(n, "is a palindrome.")
        else:
            print(n, "is not a palindrome.")

    elif choice == "5":
        n = int(input("Enter number of terms: "))

        if n > 0:
            fibonacci(n)
            print()
        else:
            print("Please enter a positive number.")

    elif choice == "6":
        n = int(input("Enter number of rows: "))

        if n > 0:
            patterns(n)
        else:
            print("Please enter a positive number.")

    elif choice == "7":
        print("Program ended.")
        break

    else:
        print("Invalid choice. Please try again.")
