from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

#from emailcontactform import views
from activitynetwork import views as act_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'NexToU.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', views.IndexView.as_view(), name='index'), #Index, first page
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    #url(r'^volunteers/$', act_views.ExampleView.as_view()),
    url(r'^activities/create/$',act_views.ActivityCreateView.as_view()),
    url(r'^activities/list/$',act_views.ActivityListView.as_view()),
    url(r'^needs/create/$',act_views.NeedCreateView.as_view()),
    #url(r'^contact/', views.BasicContactView.as_view(),name='contact'),
)
