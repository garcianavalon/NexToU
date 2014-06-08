from django.shortcuts import render
from userena.views import ProfileListView
from activitynetwork.models import talents
# Create your views here.
class CustomProfileListView (ProfileListView):
	template_name = "profile_list.html"
	def get_context_data(self, **kwargs):
		context = super(CustomProfileListView, self).get_context_data(**kwargs)
		context['talents_list'] = talents.objects.all()
		return context