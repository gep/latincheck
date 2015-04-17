from django.conf.urls import include, url
# from django.contrib import admin
from mainapp.views import ProcessDomainFormView

urlpatterns = [
    # Examples:
    # url(r'^$', 'latincheck.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^validate', ProcessDomainFormView.as_view(), name='process_url'),
]
