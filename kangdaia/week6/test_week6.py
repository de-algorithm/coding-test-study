from unittest import TestCase, main
from napsacks import hold_items


class Cache(TestCase):
    def test_napsacks_1(self):
        self.assertEqual(
            hold_items(2, 1, [1, 1]), 3
        )
    
    def test_napsacks_2(self):
        self.assertEqual(
            hold_items(1, 1, [1]), 2
        )

if __name__ == "__main__":
    main()
