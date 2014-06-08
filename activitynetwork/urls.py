from django.conf.urls import patterns, url

from activitynetwork import views

urlpatterns = patterns('',
    url(r'^create/$',views.ActivityCreateView.as_view(), name='create'),
    url(r'^list/$',views.ActivityListView.as_view(), name='list'),
)


