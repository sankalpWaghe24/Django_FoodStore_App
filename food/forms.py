from django import forms
from .models import Food

#  ? Add Food Form


class FoodForm(forms.ModelForm):
    CHOICES = (
        ('Veg', 'veg'),
        ('Non-Veg', 'non-veg'))

    foodType = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES)

    foodDesc = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control my-2",
        "style": "width:450px; height:100px"}))

    foodTitle = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control my-2",
        "style": "width:450px; "}))

    class Meta:
        model = Food
        fields = '__all__'
        widgets = {
            'foodName': forms.TextInput(attrs={
                "class": "form-control my-2",
                "style": "width:450px; "
            }),
        }
