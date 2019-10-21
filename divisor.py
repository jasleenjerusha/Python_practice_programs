Num = int(input("Enter any number:"))

for i in range(1,Num+1):
    if(Num%i == 0):
        print(i,"is a divisor of",Num)
        i=i+1
    else:
        i=i+1
