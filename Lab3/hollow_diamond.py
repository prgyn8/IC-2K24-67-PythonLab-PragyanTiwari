n = int(input("enter any odd positive number : "))
mid = n // 2


lower_bound = list(range(mid + 1))
upper_bound = lower_bound[(mid - 1) :: -1]

indices = lower_bound + upper_bound

for i in indices:
    if i == 0:
        print(mid * " " + "*")
    else:
        print((mid - i) * " " + "*" + (2 * i - 1) * " " + "*" + (mid - i) * " ")
