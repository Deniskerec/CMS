from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Records


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
                             required=True)
    first_name = forms.CharField(label="", max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
                                 required=True)
    last_name = forms.CharField(label="", max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
                                required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = ('<span class="form-text text-muted"><small>Required. 150 characters or '
                                             'fewer. Letters, digits and @/./+/-/_ only.</small></span>')

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = ('<ul class="form-text text-muted small"><li>Your password can\'t be too '
                                              'similar to your other personal information.</li><li>Your password must '
                                              'contain at least 8 characters.</li><li>Your password can\'t be a '
                                              'commonly used password.</li><li>Your password can\'t be entirely '
                                              'numeric.</li></ul>')

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = ('<span class="form-text text-muted"><small>Enter the same password as '
                                              'before, for verification.</small></span>')


### Create  Add Record form ( Montlhy) ###
class AddRecordForm(forms.ModelForm):
    month = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Month'
        }),
        label=""
    )
    year = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Year'
        }),
        label=""
    )
    timestamp = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Timestamp'
        }),
        label=""
    )
    amount = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Amount'
        }),
        label=""
    )
    amount_in_cents = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Amount in Cents'
        }),
        label=""
    )
    net_in_cents = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Net in Cents'
        }),
        label=""
    )
    km_food_in_cents = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'KM | Food in Cents'
        }),
        label=""
    )
    ljublana_trips = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ljubljana Trips Count'
        }),
        label=""
    )
    est_trips = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Estimated Trips Count '
        }),
        label=""
    )

    class Meta:
        model = Records
        fields = ['month', 'year', 'timestamp', 'amount', 'amount_in_cents', 'net_in_cents', 'km_food_in_cents',
                  'ljublana_trips', 'est_trips']

