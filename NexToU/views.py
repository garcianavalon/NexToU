from django.views.generic.base import TemplateView
from accounts.models import VolunteerProfile
class IndexView(TemplateView):
    template_name = "landing.html"



