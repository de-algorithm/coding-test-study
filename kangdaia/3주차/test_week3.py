from unittest import TestCase, main
from surveillance_cam import surveillance_camera


class Week3(TestCase):
    def test_surveil_cam(self):
        self.assertEqual(
            surveillance_camera(
                [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
            ), 2
        )