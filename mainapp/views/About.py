__author__ = 'gep'

from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        kwargs['active_tab'] = 'about'
        return super(AboutView, self).get_context_data(**kwargs)
