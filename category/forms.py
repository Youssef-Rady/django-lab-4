from django import forms
from category.models import Category

class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

