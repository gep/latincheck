__author__ = 'andrewsemikov'

import re as regex


class HtmlVerify(object):

    def __init__(self):
        self.non_latin_regex = regex.compile(ur'[\u0400-\u04FF\u0500-\u052F]')
        self.default_encoding = 'utf-8'

    def search(self, html):
        """
        :param html: str|unicode
        :return dict
        """

        # make html instance of unicode
        html = (isinstance(html, unicode) and [html] or [self._decode_html(html, self.default_encoding)])[0]

        occurances = {}
        line_number = 0

        for line in html.splitlines():
            line_number += 1
            indices = [m.start(0) for m in self.non_latin_regex.finditer(line)]
            if len(indices) == 0:
                continue
            occurances[line_number] = indices

        return occurances

    def _decode_html(self, html, encoding='utf-8'):
        """
        Try to decode html into unicode string from given encoding
        :param html:
        :param encoding:
        :return:
        """
        try:
            return html.decode(encoding=encoding)
        except UnicodeError:
            try:
                return html.decode(encoding='cp1251')
            except UnicodeError:
                return html.decode(encoding='koi8_r')