import unittest
from main import astar

class TestAStar(unittest.TestCase):
    def test_astar(self):
        grid = [[0]*5 for _ in range(5)]
        start = (0, 0)
        goal = (4, 4)
        path = astar(grid, start, goal)
        self.assertIsNotNone(path)

        grid[1][1] = 1
        grid[2][2] = 1
        path = astar(grid, start, goal)
        self.assertIsNone(path)

if __name__ == "__main__":
    unittest.main()