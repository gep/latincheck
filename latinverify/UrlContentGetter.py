__author__ = 'andrewsemikov'
import urllib2
import socket
from StringIO import StringIO
import gzip


class UrlContentGetter(object):

    def __init__(self):
        self.timeout = 5  # seconds
        self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:37.0) Gecko/20100101 Firefox/37.0'
        self.default_encoding = 'utf-8'

    def get_contents(self, url):
        request = urllib2.Request(url)
        request.add_header('User-agent', self.user_agent)

        try:
            response = urllib2.urlopen(request, timeout=self.timeout)

            if response.info().get('Content-Encoding') == 'gzip':
                buffer = StringIO(response.read())
                gzipped_content = gzip.GzipFile(fileobj=buffer)
                response_actual_string = gzipped_content.read()
            else:
                response_actual_string = response.read()

            # make html instance of unicode
            response_actual_string = (
                isinstance(response_actual_string, unicode)
                and [response_actual_string]
                or [self._decode_html(response_actual_string, self.default_encoding)]
            )[0]

            response.close()
        except socket.timeout, e:
            # For Python 2.7
            raise UrlContentGetterException("Error while getting URL contents. Timeout error: %r" % e)
        except urllib2.URLError, e:
            raise UrlContentGetterException("Error while getting URL contents: %r" % e)

        return response_actual_string

    def _decode_html(self, html, encoding='utf-8'):
        """
        Try to decode html into unicode string from given encoding
        :param html:
        :param encoding:
        :return:
        """
        try:
            return html.decode(encoding=encoding, errors='strict')
        except UnicodeError:
            try:
                return html.decode(encoding='cp1251')
            except UnicodeError:
                try:
                    return html.decode(encoding='koi8_r')
                except UnicodeError:
                    return html.decode(encoding=encoding, errors='replace')


class UrlContentGetterException(Exception):
    pass