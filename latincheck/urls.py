from django.conf.urls import  url
# from django.conf.urls import handler404
# from django.contrib import admin
from mainapp.views import ProcessUrlFormView, IndexView, AboutView

urlpatterns = [
    # Examples:
    # url(r'^$', 'latincheck.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^validate', ProcessUrlFormView.as_view(), name='process_url'),
    url(r'^about$', AboutView.as_view(), name='about'),
    url(r'^$', IndexView.as_view(), name='home'),

]
