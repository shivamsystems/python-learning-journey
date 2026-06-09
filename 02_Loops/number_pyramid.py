#Ask user for N. Print this EXACT pattern.


n = 5

for i in range(1, n+1):
    print(i)
    
    for j in range(1,i+1):
        j = j + ()
        print(f"{j}", end="")

    print() #i forgotted this print() for new line, when i ran the code then realized, because i did m1, m2, in evening and doind m3, m4 in morning


'''''
Input: N = 5
Output:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
Rules:
- Numbers are CONTINUOUS (1, 2, 3, 4... not restarting each row)
- Row 1 has 1 number
- Row 2 has 2 numbers
- Row 3 has 3 numbers
- Row i has i numbers
'''''