from src.model import PlayerStats, TournamentResult
from src.simulation import SimulationManager


def test_simulation_top_5_tie():
    first_position_players = [PlayerStats("A", 1, 1), PlayerStats("B", 1, 1)]
    top_5_positions_players = [
        PlayerStats("C", 1, 1),
        PlayerStats("D", 1, 1),
        PlayerStats("E", 1, 1),
        PlayerStats("F", 1, 1),
    ]
    simulation_manager = SimulationManager(
        first_position_players + top_5_positions_players
    )
    tournament_results = TournamentResult(
        first_position_players=first_position_players,
        top_5_positions_players=[first_position_players, top_5_positions_players],
    )
    simulation_manager.update_results(tournament_results)
    results = simulation_manager.get_results()
    assert results["A"].player_win_fraction == 1 / 2
    assert results["A"].player_top_5_fraction == 1
    assert results["B"].player_win_fraction == 1 / 2
    assert results["B"].player_top_5_fraction == 1

    assert results["C"].player_win_fraction == 0
    assert results["C"].player_top_5_fraction == 3 / 4
    assert results["D"].player_win_fraction == 0
    assert results["D"].player_top_5_fraction == 3 / 4
    assert results["E"].player_win_fraction == 0
    assert results["E"].player_top_5_fraction == 3 / 4
    assert results["F"].player_win_fraction == 0
    assert results["F"].player_top_5_fraction == 3 / 4


def test_simulation_total_tie():
    players = [
        PlayerStats("A", 1, 1),
        PlayerStats("B", 1, 1),
        PlayerStats("C", 1, 1),
        PlayerStats("D", 1, 1),
        PlayerStats("E", 1, 1),
        PlayerStats("F", 1, 1),
    ]
    simulation_manager = SimulationManager(players)
    tournament_results = TournamentResult(
        first_position_players=players, top_5_positions_players=[players]
    )
    simulation_manager.update_results(tournament_results)
    results = simulation_manager.get_results()
    assert results["A"].player_win_fraction == 1 / 6
    assert results["A"].player_top_5_fraction == 5 / 6
    assert results["B"].player_win_fraction == 1 / 6
    assert results["B"].player_top_5_fraction == 5 / 6
    assert results["C"].player_win_fraction == 1 / 6
    assert results["C"].player_top_5_fraction == 5 / 6
    assert results["D"].player_win_fraction == 1 / 6
    assert results["D"].player_top_5_fraction == 5 / 6
    assert results["E"].player_win_fraction == 1 / 6
    assert results["E"].player_top_5_fraction == 5 / 6
    assert results["F"].player_win_fraction == 1 / 6
    assert results["F"].player_top_5_fraction == 5 / 6
