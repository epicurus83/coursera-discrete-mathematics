import unittest

from week2_mathematical_thinking.diagonals_problem.diagonals_solutions import can_extend_to_solution, \
    determines_diagonals_solutions
from week2_mathematical_thinking.diagonals_problem.utils import convert_solutions_to_string


class TestCanBeExtendedToSolution(unittest.TestCase):

    def test(self):
        for _test_case in _test_cases:
            if _test_case['valid'] != can_extend_to_solution(_test_case['board'], _test_case['x'],
                                                             _test_case['y']):
                message = "Test case %s failed." % _test_case['case_num']
                raise AssertionError(message)


_test_cases = [
    {
        'case_num': "1",
        'board': [
            ["/", -1, -1],
            [-1, -1, -1],
            [-1, -1, -1]
        ],
        'x': 0,
        'y': 0,
        'valid': True
    },
    {
        'case_num': "2",
        'board': [
            ["\\", "/", -1],
            [-1, -1, -1],
            [-1, -1, -1]
        ],
        'x': 0,
        'y': 1,
        'valid': False
    },
    {
        'case_num': "3",
        'board': [
            ["/", "/", "/"],
            [-1, -1, -1],
            [-1, -1, -1]
        ],
        'x': 0,
        'y': 2,
        'valid': True
    },
    {
        'case_num': "4",
        'board': [
            ["\\", -1, -1],
            ["/", -1, -1],
            [-1, -1, -1]
        ],
        'x': 1,
        'y': 0,
        'valid': False
    },
    {
        'case_num': "5",
        'board': [
            [" ", "/", -1],
            ["/", -1, -1],
            [-1, -1, -1]
        ],
        'x': 1,
        'y': 0,
        'valid': False
    },
    {
        'case_num': "6",
        'board': [
            [" ", "/", -1],
            ["/", -1, -1],
            [-1, -1, -1]
        ],
        'x': 0,
        'y': 1,
        'valid': False
    },
    {
        'case_num': "7",
        'board': [
            ["/", -1, -1],
            ["/", -1, -1],
            ["/", -1, -1]
        ],
        'x': 2,
        'y': 0,
        'valid': True
    },
    {
        'case_num': "7.1",
        'board': [
            [-1, -1, -1],
            [-1, -1, -1],
            [-1, -1, "/"]
        ],
        'x': 2,
        'y': 2,
        'valid': True
    },
    {
        'case_num': "8",
        'board': [
            ["\\", -1, -1],
            [-1, -1, -1],
            [-1, -1, -1]
        ],
        'x': 0,
        'y': 0,
        'valid': True
    },
    {
        'case_num': "11",
        'board': [
            ["/", "\\", -1],
            [-1, -1, -1],
            [-1, -1, -1]
        ],
        'x': 0,
        'y': 1,
        'valid': False
    },
    {
        'case_num': "12",
        'board': [
            ["/", -1, -1],
            ["\\", -1, -1],
            [-1, -1, -1]
        ],
        'x': 1,
        'y': 0,
        'valid': False
    },
    {
        'case_num': "13",
        'board': [
            ["\\", -1, -1],
            [-1, "\\", -1],
            [-1, -1, -1]
        ],
        'x': 0,
        'y': 0,
        'valid': False
    },
    {
        'case_num': "14",
        'board': [
            [-1, -1, -1],
            [-1, -1, -1],
            [-1, -1, "\\"]
        ],
        'x': 2,
        'y': 2,
        'valid': True
    },
    {
        'case_num': "15",
        'board': [
            ["\\", -1, -1],
            [-1, "\\", -1],
            [-1, -1, -1]
        ],
        'x': 1,
        'y': 1,
        'valid': False
    },
    {
        'case_num': "16",
        'board': [
            [-1, -1, -1],
            [-1, -1, -1],
            [-1, -1, "\\"]
        ],
        'x': 1,
        'y': 1,
        'valid': True
    },
]


class TestFillBoardWithDiagonals(unittest.TestCase):

    def test_board_3_by_3(self):
        solutions = determines_diagonals_solutions(board_length=3, diagonals_num=6)
        expected_solutions = [
            [
                ['\\', '\\', '\\'],
                ['\\', '_', '_'],
                ['\\', '_', '\\']
            ]
        ]
        _test_solutions_is_as_expected(solutions, expected_solutions)

    def test_board_4_by_4(self):
        solutions = determines_diagonals_solutions(board_length=4, diagonals_num=10)
        expected_solutions = [
            [
                ['\\', '\\', '\\', '\\'],
                ['\\', '_', '_', '_'],
                ['\\', '_', '\\', '\\'],
                ['\\', '_', '\\', '_']
            ]
        ]
        _test_solutions_is_as_expected(solutions, expected_solutions)

    def test_board_5_by_5(self):
        solutions = determines_diagonals_solutions(board_length=5, diagonals_num=16)
        expected_solutions = [
            [
                ['\\', '_', '/', '/', '/'],
                ['\\', '_', '/', '_', '_'],
                ['\\', '\\', '_', '\\', '\\'],
                ['_', '_', '/', '_', '\\'],
                ['/', '/', '/', '_', '\\']
            ]
        ]
        _test_solutions_is_as_expected(solutions, expected_solutions)


def _test_solutions_is_as_expected(solutions, expected_solutions):
    if solutions != expected_solutions:
        message = "Was: " + convert_solutions_to_string(solutions) + "\n" \
                  + "expected: " + convert_solutions_to_string(expected_solutions)
        raise AssertionError(message)


if __name__ == '__main__':
    unittest.main()
