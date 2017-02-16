from django import forms


class FieldForm(forms.Form):
    fields = forms.CharField(label='field', max_length=100)
