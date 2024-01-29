from unittest import TestCase, main
from build_frame import build_frame_solution
from compress_str import compress_str_solution

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
    def test_compress_str_1(self):
        self.assertEqual(
            compress_str_solution(
                "aabbaccc"
            ),
            7
        )
    def test_compress_str_2(self):
        self.assertEqual(
            compress_str_solution(
                "ababcdcdababcdcd"
            ),
            9
        )
    def test_compress_str_3(self):
        self.assertEqual(
            compress_str_solution(
                "abcabcdede"
            ),
            8
        )
    def test_compress_str_4(self):
        self.assertEqual(
            compress_str_solution(
                "abcabcabcabcdededededede"
            ),
            14
        )
    def test_compress_str_5(self):
        self.assertEqual(
            compress_str_solution(
                "xababcdcdababcdcd"
            ),
            17
        )

if __name__ == '__main__':
    main()
