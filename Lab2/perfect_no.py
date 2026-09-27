def is_perfect(n):
    if n <= 1:
        return False

    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i

    return total == n


n = int(input("Enter a positive number: "))

if n > 0:
    if is_perfect(n):
        print(n, "is a perfect number.")
    else:
        print(n, "is not a perfect number.")
else:
    print("Please enter a positive number.")


limit = int(input("Enter the limit: "))

if limit > 0:
    print("Perfect numbers:", end=" ")

    for i in range(1, limit + 1):
        if is_perfect(i):
            print(i, end=" ")
else:
    print("Please enter a positive limit.")
