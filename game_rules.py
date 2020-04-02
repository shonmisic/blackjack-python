from deck import Deck
from cards.card import Card
from cards.card_rank import CardRank
from cards.card_suit import CardSuit
from players.dealer import Dealer


class GameRules():

    _card_max_value = 10
    _ace_max_value = 11
    _minimum_cards_in_hand = 2
    _winning_value = 21
    _minimum_budget = 100

    def __init__(self):
        card_rank_values = self._init_card_rank_values()
        cards = self._init_cards(card_rank_values)
        self.deck = Deck(cards)

    def _init_card_rank_values(self):
        rank_values = {rank: [rank.value] if rank.value <
                       CardRank.JACK.value else [self._card_max_value] for rank in CardRank}

        ace_card_values = [values for rank,
                           values in rank_values.items() if rank == CardRank.ACE]
        for values in ace_card_values:
            values.append(self._ace_max_value)

        return rank_values

    def _init_cards(self, card_rank_values):
        cards = []

        for suit in CardSuit:
            for rank, values in card_rank_values.items():
                card = Card(suit, rank, values)
                cards.append(card)

        return cards

    def get_playing_deck(self):
        return self.deck

    def get_minimum_budget(self):
        return self._minimum_budget

    def valid_initial_hand(self, hand):
        return len(hand.get_cards()) == self._minimum_cards_in_hand

    def card_face_down_check(self, participant):
        return isinstance(participant, Dealer) and not participant.get_hand().get_cards()

    def valid_value(self, value):
        return value <= self._winning_value
