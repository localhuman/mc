from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from portfolio import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.home),

    url(r'^contact/$', views.contact),
    url(r'^contact/thanks/$', views.contact_thanks),
    url(r'^terms/', views.terms),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),


)
