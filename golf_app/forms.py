from django import forms
from golf_app.models import Player, Post, Comment

# Players form

class PlayersForm(forms.ModelForm):

  class Meta():
    model = Player
    fields = ('name', 'full_name', 'nickname', 'handicap', 'current_score',
              'total_score', 'nearest_pin', 'birdies', 'eagles')

    widgets = {
            
            'full_name':forms.TextInput(attrs={'class':'form-control'}),
            'nickname':forms.TextInput(attrs={'class':'form-control'}),
            'handicap':forms.NumberInput(attrs={'class':'form-control'}),
            'current_score':forms.NumberInput(attrs={'class':'form-control'}),
            'total_score':forms.NumberInput(attrs={'class':'form-control'}),
            'nearest_pin':forms.NumberInput(attrs={'class':'form-control'}),
            'birdies':forms.NumberInput(attrs={'class':'form-control'}),
            'eagles':forms.NumberInput(attrs={'class':'form-control'})
    }

class PostForm(forms.ModelForm):

  class Meta():
    model = Post
    fields = ('author', 'title', 'text')

    widgets = {
            
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'text':forms.Textarea(attrs={'class':'form-control'}),
            
    }
class CommentForm(forms.ModelForm):

  class Meta():
    model = Comment
    fields = ('author', 'text')

    widgets = {
            'author':forms.TextInput(attrs={'class':'form-control'}),
            'text':forms.Textarea(attrs={'class':'form-control'}),
            
    }