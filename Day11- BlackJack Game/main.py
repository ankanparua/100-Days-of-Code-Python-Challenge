import art
import random
print(art.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


new_game = True

while new_game:
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play.lower() == "y":
        your_cards = []
        bot_cards = []
        your_score = 0
        bot_score = 0
        play_again = True

        #1st Draw
        for i in range(2):
            your_cards.append(random.choice(cards))
        bot_cards.append(random.choice(cards))
        your_score = sum(your_cards)
        bot_score = sum(bot_cards)
        print(f"Your cards: {your_cards}, current score: {your_score}")
        print(f"Computer's first card: {bot_cards[0]}")
        if your_score == 21:
            print("You win with a blackjack!")
            play_again = False

        while play_again:
            #Next Draw
            hit_or_pass = input("Type 'y' to get another card, type 'n' to pass: ")
            if hit_or_pass == "y":
                your_cards.append(random.choice(cards))
                your_score = sum(your_cards)
                print(f"    Your cards: {your_cards}, current score: {your_score}")
                print(f"    Computer's first card: [{bot_cards[0]}]")
                if your_score < 21:
                    continue
                elif your_score == 21:
                    print("You Win!")
                    play_again = False
                else:
                    if 11 in your_cards:
                        your_cards[your_cards.index(11)] = 1
                        your_score = sum(your_cards)
                        print(f"    Your cards: {your_cards}, current score: {your_score}")
                        continue
                    else:
                        print(f"    Your final hand: {your_cards}, final score: {your_score}")
                        print(f"    Computer's final hand: [{bot_cards[0]}], final score: {bot_cards[0]} ")
                        print("You went over. You lose 😭")
                        play_again = False
            elif hit_or_pass == "n":
                bot_cards.append(random.choice(cards)) #5
                bot_score = sum(bot_cards) #15

                if bot_score == 21: #false
                    print("Lose, opponent has Blackjack 😱")
                    play_again = False
                else:
                    flag = True
                    message = ""
                    while flag:
                        if bot_score > 21:
                            if 11 in bot_cards:
                                bot_cards[bot_cards.index(11)] = 1
                                continue
                            else:
                                message = "Opponent went over. You win 😁"
                                flag = False
                                play_again = False
                                break
                        else:
                            if bot_score < your_score:
                                bot_cards.append(random.choice(cards))
                                bot_score = sum(bot_cards)
                            elif bot_score == your_score:
                                message = "Draw!"
                                flag = False
                                play_again = False
                                break
                            else:
                                message = "You lose 😤"
                                play_again = False
                                flag = False

                print(f"    Your final hand: {your_cards}, final score: {your_score}")
                print(f"    Computer's final hand: {bot_cards}, final score: {bot_score} ")
                print(message)
    else:
        new_game = False