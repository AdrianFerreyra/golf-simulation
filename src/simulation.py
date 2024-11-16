from src.model import PlayerResult, PlayerStats, TournamentResult


class SimulationManager:
    def __init__(self, players_stats: list[PlayerStats]):
        self._results = {stats.player_name: PlayerResult() for stats in players_stats}
        self._updates_count = 0

    def calculate_fractional_places(
        self, start_pos: int, num_players: int, positions_available: int
    ):
        positions_overlap = max(0, (start_pos + num_players - 1) - start_pos + 1)
        positions_overlap = min(positions_overlap, positions_available)

        fraction = positions_overlap / num_players
        return fraction

    def update_results(self, tournament_results: TournamentResult):
        self._update_win_fraction(tournament_results)
        self._update_top_5_fraction(tournament_results)
        self._updates_count += 1

    def get_results(self):
        return {
            name: PlayerResult(
                player_win_fraction=result.player_win_fraction / self._updates_count,
                player_top_5_fraction=result.player_top_5_fraction
                / self._updates_count,
            )
            for name, result in self._results.items()
        }

    def _update_top_5_fraction(self, tournament_results):
        current_position = 1
        positions_remaining = 5

        for players in tournament_results.top_5_positions_players:
            fraction = self.calculate_fractional_places(
                current_position, len(players), positions_remaining
            )

            for player in players:
                self._results[player.player_name].player_top_5_fraction += fraction

            current_position += len(players)
            positions_remaining -= len(players)

    def _update_win_fraction(self, tournament_results):
        for first_position_player in tournament_results.first_position_players:
            self._results[
                first_position_player.player_name
            ].player_win_fraction += 1 / len(tournament_results.first_position_players)
