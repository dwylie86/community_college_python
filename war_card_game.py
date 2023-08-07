import random  # For card shuffling


class Card:
    """
        This class create a generic card to be used in a card game.
    """

    def __init__(self, rank, suit_index):
        """
        Initializes the rank and suit index
        :param rank: the numerical value of the card
        :param suit_index: the numerical value of the card's suit
        """
        self.rank = rank
        self.suit_index = suit_index

    def card_suit(self):
        """
        Assigns the suit index a string descriptor for the card
        :return: a string descriptor of the suit index
        """
        suits = ["Clubs", "Hearts", "Diamonds", "Spades"]
        return suits[self.suit_index - 1]

    def card_name(self):
        """
        Assigns the rank a string descriptor for the card
        :return: a string descriptor to of the card's rank
        """
        names = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
                 "Ten", "Jack", "Queen", "King", "Ace"]
        return names[self.rank - 2]

    def display_card(self):
        """
        Creates a string descriptor for the rank and suit of a card
        :return: a string descriptor for the rank and suit of a card
        """
        return f"{self.card_name()} of {self.card_suit()}"

    #  Comparative dunder functions for use in card games. Allows card objects to be compared by rank
    def __gt__(self, other):
        return self.rank > other.rank

    def __lt__(self, other):
        return self.rank < other.rank

    def __eq__(self, other):
        return self.rank == other.rank

    # String Method
    def __str__(self):
        return f"Name: {self.card_name()} Suit: {self.card_suit()} Rank: {self.rank} Suit Index: {self.suit_index}"


class Deck:
    """
    This class creates a deck of card objects to be used in a card game
    """

    def __init__(self):
        """
        Initializes the deck, adds cards, and then shuffles
        """
        self.deck = []
        self.create_deck()
        self.shuffle_deck()

    def create_deck(self):
        """
        This creates 52 standard cards from 2 to ace in each suit for a deck.
        :return: a deck of cards
        """
        for rank in range(2, 15):
            for suit in range(1, 5):
                card = Card(rank, suit)
                self.deck.append(card)

    def shuffle_deck(self):
        """
        Shuffles the deck of cards
        """
        random.shuffle(self.deck)

    def draw_from_top(self):
        """
        For use in games that draw cards from the top of the deck.
        """
        return self.deck.pop()

    def draw_from_bottom(self):
        """
        For use in games that draw cards from the bottom of the deck.
        """
        return self.deck.pop(0)

    def __len__(self):
        """
        Length dunder to return number of objects in a deck
        """
        return len(self.deck)

    def __iter__(self):
        """
        Iteration dunder to allow us to loop through deck objects
        """
        return iter(self.deck)

    # String Method
    def __str__(self):
        deck_str = "\n".join(str(card.display_card()) for card in self.deck)
        deck_size = len(self.deck)
        return f"Deck:\n{deck_str}\nDeck contains: {deck_size} cards"


class War:
    """
    This class simulates a game of War
    """

    def __init__(self):
        """
        Initializations:
        deck()-- Gets a deck of cards
        pone_deck, ptwo_deck-- The player's deck (half of deck)
        pone_bounty, ptwo_bounty-- The bounty of cards collected for War (tied round)
        split_deck()-- Splits the deck into the two players' decks
        war_count-- keeps a tab of consecutive tied rounds in the unlike event of infinite tied rounds
        pause-- allows the user to pause after each round or simulate the entire game.
        game_over-- A flag for when the game ends due to an index error from drawing cards
        """
        self.deck = Deck()
        self.pone_deck = []
        self.ptwo_deck = []
        self.pone_bounty = []
        self.ptwo_bounty = []
        self.split_deck()
        self.war_count = 0
        self.pause = True
        self.game_over = False

    def split_deck(self):
        """
        Splits the deck into the two players' decks
        :return: pone_deck and ptwo_deck
        """
        while len(self.deck) > 0:
            self.pone_deck.append(self.deck.draw_from_top())
            if len(self.deck) > 0:
                self.ptwo_deck.append(self.deck.draw_from_top())

    def round_win(self, winner_deck, winner_bounty, loser_bounty):
        """
        Handles the actions to take when a player wins a round.
        Adds the bounty cards to the winner's deck, and shuffles the deck.
        Clears both players' bounties.
        """
        winner_deck.extend(loser_bounty)
        winner_deck.extend(winner_bounty)
        random.shuffle(winner_deck)
        winner_bounty.clear()
        loser_bounty.clear()
        if self.pause:
            self.round_pause()

    def play_round(self):
        """
           Generates a round of War. High card wins, tie leads to resolve_war function
           :return: won cards to the winning player's deck
        """
        try:
            pone_hand = self.pone_deck.pop(0)
            ptwo_hand = self.ptwo_deck.pop(0)
        except IndexError:
            self.end_game()
            self.game_over = True
            return
        print(f"P1 Card: {pone_hand.display_card()}")
        print(f"P2 Card: {ptwo_hand.display_card()}")
        self.pone_bounty.append(pone_hand)
        self.ptwo_bounty.append(ptwo_hand)

        if pone_hand > ptwo_hand:
            print("P1 Wins the Round")
            self.round_win(self.pone_deck, self.pone_bounty, self.ptwo_bounty)
        elif ptwo_hand > pone_hand:
            print("P2 Wins the Round")
            self.round_win(self.ptwo_deck, self.ptwo_bounty, self.pone_bounty)
        else:
            self.resolve_war()

    def resolve_war(self):
        """
           This is what happens when a round ties. Players ante up three cards to be won in a tie-breaker round.
           winner gets all cards played and in bounty
        """
        print("War!")
        if len(self.pone_deck) < 4 or len(self.ptwo_deck) < 4:
            self.end_game()
            self.game_over = True
            return
        for _ in range(3):
            self.pone_bounty.append(self.pone_deck.pop(0))
            self.ptwo_bounty.append(self.ptwo_deck.pop(0))
        pone_war_card = self.pone_deck.pop(0)
        ptwo_war_card = self.ptwo_deck.pop(0)
        print(f"P1 War Card: {pone_war_card.display_card()}")
        print(f"P2 War Card: {ptwo_war_card.display_card()}")
        self.pone_bounty.append(pone_war_card)
        self.ptwo_bounty.append(ptwo_war_card)
        if pone_war_card > ptwo_war_card:
            print("P1 Wins the War!")
            self.round_win(self.pone_deck, self.pone_bounty, self.ptwo_bounty)
            if len(self.ptwo_deck) == 0:
                self.game_over = True
                self.end_game()
        elif ptwo_war_card > pone_war_card:
            print("P2 Wins the War!")
            self.round_win(self.ptwo_deck, self.ptwo_bounty, self.pone_bounty)
            if len(self.pone_deck) == 0:
                self.game_over = True
                self.end_game()
        else:
            print("Another WAR!")
            self.resolve_war()

    def round_pause(self):
        # Print the options for the user
        print("Press 'n' for next round - 'score' for current score - 'sim' to simulate the rest of the game")

        # Get the user's choice
        choice = input().lower()

        # Perform the appropriate action based on the user's choice
        if choice == 'score':
            print(f"""Player 1's Total Cards: {len(self.pone_deck)}
Player 2's Total Cards: {len(self.ptwo_deck)}            
""")
            # print the current score
            return self.round_pause()
        elif choice == 'sim':
            # simulate the rest of the game
            self.pause = False
        else:
            return choice

    def play_game(self):
        """
        Plays rounds until win condition is met (No cards in a players deck)
        """
        while len(self.pone_deck) > 0 and len(self.ptwo_deck) > 0:
            self.play_round()
        if not self.game_over:
            self.end_game()

    def end_game(self):
        """
        Game ends when a player cannot draw a card
        """
        if len(self.pone_deck) == 0:
            print("Player 2 wins the game! Player 1 ran out of cards.")
        else:  # len(self.ptwo_deck) == 0
            print("Player 1 wins the game! Player 2 ran out of cards.")

    def __len__(self):
        """
        Returns the total number of cards left in the game.
        """
        return len(self.pone_deck) + len(self.ptwo_deck)

    # String Method
    def __str__(self):
        pone_deck_str = ", ".join(card.display_card() for card in self.pone_deck)
        pone_deck_size = len(self.pone_deck)
        ptwo_deck_str = ", ".join(card.display_card() for card in self.ptwo_deck)
        ptwo_deck_size = len(self.ptwo_deck)
        pone_bounty_str = ", ".join(card.display_card() for card in self.pone_bounty)
        pone_bounty_size = len(self.pone_bounty)
        ptwo_bounty_str = ", ".join(card.display_card() for card in self.ptwo_bounty)
        ptwo_bounty_size = len(self.ptwo_bounty)

        return f"""P1 Deck:\n{pone_deck_str}\nDeck contains: {pone_deck_size} cards
P2 Deck:\n{ptwo_deck_str}\nDeck contains: {ptwo_deck_size} cards

P1 Bounty: {pone_bounty_str} (Bounty size: {pone_bounty_size})
P2 Bounty: {ptwo_bounty_str} (Bounty size: {ptwo_bounty_size})
        """


# Simulates a game of War
war = War()
war.play_game()
