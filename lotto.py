import random
from colorama import Fore, Back, Style

roll_num = 100000

def roll():
    random.seed()    
    return random.sample(range(1, 49), 6)
    
def simulate():
    game = roll()
    player = roll()
    x = 0
    for num in game:
        for guess in player:
            if num == guess:
                x += 1
    return x

def simulation(amount):
    print(Fore.RED)
    print(f"\n-------------- Neues Spiel mit {roll_num} Versuchen ------------\n")
    print(Fore.GREEN + "Simuliert....\n")
    results = [0,0,0,0,0,0,0]
    for i in range(amount):
        results[simulate()] += 1
    print(Fore.GREEN + "Ergebnisse: \n")
    for i in range(len(results)):
        prob = results[i] / roll_num * 100
        print(f"{i} Richtig: {round(prob,2)}% | {results[i]} mal von {roll_num} Versuchen")
    print(Fore.RED + "\n--------------------------------------------------------------\n")

simulation(roll_num)





    