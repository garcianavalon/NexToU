from django import forms

class BasicContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass #TODO


'''class HiddenEmailContactForm(BasicContactForm):
    email_to = forms.CharField(max_length=30,widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        if 'email_to' in kwargs:
            email_to_address = kwargs.pop('email_to') #before calling super or we have an error
        else:
            raise ValueError("we need an email addres!")
        super(BasicContactForm, self).__init__(*args, **kwargs)
        self.fields['email_to'].initial = email_to_address
'''