__author__ = 'andrewsemikov'

import re as regex


class HtmlVerify(object):

    def __init__(self):
        self.non_latin_regex = regex.compile(ur'[\u0400-\u04FF\u0500-\u052F]')

    def search(self, html):
        """
        :param html: str|unicode
        :return dict
        """
        occurances = {}
        line_number = 0

        for line in html.splitlines():
            line_number += 1
            indices = [m.start(0) for m in self.non_latin_regex.finditer(line)]
            if len(indices) == 0:
                continue
            occurances[line_number] = indices

        return occurances