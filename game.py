from card_deck import Deck, AddCards
import random


class Game:
    def __init__(self):
        self.deck = Deck()
        self.player_one_choice = AddCards(self.deck.player_one)
        self.player_two_choice = AddCards(self.deck.player_two)
        self.round_num = 0

    def play(self):
        print(
            "Hello to a WAR card game. LET'S START THE GAME! Player one starts the game!"
        )
        # print round number
        while len(self.player_one_choice) > 0 and len(self.player_two_choice) > 0:
            self.round_num += 1
            # check if it's time to ask the user if they want to finish the game
            if self.round_num > 1:
                game_end = input("Do you want to finish the game? ")
                if game_end.lower() == "yes":
                    if len(self.player_one_choice.cards) > len(
                        self.player_two_choice.cards
                    ):
                        print(
                            "\n"
                            + f"At this point of the game the winner is PLAYER 1 with {len(self.player_one_choice.cards)} cards!"
                        )
                        break
                    elif len(self.player_two_choice.cards) > len(
                        self.player_one_choice.cards
                    ):
                        print(
                            "\n"
                            + f"At this point of the game the winner is PLAYER 2 with {len(self.player_two_choice.cards)} cards!"
                        )
                        break
                    else:
                        print("\n" + "At this point of the game IT'S A TIE!")
                        break

            print("\n" + f"ROUND {self.round_num}")

            player_one_turn = players_card(self.player_one_choice.cards)
            player_two_turn = players_card(self.player_two_choice.cards)

            print(f"Player 1 opened {player_one_turn}")
            print(f"Player 2 opened {player_two_turn}")

            if card_value(player_one_turn) > card_value(player_two_turn):
                self.player_one_choice.add_cards([player_two_turn])
                self.player_two_choice.remove_one()
                print("Player 1 has bigger value cards and gets the cards!")
            elif card_value(player_two_turn) > card_value(player_one_turn):
                self.player_two_choice.add_cards([player_one_turn])
                self.player_one_choice.remove_one()
                print("Player 2 has bigger value cards and gets the cards!")
            else:
                war(self.player_one_choice, self.player_two_choice)

            # winner of the game
            if len(self.player_one_choice) == 0:
                print("PLAYER 2 WINS!")
                break
            elif len(self.player_two_choice) == 0:
                print("PLAYER 1 WINS!")
                break

            # print how many cards players have
            print(
                f"Player 1 has {len(self.player_one_choice.cards)} and Player 2 has {len(self.player_two_choice.cards)}"
            )


# random card of the deck
def players_card(deck_of_cards):
    return random.choice(deck_of_cards)


# card value form the class
def card_value(card):
    return card.value


# war game
def war(player_one_choice, player_two_choice):
    print("It's a tie! Time for WAR!")
    war_cards = []
    for i in range(2):
        # check if either player has run out of cards
        if len(player_one_choice.cards) == 0:
            return "Player Two wins!"
        elif len(player_two_choice.cards) == 0:
            return "Player One wins!"
        else:
            # In each iteration of the loop, this block of code removes one card from each player's deck (player_one_choice and player_two_choice) and adds them to the war_cards list.
            war_cards.append(player_one_choice.remove_one())
            war_cards.append(player_two_choice.remove_one())

    print(f"Player 1 opened {war_cards[0]}")
    print(f"Player 2 opened {war_cards[1]}")

    if card_value(war_cards[0]) > card_value(war_cards[1]):
        player_one_choice.add_cards(war_cards)
        print("Player 1 has bigger value and gets the cards!")
    elif card_value(war_cards[1]) > card_value(war_cards[0]):
        player_two_choice.add_cards(war_cards)
        print("Player 2 has bigger value and gets the cards!")
    else:
        return war()


game = Game()
game.play()
