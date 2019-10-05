import os
from deck import Deck
from time import sleep


class Game:
    def __init__(self):
        self.deck = Deck()
        self.round = 0
        self.tally = {
            "Player": 0,
            "Dealer": 0,
        }

    def score_hand(self, cards):
        score = 0
        num_aces = 0
        # Separate aces and non-aces
        for card in cards:
            if card.symbol == "A":
                num_aces += 1
            elif isinstance(card.symbol, str):
                score += 10
            else:
                score += card.symbol
        if num_aces == 0:
            return score
        # Up to one ace may count as 11 
        if score + 11 + (num_aces - 1) <= 21:
            score += 11
            num_aces -= 1
        # The rest of the aces must count as 1
        score += num_aces
        return score
    
    def print_screen(self):
        if os.name == "nt":
            os.system('cls')
        else:
            os.system('clear')
        print("*" * 10 + "    ROUND {}    ".format(self.round) + "*" * 10 + "\n")
        print("Scoreboard:")
        print("Player: {}".format(self.tally["Player"]))
        print("Dealer: {}\n".format(self.tally["Dealer"]))

    def print_hands(self, dealer_cards, player_cards):
        print("Dealer's hand:")
        dealer_card_strs = [repr(card).split("\n") for card in dealer_cards]
        for line in zip(*dealer_card_strs):
            print(*line)
        print()
        print("Your hand:")
        player_card_strs = [repr(card).split("\n") for card in player_cards]
        for line in zip(*player_card_strs):
            print(*line)

    def check_continue(self):
        resp = input("Play another round (Y/n)?\n")
        if resp.upper() != "Y":
            print("Have a nice day!")
            return exit()
        return True

    def play_round(self):
        self.deck.reset()
        self.round += 1
        self.print_screen()

        # Draw initial cards
        first_card = self.deck.draw_top()
        first_card.toggle_hidden()

        dealer_cards = [first_card, self.deck.draw_top()]
        player_cards = [self.deck.draw_top(), self.deck.draw_top()]

        dealer_score = self.score_hand(dealer_cards)
        player_score = self.score_hand(player_cards)

        # Show initial hands
        self.print_hands(dealer_cards, player_cards)

        # Player hits
        while player_score < 21:
            if len(player_cards) == 2:
                print("It's your turn to hit!")
                sleep(1.5)
            result = input("Would you like another card (Y/n)?\n")
            if result.upper() != "Y":
                break
            player_cards.append(self.deck.draw_top())
            sleep(0.5)
            self.print_screen()
            self.print_hands(dealer_cards, player_cards)
            player_score = self.score_hand(player_cards)

        # Check if player has busted or got a blackjack
        if player_score >= 21:
            if player_score == 21:
                print("Congratulations, you got a blackjack! You win!")
                self.tally["Player"] += 1
            else:
                print("Sorry, you've busted!")
                self.tally["Dealer"] += 1
            if self.check_continue():
                first_card.toggle_hidden()
                return self.play_round()
                

        # Dealer hits
        print("It's the dealer's turn to hit!")
        sleep(1.5)
        first_card.toggle_hidden()
        self.print_screen()
        self.print_hands(dealer_cards, player_cards)
        while dealer_score < 17:
            sleep(1.5)
            if len(dealer_cards) == 2:
                print("The dealer hits.")
            else:
                print("The dealer hits again.")
            sleep(1.5)
            dealer_cards.append(self.deck.draw_top())
            self.print_screen()
            self.print_hands(dealer_cards, player_cards)
            dealer_score = self.score_hand(dealer_cards)

        # Output result
        if dealer_score > 21:
            print("The dealer busted! You win!")
            self.tally["Player"] += 1
        elif player_score == dealer_score:
            print("It's a tie! Both you and the dealer scored {} points".format(player_score))
            self.tally["Player"] += 1
            self.tally["Dealer"] += 1
        elif player_score > dealer_score:
            print("Congratulations, you scored higher than the dealer! You win!")
            self.tally["Player"] += 1
        else:
            print("Sorry, the dealer scored more than you! You lose!")
            self.tally["Dealer"] += 1

        # Next round
        if self.check_continue():
            return self.play_round()
