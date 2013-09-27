__author__ = 'thomassaunders'


from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, label='Subject:')
    email = forms.EmailField(required=False, label='Your email address:')
    message = forms.CharField(widget=forms.Textarea, label='Message:')

