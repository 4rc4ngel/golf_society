from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from golf_app.models import Player,Post,Comment
from golf_app.forms import PlayersForm,PostForm,CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import(TemplateView,ListView,DeleteView,
                                DetailView,CreateView,UpdateView)


# Create your views here.

class IndexView(ListView):
  template_name = 'index.html'
  model = Player

# Players Views

class PlayersListView(ListView):
  model = Player 

  def get_queryset(self):
   return Player.objects.all().order_by('total_score')
  
class PlayersDetailView(DetailView):
  model = Player
 
  def get_queryset(self):
   return Player.objects.all().order_by('-total_score')
# Player CRUD Views

class CreatePlayerView(LoginRequiredMixin,CreateView):
  login_url = '/login/'
  redirect_field_name = 'golf_app/player_detail.html/'
  form_class = PlayersForm
  model = Player

class PlayerUpdateView(LoginRequiredMixin,UpdateView):
  login_url = '/login/'
  redirect_field_name = 'golf_app/player_detail.html/'
  form_class = PlayersForm
  model = Player

class PlayerDeleteView(LoginRequiredMixin,DeleteView):
  model = Player
  success_url = reverse_lazy('player_list')

######################################################

# Post Views

class PostListView(ListView):
  model = Post

class PostDetailView(DetailView):
  mode = Post

  def get_queryset(self):
    return Post.objects.all().order_by('-date_published')

class CreatePostView(LoginRequiredMixin,CreateView):
  login_url = '/login/'
  redirect_field_name = 'golf_app/post_list.html'
  form_class = PostForm
  model = Post

class PostUpdateView(LoginRequiredMixin,UpdateView):
  login_url = '/login/'
  redirect_field_name = 'golf_app/post_list.html'
  form_class = PostForm
  model = Post

class PostDeleteView(LoginRequiredMixin,DeleteView):
  model = Post
  success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin,ListView):
  login_url = '/login/'
  redirect_field_name = 'golf_app/post_list.html'
  model = Post

  def get_queryset(self):
    return Post.objects.filter(date_published__isnull=True).order_by('date_created')

#####################################################

# Comment functions

@login_required
def post_publish(request,pk):
  post = get_object_or_404(Post,pk=pk)
  post.publish()
  return redirect('post_detail', pk=pk)

def add_comment_to_post(request,pk):
  post = get_object_or_404(Post,pk=pk)
  if request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_valid():
      comment = form.save(commit=False)
      comment.post = post
      comment.save()
      return redirect('post_detail', pk=post.pk)
  else:
    form = CommentForm()
  return render(request, 'golf_app/comment_form.html', {'form':form})

@login_required
def approve_comment(request,pk):
  comment = get_object_or_404(Comment,pk=pk)
  comment.approve()
  return redirect('post_detail',pk=comment.post.pk)

 
@login_required
def remove_comment(request,pk):
  comment = get_object_or_404(Comment, pk=pk)
  post_pk = comment.post.pk
  comment.delete()
  return redirect('post_detail', pk=post_pk)