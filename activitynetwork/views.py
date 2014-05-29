from django.views.generic import CreateView
from activitynetwork.models import Example

class ExampleView(CreateView):
    model = Example
    fields = ['name']
    template_name = "activitynetwork/example_create_form.html"