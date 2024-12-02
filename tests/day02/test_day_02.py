import unittest
from day02.main import check_reports

data = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

class Day2Tests(unittest.TestCase):
    def test_check_reports(self):
        assert check_reports(data) == 2

    def test_check_problem_dampener(self):
        assert check_reports(data) == 4

    def test_check_edge_cases(self):
        assert check_problem_dampener("""
48 46 47 49 51 54 56
1 1 2 3 4 5
1 2 3 4 5 5
5 1 2 3 4 5
1 4 3 2 1
1 6 7 8 9
1 2 3 4 3
9 8 7 6 7
7 10 8 10 11
29 28 27 25 26 25 22 20
        """) == 10