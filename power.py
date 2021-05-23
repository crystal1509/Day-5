#Calculate power of a number using a while loop


num=int(input("enter a number:"))
exp=int(input("enter its exponent:"))
res=1
while(exp!=0):
    res=res*num
    exp=exp-1

print("its power is:",res)
