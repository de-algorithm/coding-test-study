from unittest import TestCase, main
from best_album import most_played_song
from AB import query_executor


class Cache(TestCase):
    def test_best_album_1(self):
        self.assertEqual(
            most_played_song(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]),
            [4,1,3,0]
        )
    def test_ab_1(self):
        self.assertEqual(
            query_executor([
                "add A aba",
                "add A a",
                "add A ab",
                "add B bab",
                "add B b",
                "add B ab",
                "find abab"
            ]), 10
        )



if __name__ == "__main__":
    main()