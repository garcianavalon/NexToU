from emailcontactform.forms import BasicContactForm,HiddenEmailContactForm
from django.views.generic.edit import FormView

class BasicContactView(FormView):
    template_name = 'contact.html'
    form_class = BasicContactForm
    success_url = 'TODO'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super(BasicContactView, self).form_valid(form)


'''class HiddenEmailContactView(FormView):
    #TODO probably this class can inherit from the BasicContactView
    template_name = 'contact.html'
    form_class = HiddenEmailContactForm
    success_url = 'TODO'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super(HiddenEmailContactView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(HiddenEmailContactView, self).get_context_data(**kwargs)
        #TODO get the user email to be contacted
        context['form'] = HiddenEmailContactForm()
        return context
'''