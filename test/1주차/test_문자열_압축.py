import sys
import os

# Add the directory containing solution.py to the Python path
current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, os.path.pardir, os.path.pardir)
solution_dir = os.path.abspath(parent_dir)
sys.path.insert(0, solution_dir)


from week1.problem2 import solution
from unittest import TestCase, main


class Problem2(TestCase):
    def test_solution_1(self):
        self.assertEqual(solution("aabbaccc"), 7)

    def test_solution_2(self):
        self.assertEqual(solution("ababcdcdababcdcd"), 9)

    def test_solution_3(self):
        self.assertEqual(solution("abcabcdede"), 8)

    def test_solution_4(self):
        self.assertEqual(solution("abcabcabcabcdededededede"), 14)
    
    def test_solution_str_5(self):
        self.assertEqual(solution("xababcdcdababcdcd"), 17)


if __name__ == "__main__":
    main()

