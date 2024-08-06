def CopyString(string,n):
    return (string+"\n")*n
string = input("Enter The string : ")
n = int(input("Enetr How many times : "))
print(CopyString(string,n))