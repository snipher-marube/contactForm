# forms.py
from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    general_enquiry = forms.ChoiceField(
        choices=[('general', 'General Enquiry'), ('support', 'Support Enquiry')],
        widget=forms.RadioSelect,
        required=True
    )
    message = forms.CharField(widget=forms.Textarea, required=True)
    check = forms.BooleanField(required=True)
