# tasks/forms.py
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']
        widgets = {'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'やることを入力…'})}

    def clean_title(self):
        title = (self.cleaned_data['title'] or '').strip()
        if not title:
            raise forms.ValidationError('やることを入力してください。')
        if len(title) > 120:
            raise forms.ValidationError('120文字以内で入力してください。')
        return title
