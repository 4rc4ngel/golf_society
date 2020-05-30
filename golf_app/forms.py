from django import forms
from golf_app.models import Players, Post, Comment

# Players form

class PlayersForm(forms.ModelForm):

  class Meta():
    model = Players
    fields = ('name', 'nickname', 'handicap', 'current_score',
              'total_score', 'nearest_pin', 'birdies', 'eagles')

class PostForm(forms.ModelForm):

  class Meta():
    model = Post
    fields = ('author', 'title', 'text')

class CommentForm(forms.ModelForm):

  class Meta():
    model = Comment
    fields = ('author', 'text')
