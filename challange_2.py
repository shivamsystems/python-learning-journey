#Simple quiz game
#Ask 3 questions
q1 = input("Does earth rotates arrount the sun (Yes/No): ").lower().strip()
q2 = int(input("How many days in a year: "))
q3 = float(input("Value of PIE (Including 3 values after decimal): "))

#Track score
if q1 == "yes":
    score_q1 = 10
else:
    score_q1 = 0
    
if q2 == 365:
    score_q2 = 10
else:
    score_q2 = 0
    
if q3 == 3.141:
    score_q3 = 10
else:
    score_q3 = 0
    
#Print final score and grade at end
score = score_q1 + score_q2 + score_q3
print(f"Your final score is {score}")
