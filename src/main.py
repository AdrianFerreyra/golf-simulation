from src import logging

from src.model import Tournament
from src.printer import ConsolePrinter
from src.reader import FileReader
from src.simulation import SimulationManager

logger = logging.get_logger(__name__)


def main(players_stats_filepath, tournaments_count=10000):
    logger.info(
        f"Starting Monte Carlo Simulation for {tournaments_count} tournaments..."
    )

    printer = ConsolePrinter()
    csv_reader = FileReader(players_stats_filepath)
    players_stats = csv_reader.read()
    simulation_manager = SimulationManager(players_stats)

    logger.info("Playing tournaments...")
    for _ in range(tournaments_count):
        tournament = Tournament(players_stats)
        tournament.play()
        tournament_result = tournament.get_results()
        simulation_manager.update_results(tournament_result)

    simulation_results = simulation_manager.get_results()
    printer.print(simulation_results)

    logger.info("Finished simulation.")


if __name__ == "__main__":
    main(players_stats_filepath="ratings.txt")
