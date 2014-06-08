from django.forms import ModelForm
from models import Activity

class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        #fields = ['name']
    def __init__(self, *args, **kwargs):
        super(ActivityForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs.update({'class' : 'form-control'})