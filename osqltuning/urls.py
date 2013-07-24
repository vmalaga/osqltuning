from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'osqltuning.views.home', name='home'),
    url(r'^$', 'frontend.views.index_view', name='home'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^logout', 'frontend.views.logout_view'),
    url(r'^testview', 'frontend.views.test_view'),
    # url(r'^osqltuning/', include('osqltuning.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
