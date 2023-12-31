from unittest import TestCase, main
from cache import cache_loadtime
from card_purchase import ps_card_collector
from stepping_stone import fall_picnic
from tree_cutting import wood_cutter


class Cache(TestCase):
    def test_cache_1(self):
        self.assertEqual(
            cache_loadtime(
                3,
                ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
            ), 50
        )

    def test_cache_2(self):
        self.assertEqual(
            cache_loadtime(
                3,
                ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
            ), 21
        )

    def test_cache_3(self):
        self.assertEqual(
            cache_loadtime(
                2,
                ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
            ), 60
        )

    def test_cache_4(self):
        self.assertEqual(
            cache_loadtime(
                5,
                ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
            ), 52
        )

    def test_cache_5(self):
        self.assertEqual(
            cache_loadtime(
                2,
                ["Jeju", "Pangyo", "NewYork", "newyork"]
            ), 16
        )

    def test_cache_6(self):
        self.assertEqual(
            cache_loadtime(
                0,
                ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
            ), 25
        )

    def test_cache_7(self):
        self.assertEqual(
            cache_loadtime(
                0,
                ["LA", "LA"]
            ), 10
        )

    def test_cache_8(self):
        self.assertEqual(
            cache_loadtime(
                5,
                ["LA", "LA"]
            ), 6
        )

    def test_card_purchase_1(self):
        self.assertEqual(
            ps_card_collector(4, "1 5 6 7"), 10
        )

    def test_card_purchase_2(self):
        self.assertEqual(
            ps_card_collector(5, "10 9 8 7 6"), 50
        )

    def test_card_purchase_3(self):
        self.assertEqual(
            ps_card_collector(10, "1 1 2 3 5 8 13 21 34 55"), 55
        )

    def test_card_purchase_4(self):
        self.assertEqual(
            ps_card_collector(10, "5 10 11 12 13 30 35 40 45 47"), 50
        )

    def test_card_purchase_5(self):
        self.assertEqual(
            ps_card_collector(4, "5 2 8 10"), 20
        )

    def test_card_purchase_6(self):
        self.assertEqual(
            ps_card_collector(4, "3 5 15 16"), 18
        )

    def test_card_purchase_7(self):
        self.assertEqual(
            ps_card_collector(5, "1 9 18 25 1"), 27
        )

    def test_stepping_stone_1(self):
        self.assertEqual(
            fall_picnic([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3), 3
        )

    def test_stepping_stone_2(self):
        self.assertEqual(
            fall_picnic([7, 2, 8, 7, 2, 5, 9], 3), 7
        )

    def test_stepping_stone_3(self):
        self.assertEqual(
            fall_picnic([5], 3), 5
        )

    def test_tree_cutting_1(self):
        self.assertEqual(
            wood_cutter(7, "20 15 10 17"), 15
        )

    def test_tree_cutting_2(self):
        self.assertEqual(
            wood_cutter(20, "4 42 40 26 46"), 36
        )

    def test_tree_cutting_3(self):
        self.assertEqual(
            wood_cutter(1, "1 3 3 10"), 9
        )
    
    def test_tree_cutting_4(self):
        self.assertEqual(
            wood_cutter(17, "1 3 3 10"), 0
        )

    def test_tree_cutting_5(self):
        self.assertEqual(
            wood_cutter(1, "1"), 0
        )

if __name__ == "__main__":
    main()
