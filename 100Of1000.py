def near(n):
    return ((abs(1000-n)<=100) or (abs(2000-n)<=100))
n = int(input("Enter the number : "))
print(near(n))