from unittest import TestCase, main
from skill_tree import solution

class SolutionTestCase(TestCase):
    def test_solution_1(self):
        answer = solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])
        self.assertEqual(answer, 2)
    
    def test_solution_2(self):
        answer = solution("CBD", ["AEZ"])
        self.assertEqual(answer, 1)

if __name__ == "__main__":
    main()