rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
game_pic = [rock, paper, scissors]
rand_num = random.randint(0,2)
my_turn = int(input("Enter your turn\n1. Rock\n2. Paper\n3. Scissors\n: ")) - 1

print(game_pic[rand_num])
print(game_pic[my_turn])

if my_turn == rand_num:
    print("TIE!")
elif((rand_num == 0 and my_turn == 1) or (rand_num == 1 and my_turn == 2) or (rand_num == 2 and my_turn == 0)):
    print("YOU WIN!")
else:
    print("YOU LOSE!")
