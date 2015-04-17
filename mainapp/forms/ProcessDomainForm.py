__author__ = 'andrewsemikov'

from django import forms


class ProcessDomainForm(forms.Form):
    url = forms.URLField(required=True)
