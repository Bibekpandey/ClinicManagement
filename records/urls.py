from django.conf.urls import patterns, include, url
from records import views
from records.views import Index, Receptionist

urlpatterns = patterns('',
    # Examples:
     url(r'^$', Index.as_view(), name='index'),
	 url(r'^reception/', Receptionist.as_view(), name='reception'),
    # url(r'^blog/', include('blog.urls')),

)
