#Write a program that:

# 1. Has a secret word (hardcode it, e.g., "python")
secret_word = "garden"
attempt_count = 0
letter_match_count = 0
for i in range(6):
   guess = input("Guess a word of 6 letters: ").lower().strip()  
   if guess:
      attempt_count += 1
   """if i in "garden": #i forgot this again i was using here guess
      letter_match_count += 1# i did a mistake here, if i was an int then how it can check through tring
      """
   for j in guess: # I don't know its a correct approach or not but it worked
      if j in secret_word:
         letter_match_count += 1

   if guess == secret_word:
      print(f"You Win in {attempt_count} attempts")
      break    
   else:
      print(f"Wrong guess! {letter_match_count} letter matched,{6-attempt_count} tries left")
else:
   print("Game Over! Word was: Garden")
