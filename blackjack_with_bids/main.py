import os
import time
from art import logo
from termcolor import colored
import random

game_is_on = True

player_money = 800
dealer_money = 1600

while game_is_on == True:

    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_cards = []
    player_score = 0
    dealer_cards = []
    dealer_score = 0
    begin_game = False
    compare = True


    def clear(seconds=0):
        time.sleep(seconds)
        os.system('clear')


    def game_winner():
        global player_money, dealer_money
        if player_money <= 0:
            print("\nYou're out of money! 😭 Game over 😭")
        elif dealer_money <= 0:
            print("\nDealer is broke! You won the game! 😎😎😎")


    def bid_func():
        global bid, player_money, dealer_money
        if game_is_on == True and player_money > 0 and dealer_money > 0:
            print(f"Your total money is " + (colored(f"€{player_money}", "green")) + ".")
            print(f"Dealer's total money is " + (colored(f"€{dealer_money}", "yellow")) + ".")
            bid = int(input("How much do you want to bid in?: €"))
            if bid > player_money or bid > dealer_money:
                print("You can't place a bid greater than total money or the dealer's total money!\n")
                bid_func()
            elif bid <= 0:
                print("It seems that you don't have any money!\n")
                bid_func()
            else:
                player_money -= bid
                dealer_money -= bid
                print(f"\nYour bid is " + (colored(f"€{bid}", "cyan")) + "." + " Total bid is " + (
                    colored(f"€{bid * 2}", "blue")) + ".\n")
                # ${player_money}.", "green") + (colored(f" Dealer's pool is: ${dealer_money}.", "yellow") + f"Your bid is ${bid}. The total bid is ${bid * 2}.\n"))


    def ace_player():
        global player_score
        if player_score > 21 and 11 in player_cards:
            player_cards.remove(max(player_cards))
            player_cards.insert(0, 1)
            player_score -= 10


    def ace_dealer():
        global dealer_score
        if dealer_score > 21 and 11 in dealer_cards:
            dealer_cards.remove(max(dealer_cards))
            dealer_cards.insert(0, 1)
            dealer_score -= 10


    def want_to_play():
        global begin_game, compare, game_is_on
        if player_money <= 0 or dealer_money <= 0:
            compare = False
            game_is_on = False
        else:
            begin = input("Do you want to play a game of Blackjack?: Type 'y' or 'n': ")
            if begin == "y":
                clear()
                print(logo)
                begin_game = True
            else:
                compare = False
                game_is_on = False


    def draw_card_player(deck):
        global player_draw, player_score, begin_game, compare, dealer_money
        player_draw = random.choice(deck)
        player_cards.append(player_draw)
        player_score += player_draw
        ace_player()
        if player_score > 21:
            stats()
            final_hands()
            print("You went over. You lose 😭")
            dealer_money += (bid * 2)
            game_winner()
            begin_game = False
            compare = False


    def draw_card_dealer(deck):
        global dealer_draw, dealer_score, begin_game, compare, game_is_on, player_money
        if dealer_score < player_score:
            dealer_draw = random.choice(deck)
            dealer_cards.append(dealer_draw)
            dealer_score += dealer_draw
            ace_dealer()
        if dealer_score > 21:
            final_hands()
            print("Opponent went over. You win 😁")
            player_money += (bid * 2)
            game_winner()
            begin_game = False
            compare = False


    def stats():
        print(f"    Your cards: " + (colored(f"{player_cards}", "magenta")) + "." + " Your current score: " + (
            colored(f"{player_score}", "magenta")) + ".")
        print(f"    Computer's first card: " + (colored(f"{dealer_cards[0]}", "red")) + ".\n")


    def blackjack():
        global begin_game, compare, player_money
        if player_score == 21:
            final_hands()
            begin_game = False
            compare = False
            print("Win with a Blackjack 😎")
            player_money += (bid * 2)
            game_winner()


    def question_new_card():
        global draw_new, begin_game
        draw_new = input("Type 'y' to get another card, type 'n' to pass: ")
        if draw_new == "y":
            draw_card_player(deck)
        else:
            begin_game = False
            while dealer_score < player_score:
                draw_card_dealer(deck)


    def who_is_the_winner():
        global player_money, dealer_money
        if player_score > dealer_score:
            final_hands()
            print("You win 😃")
            player_money += (bid * 2)
        elif player_score < dealer_score:
            final_hands()
            print("You lose 😤")
            dealer_money += (bid * 2)
        else:
            final_hands()
            print("It's a draw! 🙃")
            dealer_money += bid
            player_money += bid


    def final_hands():
        print(f"\n    Your final hand: " + (colored(f"{player_cards}", "magenta")) + ", final score: " + (
            colored(f"{player_score}", "magenta")) + ".")
        print(f"\n    Dealer's final hand: " + (colored(f"{dealer_cards}", "red")) + ", final score: " + (
            colored(f"{dealer_score}", "red")) + ".")
        # print(f"    Computer's final hand: {dealer_cards}, final score: {dealer_score}")


    def initial_draw():
        global player_score, dealer_score
        for card in range(2):
            player_draw = random.choice(deck)
            player_cards.append(player_draw)
            player_score += player_cards[card]
            if player_score == 22:
                ace_player()
            dealer_draw = random.choice(deck)
            dealer_cards.append(dealer_draw)
            dealer_score += dealer_cards[card]


    #####################################################################################

    want_to_play()
    bid_func()
    initial_draw()

    if begin_game == True:
        stats()
        blackjack()

    while begin_game == True:
        question_new_card()
        if compare == True:
            stats()

    if compare == True and begin_game == False:
        who_is_the_winner()
        game_winner()

if game_is_on == True:
    want_to_play()
