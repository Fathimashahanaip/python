c=0
n=int(input("enter the number"))
while n>0:
    rem=n%10
    c=c+1
    n=int(n/10)
print(c)