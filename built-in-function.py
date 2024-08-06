def print_docs(functions):
    for func in functions:
        print(f"{func.__name__} :")
        print(func.__doc__)
functions = [abs]
print_docs(functions)
