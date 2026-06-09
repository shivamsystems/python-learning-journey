# Ask user for a size N. Print a FULL diamond.
n = int(input("Size of Diamond: "))
for i in range(1,n+1):
    print("."*(n-i), end="")
    for j in range(i):
        print("*", end="",sep="")
    print("*"*(i-1),end="") #really, for getting logic of line 7 and line 4 it took me 1 hour, ohh!!
    print() #forgotten for new line to use -> print()
#first i didn't remember concepts of printing stars in this colomn
#but i did it one by one, like first printed 1st star then 2 then few wring code but fixed it self, and printed a colomn and a row
# then i got to understand how these lines works
#the full process was solving one single problem one by one and debug code self tried tested then finelly got the answer


for k in range(n-1, 0, -1): #finding this was also hard but i did it in 1.15 hr total
    print("."*(n-k), end="")
    for l in range(k):
        print("*", end = "")
    print("*"*(k-1),end="")
    print()