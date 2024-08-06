n = int(input("Enter number = "))
sum=0
m=n
terms = int(input("Enter how many number of terms? "))
for i in range (1,terms+1):
   sum+=m
   print(m)
   m+=n*(10**i)
print("the sum is : ",sum)
