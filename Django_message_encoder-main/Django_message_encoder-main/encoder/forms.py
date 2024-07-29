# encoder/forms.py

from django import forms

class EncodeMessageForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea, label="Message")
    day_type = forms.ChoiceField(choices=[('odd', 'Odd Day'), ('even', 'Even Day')], label="Day Type")
