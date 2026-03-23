word = input("Word: ").lower()
letter = input("Letter to count: ").lower()
count = 0
for character in word:
    if character == letter:
        count +=1 
print(f"{letter} appeared {count} rimes in {word}")
    
