a=int(input("Enter the number : "))
fact = 1
def factorial(n):
    if n<1:
        return 1
    return n*factorial(n-1)
print(factorial(a))
    
