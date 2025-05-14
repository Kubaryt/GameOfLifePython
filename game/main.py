import typer

from game.utils.map import Map

app = typer.Typer()


@app.command()
def main(map_grid: str = None):
    game_map = Map()
    if map_grid is not None:
        game_map.load_from_str(map_grid)
    game_map.run()


if __name__ == "__main__":
    app()
