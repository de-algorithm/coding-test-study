import sys
import os

# Add the directory containing solution.py to the Python path
current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, os.path.pardir, os.path.pardir)
solution_dir = os.path.abspath(parent_dir)
sys.path.insert(0, solution_dir)


from week1.기둥과_보_설치 import solution
from unittest import TestCase, main


class Test1(TestCase):
    def test_solution_1(self):
        self.assertEqual(
            solution(
                5,
                [
                    [1, 0, 0, 1],
                    [1, 1, 1, 1],
                    [2, 1, 0, 1],
                    [2, 2, 1, 1],
                    [5, 0, 0, 1],
                    [5, 1, 0, 1],
                    [4, 2, 1, 1],
                    [3, 2, 1, 1],
                ],
            ),
            [
                [1, 0, 0],
                [1, 1, 1],
                [2, 1, 0],
                [2, 2, 1],
                [3, 2, 1],
                [4, 2, 1],
                [5, 0, 0],
                [5, 1, 0],
            ],
        )

    def test_solution_2(self):
        self.assertEqual(
            solution(
                5,
                [
                    [0, 0, 0, 1],
                    [2, 0, 0, 1],
                    [4, 0, 0, 1],
                    [0, 1, 1, 1],
                    [1, 1, 1, 1],
                    [2, 1, 1, 1],
                    [3, 1, 1, 1],
                    [2, 0, 0, 0],
                    [1, 1, 1, 0],
                    [2, 2, 0, 1],
                ],
            ),
            [[0, 0, 0], [0, 1, 1], [1, 1, 1], [2, 1, 1], [3, 1, 1], [4, 0, 0]],
        )


if __name__ == "__main__":
    main()
