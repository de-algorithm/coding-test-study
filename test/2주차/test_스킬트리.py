import sys
import os

# Add the directory containing solution.py to the Python path
current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, os.path.pardir, os.path.pardir)
solution_dir = os.path.abspath(parent_dir)
sys.path.insert(0, solution_dir)


from week2.problem4 import solution
from unittest import TestCase, main


class Problem4(TestCase):
    def test_solution_1(self):
        self.assertEqual(
            solution("CBD", ["BACDE", "CBADF", "AECB", "BDA", "CAD"]), 2
        )

    def test_solution_2(self):
        self.assertEqual(solution("CBD", ["AEF", "ZJW"]), 2)



if __name__ == "__main__":
    main()