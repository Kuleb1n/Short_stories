from django.forms import ModelForm, Textarea, TextInput
from .models import Story


class StoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Выберите категорию:'

    class Meta:
        model = Story
        fields = ['title', 'content', 'category']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control'}),
            'content': Textarea(attrs={
                'col': 60, 'row': 5}),
        }
