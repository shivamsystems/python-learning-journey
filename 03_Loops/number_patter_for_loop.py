'''
for i in range(1,6):
    print(str(i)*i)
'''
n = int(input("Number: "))
for i in range(1, 5, +1):
    for j in range(i):
        print(f"{i}", end= "")
    print()
    