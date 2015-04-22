__author__ = 'gep'

from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        kwargs['active_tab'] = 'index'
        kwargs['url'] = self.request.GET.get('url')
        return super(IndexView, self).get_context_data(**kwargs)
