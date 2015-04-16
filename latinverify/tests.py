__author__ = 'andrewsemikov'

import unittest
from latinverify import HtmlVerify
import os


class DomainTest(unittest.TestCase):

    def test_html_text(self):

        current_dir = os.path.dirname(__file__)

        html_verification = HtmlVerify()

        with open(current_dir + '/test_fixtures/test1.html') as testfile:
            html_verification.search(testfile.read())

if __name__ == '__main__':
    unittest.main()
