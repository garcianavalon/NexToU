from django.shortcuts import render

# Create your views here.
class TalentsView(ListView):
	model = VolunteerProfile
	template_name = "profile_list.html"