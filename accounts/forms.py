from userena.forms import SignupForm, AuthenticationForm, identification_field_factory, USERNAME_RE
from django import forms
from django.utils.translation import ugettext as _
#custom forms with css and widgets
custom_attrs_dict = {"class":"required input-block-level"}
class CustomSignupForm(SignupForm):
    username = forms.RegexField(regex=USERNAME_RE,
                                max_length=30,
                                widget=forms.TextInput(attrs=custom_attrs_dict),
                                label=_("Username"),
                                error_messages={'invalid': _('Username must contain only letters, numbers, dots and underscores.')})
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(custom_attrs_dict,
                                                               maxlength=75)),
                             label=_("Email address"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=custom_attrs_dict,
                                                           render_value=False),
                                label=_("Create password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=custom_attrs_dict,
                                                           render_value=False),
                                label=_("Repeat password"))

class CustomSigninForm(AuthenticationForm):
    identification = identification_field_factory(_(u"Email or username"),
                                                  _(u"Either supply us with your email or username."))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput(attrs=custom_attrs_dict, render_value=False))