from typing import Annotated

import typer

from game.utils.cli import parse_multiple_value_argument_from_str
from game.utils.map import Map
from game.utils.tui import run

app = typer.Typer()


@app.callback(invoke_without_command=True)
def main(
    map_grid: Annotated[
        str,
        typer.Option(
            help="Load a map from a string representation",
        ),
    ] = None,
    file_path: Annotated[
        str,
        typer.Option(
            help="Load a map from a file",
        ),
    ] = None,
    survival_condition: Annotated[
        str,
        typer.Option(
            help="Survival condition for the game, e.g., [2, 3]",
        ),
    ] = None,
    birth_condition: Annotated[
        str,
        typer.Option(
            help="Birth condition for the game, e.g., [3]",
        ),
    ] = None,
    neighbouring_condition: Annotated[
        int,
        typer.Option(
            help="Number of neighbouring cells to consider for the game",
        ),
    ] = 1,
):
    game_map = Map()

    if survival_condition is not None:
        game_map.survival_condition = parse_multiple_value_argument_from_str(survival_condition)
    if birth_condition is not None:
        game_map.birth_condition = parse_multiple_value_argument_from_str(birth_condition)
    if neighbouring_condition is not None:
        game_map.neighbouring_condition = neighbouring_condition

    if file_path is not None:
        game_map.load_from_file(file_path)
    elif map_grid is not None:
        game_map.load_from_str(map_grid)
    run(game_map)


if __name__ == "__main__":
    app()
