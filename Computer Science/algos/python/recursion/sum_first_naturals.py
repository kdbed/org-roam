def sum_first_naturals(n):
    if n == 1:
        return 1  # base case
    else:
        return sum_first_naturals(n - 1) + n  # recursive case
