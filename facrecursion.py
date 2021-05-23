#Python Program to Find Factorial of Number Using Recursion

def fac_recursion(n):
    if n==1:
        return n
    else:
        return n*fac_recursion(n-1)


num=int(input("enter a number:"))
if num<0:
    print("negative number!!! enter again")
else:
    print("factorial is:",fac_recursion(num))
