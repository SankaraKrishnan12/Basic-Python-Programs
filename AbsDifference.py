def difference(n):
    diff = n - 17
    if n > 17:
        diff = 2 * diff
    return abs(diff)
n = int(input("Enter a number : "))
print(difference(n))
