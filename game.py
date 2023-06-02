from card_deck import Deck, AddCards, card_value
from war_game import war
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
                    end_game(self.player_one_choice.cards, self.player_two_choice.cards)
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


def end_game(player_one_cards, player_two_cards):
    if len(player_one_cards) > len(player_two_cards):
        print(
            "\n"
            + f"At this point of the game the winner is PLAYER 1 with {len(player_one_cards)} cards!"
        )
    elif len(player_two_cards) > len(player_one_cards):
        print(
            "\n"
            + f"At this point of the game the winner is PLAYER 2 with {len(player_two_cards)} cards!"
        )
    else:
        print("\n" + "At this point of the game IT'S A TIE!")


game = Game()
game.play()
