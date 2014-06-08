from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from views import IndexView
from activitynetwork import views as act_views
from accounts.forms import CustomSignupForm, CustomSigninForm
from userena import views as userena_views
urlpatterns = patterns('',

    url(r'^$', IndexView.as_view(), name='landing'), #Index, first page
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/signup/$',
        userena_views.signup,
        {'signup_form': CustomSignupForm}),
    url(r'^accounts/signin/$',
        userena_views.signin,
        {'auth_form': CustomSigninForm}),
    url(r'^accounts/', include('userena.urls')),
    url(r'^activities/create/$',act_views.ActivityCreateView.as_view()),
    url(r'^activities/list/$',act_views.ActivityListView.as_view()),
    url(r'^needs/create/$',act_views.NeedCreateView.as_view()),

)
