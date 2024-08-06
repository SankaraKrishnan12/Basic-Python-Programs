def AddIs(str):
    if str.startswith("Is"):
        return str
    else:
        return "Is "+str
str = input("Enter a string : ")
print(AddIs(str))