#Count Number of Digits in an Integer using while loop


def count1(n):
    c=0
    while (n!=0):
        n=n//10
        c=c+1
    return c
  
num=int(input("enter an integer:"))
print("no of digits in it are:",count1(num))
