import random
import logo
import word

print(logo.logo)

word_list = word.word_list
stages = logo.stages
chosen_word = random.choice(word_list)
lives = 6

display = []
l  = len(chosen_word)
for i in range(0, l):
    display.append('_')


cnt = 0
while cnt < l and lives != 0:
    guess = input("Guess a letter: ").lower()
    for p in range(l):
        letter = chosen_word[p]
        if letter == guess:
            display[p] = letter

    if guess not in chosen_word :
        lives -= 1
        print(stages[lives])


    if "_" in display and lives != 0:
        print(display)
        continue
    elif "_" in display and lives == 0:
        print(stages[lives])
        print("You are Hanged till death")
    else :
        print(f"you won {display}")
        break
    cnt += 1


