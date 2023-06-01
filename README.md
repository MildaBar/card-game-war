# card-game-war

Card game "War" written in Python using OOP paradigm.

INTRODUCTION. Game rules:
The goal is to be the first player to win all 52 cards.

The deck is divided evenly among the players, giving each a down stack. In unison, each player reveals the top card of their deck—this is a "battle"—and the player with the higher card takes both of the cards played and moves them to their stack.

If the two cards played are of equal value, then there is a "war". Both players place the next card from their pile face down and then another card face-up. The owner of the higher face-up card wins the war and adds all the cards on the table to the bottom of their deck. If the face-up cards are again equal then the battle repeats with another set of face-down/up cards. This repeats until one player's face-up card is higher than their opponent's.

If a player runs out of cards during a war, that player immediately loses.

REQUIREMENTS OF THE PROGRAM:

1. There should be two players participating the game.
2. The deck needs to be randomly initialized at the beggining of each game. Each player gets 26 cards.
3. Each player should "open" and "show" a card.
4. After each round, the program should update how many cards each player has.
5. The program should compare cards and act on what it shows:
   - if the cards are the same, start a "war"
   - if the cards are different, check whitch player has the higher card and gets the cards
6. The program should count the cards:
   - if on of the players has all cards, that player wins
   - if on of the player has no cards while playing "war", that player immediately loses.
7. If players wants to quit the program in the middle of the game, one of the player should write "done".
