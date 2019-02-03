from django import forms
# import forms from Django
from .models import Post
# import our model on post

class PostForm(forms.ModelForm): #type forms.ModelForm

  class Meta:
    model = Post #telll Django which model should be used
    fields = ('title', 'text',) # exposing only title and text and created date is automatically set along with author,
