__author__ = 'andrewsemikov'

import unittest
from latinverify import HtmlVerify
import os


class HtmlVerifyTest(unittest.TestCase):

    def setUp(self):
        super(HtmlVerifyTest, self).setUp()
        self.current_dir = os.path.dirname(__file__)

    def test_html_text_single_line(self):
        html_verification = HtmlVerify()

        with open(self.current_dir + '/test_fixtures/test_singleline.html') as testfile:
            self.assertDictEqual(
                html_verification.search(testfile.read()),
                {5: [16]}
            )

    def test_html_singleline_several_occurances(self):
        html_verification = HtmlVerify()

        with open(self.current_dir + '/test_fixtures/test_singleline_several_occurances.html') as testfile:
            self.assertDictEqual(
                html_verification.search(testfile.read()),
                {5: [16, 26, 27, 28]}
            )

    def test_html_multiline(self):
        html_verification = HtmlVerify()

        with open(self.current_dir + '/test_fixtures/test_multiline.html') as testfile:
            self.assertDictEqual(
                html_verification.search(testfile.read()),
                {8: [17, 20, 21, 22, 23, 24], 5: [28, 29, 30, 31, 32, 33, 34]}
            )


if __name__ == '__main__':
    unittest.main()
