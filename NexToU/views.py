from django.views.generic.base import TemplateView

class IndexView(TemplateView):
    template_name = "landing.html"

class TalentsView(TemplateView):
	template_name = "profile_list.html"