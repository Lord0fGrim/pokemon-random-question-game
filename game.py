##this is the questioning game
import random

question_bank = ["Pokemon is an abbreviation of Poketto Monsutā. What does this mean in Japanese? ",
                 "What is the name of the creator of Pokemon? ",
                 "How many cards have been sold by the Pokémon Trading Card Game? ",
                 "What type of Pokemon is Pikachu? ",
                 "What year was Pokemon created? ",
                 "What does Zubat not have? ",
                 "What is the English slogan for the franchise? ",
                 "How many animated theatrical Pokemon films have there been? ",
                 "Who is the main character in Pokemon? ",
                 "Who is the strongest Pokemon? "]
answer_bank = ["Pocket monsters",
                 "Satoshi Tajiri",
                 "43.2 billion",
                 "Electric",
                 "1996",
                 "Eyes",
                 "Gotta Catch Em All",
                 "23",
                 "Ash",
                 "Arceus"]

num_correct = 0

for x in range(10):

    random_number = random.randint(0,x)

    random_question = question_bank[random_number]
    correct_answer = answer_bank[random_number].upper()

    player_answer = input(random_question).upper()


    if player_answer == correct_answer:
        print("Correct!!")
        num_correct += 1
        print(num_correct)
    else:
        print("Dumbass!!")
        print(num_correct)

print("You got " + str(num_correct) + " question correct!")
print("You got " + str((num_correct / 10) * 100 ) + "%!")   








