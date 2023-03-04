from django import forms
from .models import Review
from django.forms import ModelForm

# class ReviewForm(forms.Form):
#     first_name = forms.CharField(label="First Name", max_length=100)
#     last_name = forms.CharField(label="Last Name", max_length=100)
#     email = forms.CharField(label="Email")
#     review = forms.CharField(label="Please write your review here", 
#                              widget=forms.Textarea())

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['first_name', 'last_name', 'stars']
        