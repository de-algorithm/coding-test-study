import sys
import os

# Add the directory containing solution.py to the Python path
current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, os.path.pardir, os.path.pardir)
solution_dir = os.path.abspath(parent_dir)
sys.path.insert(0, solution_dir)


from week2.problem2 import solution
from unittest import TestCase, main


class Problem2(TestCase):
    def test_solution_1(self):
        self.assertEqual(solution(2, [5, 6], [0, 0, 1, 0]), [30, 30])

    def test_solution_2(self):
        self.assertEqual(solution(3, [3, 4, 5], [1, 0, 1, 0]), [35, 17])

    def test_solution_3(self):
        self.assertEqual(
            solution(6, [1, 2, 3, 4, 5, 6], [2, 1, 1, 1]), [54, -24]
        )

    def test_solution_4(self):
        self.assertEqual(
            solution(5, [100, 100, 100, 100, 10], [0, 0, 4, 0]), [1e9, 1e9]
        )


if __name__ == "__main__":
    main()