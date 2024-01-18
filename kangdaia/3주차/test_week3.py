from unittest import TestCase, main
from surveillance_cam import surveillance_camera
from post_office import min_dist_post_office
from file_concat import file_concat_sol
from milky_way_train import travel_milky_way


class Week3(TestCase):
    def test_surveil_cam(self):
        self.assertEqual(
            surveillance_camera(
                [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
            ), 2
        )

    def test_post_office_1(self):
        self.assertEqual(
            min_dist_post_office(
                3, [1, 2, 3], [3, 5, 3]
            ), 2
        )
    
    def test_post_office_2(self):
        self.assertEqual(
            min_dist_post_office(
                4, [1, 2, 3, 4], [1, 1, 1, 1]
            ), 2
        )

    def test_post_office_3(self):
        self.assertEqual(
            min_dist_post_office(
                1, [-1000000000], [1]
            ), -1000000000
        )

    def test_post_office_4(self):
        self.assertEqual(
            min_dist_post_office(
                2, [1, 2], [1, 2]
            ), 2
        )

    def test_file_concat_1(self):
        self.assertEqual(
            file_concat_sol(
                [40, 30, 30, 50]  
            ), 300
        )

    def test_file_concat_2(self):
        self.assertEqual(
            file_concat_sol(
                [1, 21, 3, 4, 5, 35, 5, 4, 3, 5, 98, 21, 14, 17, 32]
            ), 826
        )

    def test_milky_way_train_1(self):
        self.assertEqual(
            travel_milky_way(
                5, ["1 1 1", "1 1 2", "1 2 2", "1 2 3", "3 1"]
            ), 2
        )


if __name__ == "__main__":
    main()
