
word = input("Enter a word: ")
consonant = ""
for char in word:
    if char in "aeiou":
        continue
    consonant += char
    
print(f"Consonant: {consonant}",sep="", end="")