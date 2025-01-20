import collections
from random import choice

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    """
    A class representing a standard French deck of cards.
    """

    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "clubs diamonds hearts spades".split()

    def __init__(self) -> None:
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self) -> None:
        return len(self._cards)

    def __getitem__(self, position) -> None:
        return self._cards[position]

    def __repr__(self) -> str:
        return f"Cards: ({self.ranks}), Suits: ({self.suits})"

    def get_cards(self):
        """
        Returns the cards in the deck.
        """
        return self._cards


beerCard = Card("7", "diamonds")
print(beerCard)
print(beerCard._asdict())
golfClub = Card("9", "iron")
print(golfClub)
deckOfCards = FrenchDeck()
print(len(deckOfCards))
print(deckOfCards[0])
print(deckOfCards[-1])
print("Using Choice from Random")
print(choice(deckOfCards))
print(choice(deckOfCards))
print(choice(deckOfCards))
print("Using slicing like deckOfCards[:3]")
print(deckOfCards[:3])
print(deckOfCards[12::13])
print("Does a golf club 9 iron exist in the card deck?")
print(golfClub in deckOfCards)
print(beerCard in deckOfCards)
print(deckOfCards)
