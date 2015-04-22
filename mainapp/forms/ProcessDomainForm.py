from latinverify import UrlContentGetter, HtmlVerify
from latinverify.UrlContentGetter import UrlContentGetterException

__author__ = 'andrewsemikov'

from django import forms


class ProcessDomainForm(forms.Form):
    url = forms.URLField(required=True)
    return_contents = forms.BooleanField(required=False)

    def verify_url(self):
        contents_getter = UrlContentGetter()
        html_verificator = HtmlVerify()

        try:
            content = contents_getter.get_contents(self.clean().get('url'))
            occurrences = html_verificator.search(content)
        except UrlContentGetterException, e:
            return {'errors': {'ContentError': e.message}, 'occurrences': {}, 'content': ''}
        except UnicodeError, e:
            return {'errors': {'DecodeError': e.message}, 'occurrences': {}, 'content': ''}

        return {
            'errors': {},
            'occurrences': occurrences,
            'content': (self.clean().get('return_contents') and [content] or [''])[0]
        }