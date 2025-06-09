from game.utils.map import Map
from game.utils.tui import prepare_display


def test_from_arg():
    game_map = Map()
    game_map.load_from_str("..... .### # ....# .")

    assert game_map.map == [
        [False for _ in range(5)],
        [False] + [True for _ in range(3)] + [False],
        [True] + [False for _ in range(4)],
        [False for _ in range(4)] + [True],
        [False for _ in range(5)],
    ]


def test_from_file():
    game_map = Map()
    game_map.load_from_file("game/tests/test_map.txt")

    assert game_map.map == [
        [False for _ in range(5)],
        [False] + [True for _ in range(3)] + [False],
        [True] + [False for _ in range(4)],
        [False for _ in range(4)] + [True],
        [False for _ in range(5)],
    ]


def test_from_arg_and_from_file_are_identical():
    game_map_from_arg = Map()
    game_map_from_arg.load_from_str("..... .### # ....# .")

    game_map_from_file = Map()
    game_map_from_file.load_from_file("game/tests/cli/test_map.txt")

    assert game_map_from_arg.map == game_map_from_file.map


def test_tui():
    game_map = Map()
    game_map.load_from_file("game/tests/cli/test_map.txt")

    display = prepare_display(game_map, state={"paused": False})

    expected_display = open("game/tests/cli/expected_display.txt").read()

    assert display == expected_display
