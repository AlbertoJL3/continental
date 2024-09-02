from typing import List, Dict
from app.models.player import Player
from app.models.card import Card
from app.models.deck import Deck

class GameModel:
    def __init__(self, num_players: int):
        self.players: List[Player] = [Player(f"Player {i+1}") for i in range(num_players)]
        self.current_player_index: int = 0
        self.deck: Deck = Deck()
        self.discard_pile: List[Card] = []
        self.round: int = 1
        self.game_state: str = 'initializing'  # Can be 'initializing', 'playing', 'roundEnd', 'gameEnd'

        self.start_new_round()

    def start_new_round(self):
        self.round += 1
        self.deck.shuffle()
        self.deal_cards()
        self.discard_pile = [self.deck.draw_card()]
        self.game_state = 'playing'

    def deal_cards(self):
        cards_per_player = 6 + self.round
        for player in self.players:
            player.hand = self.deck.draw_cards(cards_per_player)

    def draw_card(self, player_index: int, from_discard: bool = False):
        if self.current_player_index != player_index:
            raise ValueError('Not your turn')

        player = self.players[player_index]
        ## Add a way to prompt other users for permission. 
        if from_discard:
            player.add_card_to_hand(self.discard_pile.pop())
        else:
            player.add_card_to_hand(self.deck.draw_card())

    def play_card(self, player_index: int, card_index: int):
        if self.current_player_index != player_index:
            raise ValueError('Not your turn')

        player = self.players[player_index]
        card = player.remove_card_from_hand(card_index)
        self.discard_pile.append(card)

        self.check_for_round_end()
        self.next_turn()

    def check_for_round_end(self):
        current_player = self.players[self.current_player_index]
        if len(current_player.hand) == 0:
            self.game_state = 'roundEnd'
            self.calculate_scores()

    def calculate_scores(self):
        for player in self.players:
            player.score += sum(card.get_point_value() for card in player.hand)

    def next_turn(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def get_game_state(self) -> Dict:
        return {
            'players': [player.get_state() for player in self.players],
            'current_player_index': self.current_player_index,
            'discard_pile_top': str(self.discard_pile[-1]) if self.discard_pile else None,
            'round': self.round,
            'game_state': self.game_state
        }
