from card_deck import card_value


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
