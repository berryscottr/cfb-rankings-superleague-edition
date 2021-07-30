import unittest
from src.ranking import ranking


class RankingTestCase(unittest.TestCase):
    def test_ranking(self):
        self.assertTrue(type(ranking()) == int, True)
        self.assertTrue(1 <= ranking() <= 25, True)


if __name__ == '__main__':
    unittest.main()
