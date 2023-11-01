from unittest import TestCase, main
from best_album import most_played_song


class Cache(TestCase):
    def test_best_album_1(self):
        self.assertEqual(
            most_played_song(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]),
            [4,1,3,0]
        )



if __name__ == "__main__":
    main()