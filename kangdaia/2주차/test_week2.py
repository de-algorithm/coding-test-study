from unittest import TestCase, main
from flight_route import flight_route_backtracking
from sequence_op import sequence_add_operator
from start_taxi import start_taxi_route
from skill_tree import skill_tree


class Week2(TestCase):
    def test_flight_route_1(self):
        self.assertEqual(
            flight_route_backtracking(
                [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
            ),
            ["ICN", "JFK", "HND", "IAD"],
        )

    def test_flight_route_2(self):
        self.assertEqual(
            flight_route_backtracking(
                [
                    ["ICN", "SFO"],
                    ["ICN", "ATL"],
                    ["SFO", "ATL"],
                    ["ATL", "ICN"],
                    ["ATL", "SFO"],
                ]
            ),
            ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"],
        )

    def test_sequence_op_1(self):
        self.assertEqual(
            sequence_add_operator(2, [5, 6], [0, 0, 1, 0]),
            [30, 30]
        )

    def test_sequence_op_2(self):
        self.assertEqual(
            sequence_add_operator(3, [3, 4, 5], [1, 0, 1, 0]),
            [35, 17]
        )

    # 최댓값: 1-2÷3+4+5×6
    # 최솟값: 1+2+3÷4-5×6
    def test_sequence_op_3(self):
        self.assertEqual(
            sequence_add_operator(6, [1, 2, 3, 4, 5, 6], [2, 1, 1, 1]),
            [54, -24]
        )

    def test_sequence_op_4(self):
        self.assertEqual(
            sequence_add_operator(5, [100, 100, 100, 100, 10], [0, 0, 4, 0]),
            [1e9, 1e9]
        )

    def test_start_taxi_1(self):
        self.assertEqual(
            start_taxi_route(15,
                [
                    [0, 0, 1, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0],
                    [0, 0, 0, 1, 0, 0]
                ],
                [6, 5],
                [
                    [2, 2, 5, 6],
                    [5, 4, 1, 6],
                    [4, 2, 3, 5]
                ]
            ), 14
        )

    def test_skill_tree_1(self):
        self.assertEqual(
            skill_tree(
                "CBD",
                ["BACDE", "CBADF", "AECB", "BDA", "CAD", "BAD", "CED"]
            ), 2
        )

    def test_skill_tree_2(self):
        self.assertEqual(
            skill_tree(
                "CBD",
                ["AEF", "ZJW"]
            ), 2
        )


if __name__ == "__main__":
    main()
