from django import forms
from tuites.models import Tuite


class PostTuiteForm(forms.ModelForm):
    class Meta:
        model = Tuite
        fields = ('content', 'author')

    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].initial = self.initial['user'].id
        self.fields['author'].widget = forms.HiddenInput()
        self.fields['content'].help_text='Digite o que você está pensando'
        self.fields['content'].widget = forms.TextInput(attrs={'class': 'post-tuite-input'})
    
    
    def clean(self):
        cleaned_data = super().clean()
        content = self.cleaned_data.get('content')
        if 'Guga' in content:
            raise forms.ValidationError('acertou')
        return cleaned_data
