a = [1,2,4,6,8,99,3,11,45,65,2,0]

Len=len(a)
print( "length of list is", Len)

#print all the elements less than 5
x=[]
for i in range(0,Len):
    if(a[i]<5):
        x.append(a[i])
        i=i+1
    else:
        i=i+1
print(x) 
