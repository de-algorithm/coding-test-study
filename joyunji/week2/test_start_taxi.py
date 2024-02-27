from unittest import TestCase, main
from start_taxi import solution

class SolutionTestCase(TestCase):
    def test_solution_1(self):
        maps = [
                [0, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0],
                [0, 0, 0, 1, 0, 0] 
            ]
        passengers = [
            [2, 2, 5, 6],
            [5, 4, 1, 6],
            [4, 2, 3, 5]
        ]
        answer = solution(6, 3, 15, maps, 6, 5, passengers)
        self.assertEqual(answer, 14)
        
    def test_solution_2(self):
        maps = [
                [0, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0],
                [0, 0, 0, 1, 0, 0] 
            ]
        passengers = [
            [2, 2, 5, 6],
            [5, 4, 1, 6],
            [4, 2, 3, 5]
        ]
        answer = solution(6, 3, 13, maps, 6, 5, passengers)
        self.assertEqual(answer, -1)
    
    def test_solution_3(self):
        maps = [
                [0, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0],
                [0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 1, 0],
                [0, 0, 0, 1, 0, 0] 
            ]
        passengers = [
            [2, 2, 5, 6],
            [5, 4, 1, 6],
            [4, 2, 3, 5]
        ]
        answer = solution(6, 3, 100, maps, 6, 5, passengers)
        self.assertEqual(answer, -1)
        
if __name__ == "__main__":
    main()