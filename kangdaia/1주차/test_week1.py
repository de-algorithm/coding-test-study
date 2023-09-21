from unittest import TestCase, main
from build_frame import build_frame_solution

class Week1(TestCase):
    def test_build_frame_1(self):
        self.assertEqual(
            build_frame_solution(
                5,
                [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
            ), 
            [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]
        )
    def test_build_frame_2(self):
        self.assertEqual(
            build_frame_solution(
                5,
                [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
            ), 
            [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]
        )

if __name__ == '__main__':
    main()
