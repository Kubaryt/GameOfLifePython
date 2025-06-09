class AbstractMap:
    """
    Abstract class for the map.
    """

    population = int
    generation = int
    map = list[list[bool]]

    def __init__(self, game_map: list[list[bool]] = None):
        if game_map is None:
            game_map = [[False for _ in range(10)] for _ in range(10)]
            game_map[1][0] = True
            game_map[1][1] = True
            game_map[1][2] = True
            game_map[1][3] = True
            game_map[1][4] = True

        self.generation = 0
        self.map = game_map
        self.population = self.count_population()

    def __str__(self) -> str:
        map_to_str = ""
        for row in self.map:
            map_to_str += "".join(["#" if cell else "." for cell in row]) + "\n"

        return map_to_str

    def count_population(self) -> int:
        population = 0

        for row in self.map:
            for cell in row:
                if cell:
                    population += 1
                else:
                    continue

        return population

    def count_neighbours(self, x, y) -> int:
        neighbours = 0

        if len(self.map) == 1:
            if len(self.map[y]) == 1:
                return neighbours

        try:
            self.map[y][x]
        except IndexError:
            raise IndexError("Invalid coordinates.") from IndexError

        for i in range(y - 1, y + 2):
            if 0 <= i < len(self.map):
                for j in range(x - 1, x + 2):
                    if 0 <= j < len(self.map[i]) and (i != y or j != x):
                        if self.map[i][j]:
                            neighbours += 1

        return neighbours

    def next_generation(self):
        pass


class Map(AbstractMap):
    birth_condition = (list[int],)
    survival_condition = (list[int],)
    number_of_rows = int
    number_of_columns = int

    def __init__(self, game_map: list[list[bool]] = None):
        super().__init__(game_map)
        self.birth_condition = [3]
        self.survival_condition = [2, 3]
        self.number_of_rows = len(self.map)
        self.number_of_columns = len(self.map[0])

    def __str__(self) -> str:
        map_str = ""
        for row in self.map:
            map_str += "".join(["# " if cell else ". " for cell in row])
            map_str = map_str.strip()
            map_str += "\n"

        return map_str

    def load_from_str(self, map_grid: str):
        """
        Load the map from a string.
        Use space for end of row, . for dead cells and # for alive cells.
        """
        rows = map_grid.split(" ")
        self.load_from_rows(rows)

    def load_from_file(self, file_path: str):
        """
        Load the map from a file.
        Use line breaks for end of row, . for dead cells and # for alive cells.
        """
        with open(file_path) as file:
            map_grid = file.readlines()
            self.load_from_rows(map_grid)

    def load_from_rows(self, rows: list[str]):
        self.number_of_rows = len(rows)
        self.number_of_columns = len(rows[0].strip())
        self.map = [[False for _ in range(self.number_of_columns)] for _ in range(self.number_of_rows)]
        for y, line in enumerate(rows):
            for x, char in enumerate(line.strip()):
                if char == "#":
                    self.map[y][x] = True
                elif char != ".":
                    raise ValueError(f"Invalid character '{char}' in map string.")

        self.population = self.count_population()

    def next_generation(self):
        new_map = [[False for _ in range(self.number_of_columns)] for _ in range(self.number_of_rows)]
        population = 0

        for y, row in enumerate(self.map):
            for x, cell in enumerate(row):
                neighbours = self.count_neighbours(x, y)

                if cell:
                    if neighbours in self.survival_condition:
                        population += 1
                        new_map[y][x] = True
                else:
                    if neighbours in self.birth_condition:
                        population += 1
                        new_map[y][x] = True

        self.map = new_map
        self.generation += 1
        self.population = population
