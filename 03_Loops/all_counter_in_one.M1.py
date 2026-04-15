# Write a program that:

sum_numbers = 0
count_numbers = 0
count_positive = 0
count_negative = 0
count_zero = 0

# 1. Asks user to enter 5 numbers (use for loop)

for i in range(5, 0, -1):
# 2. For each number:   

   n = int(input(f"Enter the number ({i}): "))
   if n:
      count_numbers += 1
# Track the TOTAL (sum)   

   sum_numbers += n
#  Track how many were POSITIVE

   if n > 0:
      count_positive += 1
# Track how many were NEGATIVE

   if n < 0:
      count_negative += 1
# Track how many were ZERO

   if n == 0:
      count_zero += 1
avarage = sum_numbers/5

# At the end, print:
# The sum
# Count of positives, negatives, zeros
#The average

print(f"The total zeros are: {count_zero}")
print(f"Sum of the numbers is {sum_numbers}")
print(f"The total negative numbers are: {count_negative}")
print(f"The total positive numbers are: {count_positive}")
print(f"The total avarage of numbers is: {avarage}")
