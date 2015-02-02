from django.contrib import admin
from django.conf.urls import patterns, include, url

admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
     url(r'^$', include('records.urls')),
	 url(r'^index/', include('records.urls')),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
