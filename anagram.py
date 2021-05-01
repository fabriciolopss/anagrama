import os
import random
import time
score = 0
rounds = 0
def gameLoop(gameStatus):
    global score
    global rounds
    reader = open("7776palavras.txt", encoding="utf8").read().splitlines()
    while gameStatus:
        randomword = random.choice(reader)
        anagram = list(randomword)
        random.shuffle(anagram)
        resultword = "".join(anagram)
        print(randomword)
        tentativa = str(input("O anagrama é {}, qual o seu palpite?".format(resultword)))
        if str(randomword) == tentativa:
            score += 1
            rounds += 1
            print("Parabéns você acertou!")
            drawTabela(score,rounds)
        elif str(randomword) != tentativa:
            rounds += 1
            print("Você errou!")
            drawTabela(score, rounds)
            
def drawTabela(pontuação,rounds):
    time.sleep(2)
    os.system("cls")
    porcentagem = (pontuação/rounds) * 100
    print("Numero de acertos: {}, aproveitamento {:.1f}%".format(pontuação,porcentagem))
    


gameLoop(True)