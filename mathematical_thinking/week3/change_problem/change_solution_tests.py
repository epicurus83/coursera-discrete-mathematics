import unittest

from mathematical_thinking.week3.change_problem.change_solution import change


class MyTestCase(unittest.TestCase):
    def test_invalid_input(self):
        _invalid_amounts = [None, -1, 23, 1001]
        for amounts in _invalid_amounts:
            with self.assertRaises(ValueError):
                change(amounts)

    def test_valid_input(self):
        for test_case in _test_cases:
            _change_list = change(test_case['amount'])
            _exp_change_list = test_case['exp_change_list']
            self.assertEqual(_exp_change_list, _change_list,
                             'Test case ' + str(test_case['case_num']) + ' failed')


_test_cases = [
    {
        'case_num': 1,
        'amount': 28,
        'exp_change_list': [7, 7, 7, 7]
        # If amount is a multiple of 7.
    },
    {
        'case_num': 2,
        'amount': 24,
        'exp_change_list': [7, 7, 5, 5]
    },
    {
        'case_num': 3,
        'amount': 32,
        'exp_change_list': [7, 5, 5, 5, 5, 5]
    },
    {
        'case_num': 4,
        'amount': 101,
        'exp_change_list': [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 5, 5]
    },
    {
        'case_num': 5,
        'amount': 1000,
        'exp_change_list': [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
                            7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
                            7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
                            7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
                            7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 5, 5, 5, 5]
    }
]

if __name__ == '__main__':
    unittest.main()
