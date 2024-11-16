from collections import defaultdict
from dataclasses import dataclass
import heapq
import random


@dataclass
class PlayerResult:
    def __init__(self, player_win_fraction=0, player_top_5_fraction=0):
        self.player_win_fraction = player_win_fraction
        self.player_top_5_fraction = player_top_5_fraction


@dataclass
class PlayerStats:
    def __init__(self, name, mean, sigma):
        self.player_name = name
        self.player_mean = mean
        self.player_std_dev = sigma


def calculate_round_result(player_stats: PlayerStats) -> float:
    return random.normalvariate(player_stats.player_mean, player_stats.player_std_dev)


@dataclass
class TournamentResult:
    def __init__(
        self,
        first_position_players: list[PlayerStats],
        top_5_positions_players: list[list[PlayerStats]],
    ):
        self.first_position_players = first_position_players
        self.top_5_positions_players = top_5_positions_players


class Tournament:
    def __init__(self, players_stats: list[PlayerStats]):
        self._players_stats = players_stats
        self._points_heap = []
        heapq.heapify(self._points_heap)
        self._points_to_players = defaultdict(list[PlayerStats])

    def play(self):
        for player_stats in self._players_stats:
            player_result = 0
            for _ in range(1, 5):
                round_result = calculate_round_result(player_stats)
                player_result += round_result
            if player_result not in self._points_heap:
                heapq.heappush(self._points_heap, player_result)
            self._points_to_players[player_result].append(player_stats)

    def _get_first_position_players(self) -> list[PlayerStats]:
        min_score = self._points_heap[0]
        players_for_min_score = self._points_to_players[min_score]
        return players_for_min_score

    def _get_5_positions_players(self) -> list[list[PlayerStats]]:
        players_for_smallest_5 = []

        for i in range(0, 4):
            if len(players_for_smallest_5) >= 5:
                break
            points_in_pos_i = self._points_heap[i]
            players_in_pos_i = self._points_to_players[points_in_pos_i]
            players_for_smallest_5.append(players_in_pos_i)

        return players_for_smallest_5

    def get_results(self) -> TournamentResult:
        _first_position_players = self._get_first_position_players()
        _top_5_positions_players = self._get_5_positions_players()
        return TournamentResult(
            first_position_players=_first_position_players,
            top_5_positions_players=_top_5_positions_players,
        )
