from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from views import IndexView
from django.contrib.auth.decorators import login_required
from accounts.forms import CustomSignupForm, CustomSigninForm, CustomEditProfileForm, CustomMessageForm
from accounts.views import CustomProfileListView
from userena import views as userena_views
from userena.contrib.umessages import views as messages_views
urlpatterns = patterns('',

    url(r'^$', IndexView.as_view(), name='landing'), #Index, first page
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/$', CustomProfileListView.as_view()),
    url(r'^accounts/signup/$',
        userena_views.signup,
        {'signup_form': CustomSignupForm}),
    url(r'^accounts/signin/$',
        userena_views.signin,
        {'auth_form': CustomSigninForm}),
    url(r'^accounts/(?P<username>[\.\w-]+)/edit/$', userena_views.profile_edit,
        {'edit_profile_form': CustomEditProfileForm}),
    url(r'^accounts/(?P<username>[\.\w-]+)/profile_detail/$', userena_views.profile_detail),
    url(r'^accounts/', include('userena.urls')),
    url(r'^activities/', include('activitynetwork.urls',namespace="activities")),
    url(r'^messages/compose/(?P<recipients>[\+\.\w]+)/$',
        messages_views.message_compose,
        {'compose_form': CustomMessageForm}),
    url(r'^messages/', include('userena.contrib.umessages.urls')),
)
