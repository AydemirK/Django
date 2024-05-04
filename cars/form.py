from django import forms
from cars.models import Post, Review, Tag


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'brand', 'model', 'price', 'year_of_issue', 'img']
        
        
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']



class SearchForm(forms.Form):
    search = forms.CharField(
        required=False,
        max_length=100,
        min_length=3,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Поиск',
                'class': 'form-control'
            }
        )
    )
    tags = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

