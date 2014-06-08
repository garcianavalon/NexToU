from django.views.generic import CreateView, ListView
from activitynetwork.models import Activity, Need
from activitynetwork.forms import ActivityForm

class ActivityCreateView(CreateView):
    model = Activity
    form_class = ActivityForm
    #fields = ['name']
    success_url = '/activities/list/'
    template_name = "activity_create.html"

    def form_valid(self, form):
        object = form.save(commit=False)
        object.act_holder = self.request.user
        object.save()
        return super(ActivityCreateView, self).form_valid(form)

class ActivityListView(ListView):
    model = Activity
    template_name = "activity_list.html"

class ActivityFollowingListView(ListView):
    model = Activity
    template_name = "activity_following_list.html"

class ActivityHostingListView(ListView):
    model = Activity
    template_name = "activity_hosting_list.html"
