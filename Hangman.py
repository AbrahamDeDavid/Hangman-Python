import os
import random
from unidecode import unidecode

def choice_words():
    with open ("./words.txt", "r", encoding="utf-8") as f:
        words = [word.strip() for word in f]
    word = random.choice(words)
    return word.lower()

def play_game(word, hidden_word, used_letters):
    print(" ".join(hidden_word))
    user_letter = input("Ingresa una letra: ")

    if user_letter in used_letters:
        print("Ya se ha utilizado esta palabra antes, intenta con otra")
        return True

    if not user_letter.isalpha():
        print("Solo puedes ingresar letras")
        return True
    used_letters.add(user_letter)

    match_found = False
    position_counter = -1
    for letter in word:
        position_counter += 1
        if user_letter == letter:
            hidden_word[position_counter] = user_letter
            match_found = True

    k_continue = True
    if "".join(hidden_word) == word:
        print("¡Ganastes!" + "\n" + "la palabra era: " + word)
        k_continue = "Break"
        return k_continue

    if match_found:
        return True

    os.system("cls")

    return False
def run():
    word = unidecode(choice_words())
    print(word)
    hidden_word = ["_" for letter in word]
    used_letters = set()

    attemps = 7 if len(word) < 10 else 15

    while attemps > 0:
        lifes = ["❤" for attemp in range(1, attemps + 1)]
        print(" ".join(lifes))
        playing = play_game(word, hidden_word, used_letters)
        if not playing:
            attemps -= 1
        if playing == "Break":
            break

    if attemps == 0:
        print("Perdistes, la palabra era: " + word)



if __name__ == "__main__":
    run()
