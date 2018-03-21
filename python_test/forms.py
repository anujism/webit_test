from django import forms

from .models import Client


class BootstrapForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BootstrapForm, self).__init__(*args, **kwargs)

        for key in self.fields:
            self.fields[key].widget.attrs['class'] = 'form-control'


class ClientSearchForm(BootstrapForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone', 'suburb']

    def __init__(self, *args, **kwargs):
        super(ClientSearchForm, self).__init__(*args, **kwargs)

        for key in self.fields:
            self.fields[key].required = False


class ClientForm(BootstrapForm):
    class Meta:
        model = Client
        fields = '__all__'
