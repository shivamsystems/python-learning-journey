word = input("Enter a word: ").lower().strip()
vowel_count = 0
for char in word:
    if char in "aeiou":
        vowel_count += 1 
print(f"Their are {vowel_count} vowels in '{word}' word")