from unittest import TestCase, main
from compress import lzw_zip
from simplify_path_71 import canonical_path


class Cache(TestCase):
    """
    def test_compress_1(self):
        self.assertEqual(
            lzw_zip("KAKAO"), [11, 1, 27, 15]
        )

    def test_compress_2(self):
        self.assertEqual(
            lzw_zip("ABABABABABABABAB"), [1, 2, 27, 29, 28, 31, 30]
        )

    def test_compress_3(self):
        self.assertEqual(
            lzw_zip("TOBEORNOTTOBEORTOBEORNOT"), 
            [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
        )
    """
    def test_simplify_path_1(self):
        self.assertEqual(
            canonical_path("/home/"),
            "/home"
        )
    
    def test_simplify_path_2(self):
        self.assertEqual(
            canonical_path("/../"),
            "/"
        )

    def test_simplify_path_3(self):
        self.assertEqual(
            canonical_path("/home//foo/"),
            "/home/foo"
        )

    def test_simplify_path_4(self):
        self.assertEqual(
            canonical_path("/home/user/Documents/../Pictures"),
            "/home/user/Pictures"
        )
    
    def test_simplify_path_5(self):
        self.assertEqual(
            canonical_path("/../home/user/Documents"),
            "/home/user/Documents"
        )

    def test_simplify_path_6(self):
        self.assertEqual(
            canonical_path("/home/user/../../usr/local/bin"),
            "/usr/local/bin"
        )

    def test_simplify_path_7(self):
        self.assertEqual(
            canonical_path("/home/user/./Downloads/../Pictures/././"),
            "/home/user/Pictures"
        )
    
    def test_simplify_path_8(self):
        self.assertEqual(
            canonical_path("/home/user/Documents/../../usr/local/bin"),
            "/home/usr/local/bin"
        )

if __name__ == "__main__":
    main()
