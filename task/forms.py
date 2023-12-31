from django import forms
from .models import TaskModel

class TaskForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Your Email')
    message = forms.CharField(widget=forms.Textarea, label='Your Message')
    age = forms.IntegerField(min_value=0, label='Your Age')

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age and age < 18:
            raise forms.ValidationError('You must be at least 18 years old.')
        return age