from unittest import TestCase, main
from napsacks import hold_items
from ladder import competition


class Cache(TestCase):
    def test_napsacks_1(self):
        self.assertEqual(
            hold_items(2, 1, [1, 1]), 3
        )
    
    def test_napsacks_2(self):
        self.assertEqual(
            hold_items(1, 1, [1]), 2
        )
    
    def test_ladder_1(self):
        self.assertEqual(
            competition(10, 5, "ACGBEDJFIH", 
                        ["*-***-***", "-*-******", "?????????", "-**-***-*", "**-*-*-*-"]),
            "**-*-***-"
        )
    
    def test_ladder_2(self):
        self.assertEqual(
            competition(11, 5, "CGBEDJFKIHA", 
                        ["*-***-****", "-*-******-", "??????????", "-**-***-*-", "**-*-*-*-*"]),
            "xxxxxxxxxx"
        )

if __name__ == "__main__":
    main()
