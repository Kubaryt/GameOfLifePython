class AbstractMap:
    """
    Abstract class for the map.
    """

    population = (int,)
    generation = (int,)
    map = (list[list[bool]],)

    def __init__(self):
        """
        Initializes the map with a default map containing living cells on coordinates y = 1 and x from 0 to 4
        and a population of 5.
        """
        self.population = 5
        self.generation = 0

        blank_map = [[False for _ in range(10)] for _ in range(10)]
        blank_map[1][0] = True
        blank_map[1][1] = True
        blank_map[1][2] = True
        blank_map[1][3] = True
        blank_map[1][4] = True

        self.map = blank_map

    def __str__(self) -> str:
        """
        Converts the map to a string.
        :return: Map as a string.
        """
        map_to_str = ""
        for row in self.map:
            map_to_str += "".join(["#" if cell else "." for cell in row]) + "\n"

        return map_to_str

    def count_neighbours(self, x, y) -> int:
        """
        Counts the number of living cells around a cell.
        :param x: index of the row (one list in the map)
        :param y: index of the column (whole map)
        :return: Number of living cells around the cell.
        """
        neighbours = 0

        if len(self.map) == 1:
            if len(self.map[y]) == 1:
                return neighbours

        try:
            self.map[y][x]
        except IndexError:
            raise IndexError("Invalid coordinates.") from IndexError

        if y == 0:
            if len(self.map[y]) == 1:
                neighbouring_cells = [self.map[y][x]] + [self.map[y + 1][x]]
            elif x == 0:
                neighbouring_cells = self.map[y][x + 1 : x + 2] + self.map[y + 1][x : x + 2]
            elif x != len(self.map[y]) - 1:
                neighbouring_cells = [self.map[y][x - 1], self.map[y][x + 1]] + self.map[y + 1][x - 1 : x + 2]
            else:
                neighbouring_cells = self.map[y][x - 1 : x] + self.map[y + 1][x - 1 : x + 1]
        elif y != len(self.map) - 1:
            if x == 0:
                neighbouring_cells = [self.map[y][x + 1]] + self.map[y - 1][x : x + 2] + self.map[y + 1][x : x + 2]
            elif x != len(self.map[y]) - 1:
                neighbouring_cells = (
                    [self.map[y][x - 1], self.map[y][x + 1]]
                    + self.map[y - 1][x - 1 : x + 2]
                    + self.map[y + 1][x - 1 : x + 2]
                )
            else:
                neighbouring_cells = (
                    self.map[y - 1][x - 1 : x + 1] + self.map[y][x - 1 : x] + self.map[y + 1][x - 1 : x + 1]
                )
        else:
            if x == 0:
                neighbouring_cells = [self.map[y][x + 1]] + self.map[y - 1][x : x + 2]
            elif x != len(self.map[y]) - 1:
                neighbouring_cells = [self.map[y][x - 1], self.map[y][x + 1]] + self.map[y - 1][x - 1 : x + 2]
            else:
                neighbouring_cells = self.map[y][x - 1 : x] + self.map[y - 1][x - 1 : x + 1]

        for cell in neighbouring_cells:
            if cell:
                neighbours += 1
            else:
                continue

        return neighbours

    def next_generation(self):
        """
        Calculates the next generation of the map.
        """
        pass


class Map(AbstractMap):
    """
    Class for the map with range = 1 and configurable birth and survival conditions.
    """

    birth_condition = (list[int],)
    survival_condition = (list[int],)

    def __init__(self):
        """
        Initializes the map with a default map and a population of 5.
        """
        super().__init__()
        self.birth_condition = [3]
        self.survival_condition = [2, 3]

    def __str__(self) -> tuple[str, int, int]:
        """
        Converts the map to a string and return it with current population and generation.
        :return: Map as a string, population count, generation number.
        """
        map_str = super().__str__()

        return map_str, self.population, self.generation

    def next_generation(self):
        """
        Calculates the next generation of the map.
        """
        new_map = [[False for _ in range(10)] for _ in range(10)]
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
