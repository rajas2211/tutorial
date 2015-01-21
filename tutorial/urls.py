from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tutorial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
<<<<<<< HEAD
    # Expected from tutorial
    # urlpatterns =[ <code below> ]
    url(r'^', include ('snippets.urls')),
)
=======
)
>>>>>>> 06d66608c253f6cfc500b0b5184a1c9597ef06f1
