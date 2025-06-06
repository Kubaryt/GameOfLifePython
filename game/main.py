import typer

from game.utils.map import Map

app = typer.Typer()


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    map_grid: str = typer.Option(
        None,
        "--map-grid",
        "-m",
        help="Load a map from a string representation",
    ),
):
    if ctx.invoked_subcommand is not None:
        return

    game_map = Map()
    if map_grid is not None:
        game_map.load_from_str(map_grid)
    game_map.run()


@app.command()
def from_file(file_path: str):
    game_map = Map()
    game_map.load_from_file(file_path)
    game_map.run()


if __name__ == "__main__":
    app()
