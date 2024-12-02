import unittest
from day01.main import calculate_total_distance, similarity_score, sort_input

data = sort_input("""
3   4
4   3
2   5
1   3
3   9
3   3        
        """)

class Day1Tests(unittest.TestCase):

    def test_calculate_total_distance(self):
        assert calculate_total_distance(*data) == 11

    def test_similarity_score(self):
        assert similarity_score(*data) == 31


if __name__ == '__main__':
    unittest.main()
