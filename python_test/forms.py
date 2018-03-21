from django import forms

from .models import Client
from django.utils.safestring import mark_safe

import string


def pretty_name(name):
    if not name:
        return ''
    return string.capwords(name.replace('_', ' '))


class BootstrapForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BootstrapForm, self).__init__(*args, **kwargs)
        self.stylize_fields()

    def stylize_fields(self):
        # Add classes for the HTML template in use
        for name, field in self.fields.items():

            if getattr(field, '_b3_stylized', False):
                continue

            field.widget.attrs['class'] = 'form-control'
            field.label = pretty_name(field.label or name)

            if field.required:
                field.widget.attrs['required'] = 'required'
                field.label = mark_safe('<span class="required">*</span> {}'.format(field.label))

            field._b3_stylized = True


class ClientSearchForm(BootstrapForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone', 'suburb']

    def __init__(self, *args, **kwargs):
        for key in self.base_fields:
            self.base_fields[key].required = False

        super(ClientSearchForm, self).__init__(*args, **kwargs)


class ClientForm(BootstrapForm):
    class Meta:
        model = Client
        fields = '__all__'
