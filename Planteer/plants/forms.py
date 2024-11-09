from django import forms
from .models import Plant

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = "__all__" 
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'about': forms.Textarea(attrs={'class': 'form-control'}),
            'used_for': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'native_to': forms.SelectMultiple(attrs={'class': 'form-control select2-multi'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'is_edible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }