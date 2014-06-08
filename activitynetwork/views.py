from django.views.generic import CreateView, ListView
from django.contrib.auth.models import User
from activitynetwork.models import Activity, Category
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
    def get_context_data(self, **kwargs):
        context = super(ActivityListView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context

class ActivityFollowingListView(ListView):
    model = Activity
    template_name = "activity_following_list.html"
    def get_context_data(self, **kwargs):
        context = super(ActivityFollowingListView, self).get_context_data(**kwargs)
        user = User.objects.get(username=self.kwargs['username'])
        context['user'] = user
        context['activity_list'] = Activity.objects.filter(followed_activites__id=user.volunteer_profile.id)
        return context

class ActivityHostingListView(ListView):
    model = Activity
    template_name = "activity_hosting_list.html"
    def get_context_data(self, **kwargs):
        context = super(ActivityHostingListView, self).get_context_data(**kwargs)
        user_name = self.kwargs['username']
        context['user'] = User.objects.get(username=user_name)
        context['activity_list'] = Activity.objects.filter(act_holder=context['user'].id)
        return context
