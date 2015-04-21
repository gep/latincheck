__author__ = 'gep'

from django.views.generic.edit import BaseFormView
from django.http.response import JsonResponse
from mainapp.forms import ProcessDomainForm
import django.utils.html as html


class ProcessUrlFormView(BaseFormView):
    form_class = ProcessDomainForm
    content_type = None

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates a blank version of the form.
        """
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        return self.get(request, *args, **kwargs)

    def form_invalid(self, form):
        return JsonResponse({'errors': form.errors})

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # HttpRes
        # return HttpResponseRedirect(self.get_success_url())

        result = form.verify_url()

        return JsonResponse(
            {
                'errors': result['errors'],
                'occurrences': result['occurrences'],
                'html': html.conditional_escape(result['content'])
                # 'html': result['content']
            }
        )

    def get_form_kwargs(self):
        """
        Returns the keyword arguments for instantiating the form.
        """
        kwargs = {
            'initial': self.get_initial(),
            'prefix': self.get_prefix(),
        }

        if self.request.method in ('GET', 'POST'):
            kwargs.update({
                'data': self.request.GET,
                'files': self.request.FILES,
            })
        return kwargs