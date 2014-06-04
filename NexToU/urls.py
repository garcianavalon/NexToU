from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

#from emailcontactform import views
from activitynetwork import views as act_views

urlpatterns = patterns('',

    #url(r'^$', views.IndexView.as_view(), name='index'), #Index, first page
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('userena.urls')),
    url(r'^activities/listm',ActivityListView())

)
