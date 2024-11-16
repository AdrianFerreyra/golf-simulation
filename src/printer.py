from src.model import PlayerResult
from tabulate import tabulate


class ConsolePrinter:
    def print(self, tournament_results: dict[str, PlayerResult]):
        print("Printing results")
        print(
            tabulate(
                [
                    [name, result.player_win_fraction, result.player_top_5_fraction]
                    for name, result in tournament_results.items()
                ],
                headers=["Player Name", "Win Fraction", "Top 5 Fraction"],
            )
        )
