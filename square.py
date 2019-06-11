#function start
def magic(a):
    s=(a**3+a)/2 # constant value for a magic square
    return s
#function end

#main
n= int(input("Enter order"))
y= magic(n)   # constant sum of the square

r=[int(x)for x in input("Enter the elements").split()] # to have multiple inputs

#to print the elements of the list
for i in range (0,n**2,n):    # from zero till n squared -1 in intervals of n
    for j in range (i,i+n,1):  # from i till i+n-1 in intervals of 1
        print("%d"%r[j])
    print("\n")
#printing of elements of list over

# sum of rows
s=0  #initializing sum as zero
flag=1
for i in range (0,n**2,n):
    for j in range (i,i+n,1):
                s+=r[j]
    if(s!=y):
       flag=0
    break
s=0

#sum of columns
i=0
j=0
s=0
if (flag==1):
    for i in range (n):
        for j in range (i,n**2+i,n):
            s+=r[j]
        if(s!=y):
            flag=0
        break
s=0

#diagonals
if(flag==1):
    for i in range(0, n**2, n + 1):
        s = s + r[i]
    if (s != y):
        flag = 0
    s = 0
    for j in range(n - 1, n**2 - 1, n - 1):
        s = s + r[j]
    if (s != y):
        flag  = 0
        # final result
if (flag == 0):
    print("It is not magic square")
else:
    print("It is magic square")