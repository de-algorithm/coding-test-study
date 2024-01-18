from unittest import TestCase, main
from compress import lzw_zip
from simplify_path_71 import canonical_path
from network_delay_time import min_time_cost
from sheep_n_wolf import survive


class Cache(TestCase):

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

    def test_network_delay_1(self):
        self.assertEqual(
            min_time_cost([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2),
            2
        )

    def test_network_delay_2(self):
        self.assertEqual(
            min_time_cost([[1, 2, 1]], 2, 1),
            1
        )

    def test_network_delay_3(self):
        self.assertEqual(
            min_time_cost([[1, 2, 1]], 2, 2),
            -1
        )

    def test_network_delay_4(self):
        self.assertEqual(
            min_time_cost([[1, 2, 1], [2, 3, 2], [1, 3, 2]], 3, 1),
            2
        )

    def test_network_delay_5(self):
        self.assertEqual(
            min_time_cost([[1, 2, 1], [2, 3, 7], [1, 3, 4], [2, 1, 2]], 4, 1),
            -1
        )

    def test_sheep_n_wolf_1(self):
        self.assertEqual(
            survive([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]),
            5
        )

    def test_sheep_n_wolf_2(self):
        self.assertEqual(
            survive([0,1,0,1,1,0,1,0,0,1,0], 	[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]),
            5
        )


if __name__ == "__main__":
    main()
