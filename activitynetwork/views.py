from django.views.generic import CreateView, ListView
from activitynetwork.models import Activity, Need
from activitynetwork.forms import ActivityForm

class ActivityCreateView(CreateView):
    model = Activity
    form_class = ActivityForm
    #fields = ['name']
    success_url = '/'
    template_name = "activity_create.html"

class ActivityListView(ListView):
    model = Activity
    template_name = "activitylist.html"

class NeedCreateView(CreateView):
    model = Need
    success_url = '/needs/create/'
    #fields = ['name']
    template_name = "activitynetwork/example_create_form.html"