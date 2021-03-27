import unittest

from mathematical_thinking.week2.diagonals_problem.diagonals_solutions import can_extend_to_solution, \
    determines_diagonals_solutions
from mathematical_thinking.week2.diagonals_problem.utils import convert_solutions_to_string


class TestCanBeExtendedToSolution(unittest.TestCase):

    def test(self):
        for _test_case in _test_cases:
            if _test_case['valid'] != can_extend_to_solution(_test_case['perm'], _test_case['board_len']):
                message = 'Test case %s failed. Description: %s.' % (_test_case['case_num'], _test_case['description'])
                raise AssertionError(message)


# LD = '\'
# RD = '/'
# VOID = '_'
_test_cases = [
    {
        'case_num': '1',
        'board_len': 3,
        'perm': ['/'],
        'valid': True,
        'description': 'Single RD valid'
    },
    {
        'case_num': '2',
        'board_len': 3,
        'perm': ['\\', '/'],
        'valid': False,
        'description': 'Insert RD right of LD invalid'
    },
    {
        'case_num': '3',
        'board_len': 3,
        'perm': ['_', '_', '_', '_', '_', '\\', '/'],
        'valid': True,
        'description': 'Insert RD right of LD valid because RD is on next row'
    },
    {
        'case_num': '4',
        'board_len': 3,
        'perm': ['/', '/', '/'],
        'valid': True,
        'description': '3 adjacent RD valid'
    },
    {
        'case_num': '5',
        'board_len': 3,
        'perm': ['_', '_', '_', '\\', '_', '_', '/'],
        'valid': False,
        'description': 'Insert RD below a LD invalid'
    },
    {
        'case_num': '6',
        'board_len': 3,
        'perm': ['\\', '_', '_', '_', '/'],
        'valid': True,
        'description': 'Insert RD bottom right of LD is valid'
    },
    {
        'case_num': '7',
        'board_len': 3,
        'perm': ['_', '_', '_', '_', '/', '_', '/'],
        'valid': False,
        'description': 'Insert RD bottom left of RD is invalid'
    },
    {
        'case_num': '8',
        'board_len': 3,
        'perm': ['/', '_', '_', '/', '_', '_', '/'],
        'valid': True,
        'description': 'Insert 3 RD in a column is valid'
    },
    {
        'case_num': '9',
        'board_len': 3,
        'perm': ['_', '_', '_', '_', '_', '_', '_', '_', '/'],
        'valid': True,
        'description': 'Insert RD in bottom right of board'
    },
    {
        'case_num': '10',
        'board_len': 3,
        'perm': ['\\'],
        'valid': True,
        'description': 'Single LD valid'
    },
    {
        'case_num': '11',
        'board_len': 3,
        'perm': ['/', '\\'],
        'valid': False,
        'description': 'Insert LD right of RD invalid'
    },
    {
        'case_num': '12',
        'board_len': 3,
        'perm': ['_', '_', '_', '_', '_', '/', '\\'],
        'valid': True,
        'description': 'Insert LD right of RD valid because LD is on next row'
    },
    {
        'case_num': '13',
        'board_len': 3,
        'perm': ['\\', '\\', '\\'],
        'valid': True,
        'description': '3 adjacent LD valid'
    },
    {
        'case_num': '14',
        'board_len': 3,
        'perm': ['_', '_', '_', '/', '_', '_', '\\'],
        'valid': False,
        'description': 'Insert LD below a RD invalid'
    },
    {
        'case_num': '15',
        'board_len': 3,
        'perm': ['/', '_', '_', '_', '\\'],
        'valid': True,
        'description': 'Insert LD bottom right of RD is valid'
    },
    {
        'case_num': '16',
        'board_len': 3,
        'perm': ['_', '_', '_', '\\', '_', '_', '_', '\\'],
        'valid': False,
        'description': 'Insert LD bottom right of LD is invalid'
    },
    {
        'case_num': '17',
        'board_len': 3,
        'perm': ['\\', '_', '_', '\\', '_', '_', '\\'],
        'valid': True,
        'description': 'Insert 3 LD in a column is valid'
    },
    {
        'case_num': '18',
        'board_len': 3,
        'perm': ['_', '_', '_', '_', '_', '_', '_', '_', '\\'],
        'valid': True,
        'description': 'Insert LD in bottom right of board'
    },
    {
        'case_num': '19',
        'board_len': 3,
        'perm': ['\\', '\\', '\\', '\\', '_'],
        'valid': True,
        'description': 'Insert space is always valid'
    },
    {
        'case_num': '20',
        'board_len': 5,
        'perm': ['/', '/', '/', '_', '\\', '_', '_', '/', '_', '\\', '\\', '\\', '_', '\\', '\\', '\\'],
        'valid': True,
        'description': 'Insert a LD at the start of new row in grid not check top left value'
    },
    {
        'case_num': '21',
        'board_len': 5,
        'perm': ['_', '_', '_', '_', '_', '_', '_', '_', '_', '/', '/', '/', '_', '_', '/', '_', '_', '_', '_', '/'],
        'valid': True,
        'description': 'Insert a LD at the start of new row in grid not check top left value'
    }
]


class TestFillBoardWithDiagonals(unittest.TestCase):

    def test_board_3_by_3(self):
        solution = determines_diagonals_solutions(board_len=3, diagonals_num=6)
        expected_solution = [
            ['/', '/', '/', '_', '_', '/', '\\', '\\', '_']
        ]
        _test_solutions_is_as_expected(solution, expected_solution, 3)

    def test_board_4_by_4(self):
        solutions = determines_diagonals_solutions(board_len=4, diagonals_num=10)
        expected_solutions = [
            ['/', '/', '/', '/', '_', '_', '_', '/', '/', '/', '_', '_', '_', '/', '/', '/']
        ]
        _test_solutions_is_as_expected(solutions, expected_solutions, 4)

    def test_board_5_by_5(self):
        solutions = determines_diagonals_solutions(board_len=5, diagonals_num=16)
        expected_solutions = [
            ['/', '/', '/', '_', '\\', '_', '_', '/', '_', '\\', '\\', '\\', '_', '\\', '\\', '\\', '_', '/', '_', '_',
             '\\', '_', '/', '/', '/']
        ]
        _test_solutions_is_as_expected(solutions, expected_solutions, 5)


def _test_solutions_is_as_expected(solution, expected_solution, board_len):
    if solution != expected_solution:
        message = 'Was: ' + convert_solutions_to_string(solution, board_len) + '\n' \
                  + 'expected: ' + convert_solutions_to_string(expected_solution, board_len)
        raise AssertionError(message)


if __name__ == '__main__':
    unittest.main()
