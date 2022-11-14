from typing import List
from collections import namedtuple
from random import randint, choice

# Card = namedtuple("Card", ["suit", "rank"])
class Card:
    
    def __init__(self, suit:str, rank:str) -> None:
        self.suit = suit
        self.rank = rank
    
    def __repr__(self) -> str:
        return f"<{self.suit[0].upper()},{self.rank}>"

    def prettify(self) -> str:
        if self.rank == '' and self.suit == '':
            pretty_card = [
            """┌─────────┐""",
            """│░░░░░░░░░│""",
            """│░░░░░░░░░│""",
            """│░░░░░░░░░│""",
            """│░░░░░░░░░│""",
            """│░░░░░░░░░│""",
            """│░░░░░░░░░│""",
            """│░░░░░░░░░│""",        
            """└─────────┘"""
            ]
        else:
            suit_symbols = {'S':'♠', 'D':'♦', 'H':'♥', 'C':'♣'}
            pretty_card = []
            space = '' if self.rank == '10' else ' '
            pretty_card.append('┌─────────┐')
            pretty_card.append('│{}{}       │'.format(self.rank, space))  # use two {} one for char, one for space or char
            pretty_card.append('│         │')
            pretty_card.append('│         │')
            pretty_card.append('│    {}    │'.format(suit_symbols[self.suit]))
            pretty_card.append('│         │')
            pretty_card.append('│         │')
            pretty_card.append('│       {}{}│'.format(space, self.rank))
            pretty_card.append('└─────────┘')
        return "\n".join(pretty_card)

class CardDeck:
    
    def __init__(self) -> None:
        self.cards: List[Card] = []        
        for suit in ['H','S','C','D']:
            for rank in ['A'] + list(map(str, range(2,11))) + ['J','Q','K']:
                self.cards.append(Card(suit, rank))

        self.shuffled:bool = False
    
    def __str__(self) -> str:
        return f"A {'non-shuffled' if not self.shuffled else 'shuffled'} deck of {len(self.cards)} cards"
    
    def __repr__(self) -> str:
        # return f"{len(self.cards)} {'non-shuffled' if not self.shuffled else 'shuffled'} cards:\n" +  "\n".join([str(card) for card in self.cards])
        repr_str =  f"{len(self.cards)} {'non-shuffled' if not self.shuffled else 'shuffled'} cards:\n" 
        for i in range(0, len(self.cards), 13):
            _ = " ".join([str(card) for card in self.cards[i: i+13]])
            repr_str = "\n".join([repr_str, _])
        return repr_str

    def shuffle(self, n=10):
        for _ in range(n):
            n1 = randint(0, len(self.cards))
            n2 = randint(n1, len(self.cards))
            top, middle, bottom = self.cards[: n1], self.cards[n1: n2], self.cards[n2:]
            # print(f"{0, n1, n2}")
            self.cards = top + bottom + middle
        self.shuffled = True

    def cut(self):
        n = randint(0, len(self.cards))
        top, bottom = self.cards[0:n], self.cards[n:]
        self.cards = bottom + top
        self.shuffled = True

    def reset(self):
        self.__init__()

    # 'Overloading' methods
    def __getitem__(self, i):
        # indexed access and slicing
        return self.cards[i]

    def __len__(self):
        return len(self.cards)

    def __iter__(self):
        i = 0
        while True:
            if i >= len(self.cards):
                raise StopIteration()
            yield self.cards[i]
            i += 1

def prettify(cards):
    cards = [card.prettify() for card in cards]
    cards = [card.split("\n") for card in cards]
    prettify_cards = []
    for l in zip(*cards):
        prettify_cards.append(" ".join(l))
    return "\n".join(prettify_cards)

if __name__=="__main__":
    # Basic tests
    deck = CardDeck()
    print(deck)
    print(repr(deck))

    deck.shuffle(n=50)
    deck.cut()
    print(deck)
    print(repr(deck))
    
    print(deck[0])
    print(deck[:5])

    print(choice(deck).prettify())
    counter = 7
    deck_iter = iter(deck)
    cards = []
    for card in deck_iter:
        cards.append(card)
        counter -= 1
        if not counter: break
    print(prettify(cards))