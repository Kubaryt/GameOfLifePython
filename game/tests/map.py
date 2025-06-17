from game.utils.map import Map


def test_neighbour_count():
    excepted_neighbours = 2
    game_map = Map()

    neighbours = game_map.count_neighbours(1, 1)

    assert neighbours == excepted_neighbours


def test_neighbour_count_condition_2():
    excepted_neighbours = 3
    game_map = Map()

    neighbours = game_map.count_neighbours(1, 2)
    assert neighbours == excepted_neighbours

def test_neighbour_count_fail():
    excepted_neighbours = 1
    game_map = Map()

    neighbours = game_map.count_neighbours(1, 1)

    assert neighbours != excepted_neighbours


def test_next_generation():
    expected_map = [[False, True, True, True, False, False, False, False, False, False] for _ in range(3)] + [
        [False for _ in range(10)] for _ in range(7)
    ]
    print(expected_map)
    game_map = Map()

    game_map.next_generation()
    print(game_map.map)

    assert game_map.map == expected_map
