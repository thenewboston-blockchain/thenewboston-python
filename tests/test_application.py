import unittest

import pycodestyle


class TestApplication(unittest.TestCase):

    def test_style(self):
        """
        Test PEP 8 style conventions
        E501 - Line too long (82 > 79 characters)
        W504 - Line break occurred after a binary operator
        """

        style = pycodestyle.StyleGuide(ignore=['E501', 'W504'])
        result = style.check_files([
            'tests/',
            'thenewboston/',
        ])
        self.assertEqual(result.total_errors, 0)
