import sys
sys.path.append('../../')
from week1.문자열_압축 import solution
from unittest import TestCase, main


class Cache(TestCase):
    def test_compress_1(self):
        self.assertEqual(solution("aabbaccc"), 7)

    def test_compress_2(self):
        self.assertEqual(solution("ababcdcdababcdcd"), 9)

    def test_compress_3(self):
        self.assertEqual(solution("abcabcdede"), 8)

    def test_compress_4(self):
        self.assertEqual(solution("abcabcabcabcdededededede"), 14)


if __name__ == "__main__":
    main()

