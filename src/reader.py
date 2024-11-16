import csv
from src import logging
from src.model import PlayerStats

logger = logging.get_logger(__name__)


class FileReader:
    def __init__(self, filepath):
        self._filepath = filepath

    def read(self) -> list[PlayerStats]:
        logger.info(f"Reading file {self._filepath}...")
        with open(self._filepath, "r", encoding="utf-8") as file:
            csv_reader = csv.reader(file, delimiter="\t")

            player_stats = []
            for i, row in enumerate(csv_reader):
                if i == 0:
                    continue
                name: str = row[0]
                mean: str = row[1]
                sigma: str = row[2]

                processed_name = name.strip()
                processed_mean = float(mean.strip())
                processed_sigma = float(sigma.strip())
                player_stats.append(
                    PlayerStats(
                        name=processed_name, mean=processed_mean, sigma=processed_sigma
                    )
                )

        return player_stats
