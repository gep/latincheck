__author__ = 'andrewsemikov'
import urllib2


class UrlContentGetter(object):

    def __init__(self):
        self.timeout = 5 # seconds
        self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:37.0) Gecko/20100101 Firefox/37.0'

    def get_contents(self, url):
        request = urllib2.Request(url)

        # if 'POST' == method and isinstance(params, dict) and len(params) > 0:
        #     request.add_data(self._build_query_for_server_recursively(params))

        # print 'Request method after data :', request.get_method()
        request.add_header('User-agent', self.user_agent)

        response = urllib2.urlopen(request, timeout=self.timeout)
        response_actual_string = response.read()
        response.close()
        #
        return response_actual_string
