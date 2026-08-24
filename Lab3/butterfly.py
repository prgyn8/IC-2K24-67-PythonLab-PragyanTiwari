n = 5

upper_bound = list(range(0, (n * 2), 2))
lower_bound = upper_bound[:0:-1]

indices = lower_bound + upper_bound

for i in range(n * 2):
    calc_stars = ((n * 2) - indices[i - 1]) // 2
    print(calc_stars * ("*") + indices[i - 1] * " " + calc_stars * ("*"))
