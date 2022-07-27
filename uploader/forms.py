from django import forms
from .models import UserFiles
from django.core.validators import FileExtensionValidator

class UploadForm(forms.ModelForm):
    filename = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter name of your file...'}), label='')
    ufile = forms.FileField(widget=forms.FileInput(), label='', validators=[FileExtensionValidator(['doc', 'docx', 'pdf'])], help_text='Supported file formats: .doc, .docx, .pdf')
    
    class Meta:
        model = UserFiles
        fields = ['ufile', 'filename']
