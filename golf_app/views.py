from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from golf_app.models import Players,Post,Comment
from golf_app.forms import PlayersForm,PostForm,CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import(TemplateView,ListView,DeleteView,
                                DetailView,CreateView,UpdateView)


# Create your views here.


# Players Views

class PlayersListView(ListView):
  model = Players

  def get_queryset(self):
    return Players.objects.all()order.by('-total_score')

class PlayersDetailView(DetailView):
  model = Players

# Player CRUD Views

class CreatePlayerView(LoginRequiredMixin,CreateView):
  login_url = '/login/'
  redirect_field_name = 'golf_app/player_detail.html'
  form_class = PlayersForm
  model = Players

class PlayerUpdateView(LoginRequiredMixin,UpdateView):
  login_url = '/login/'
  redirect_field_name = 'golf_app/player_detail.html'
  form_class = PlayersForm
  model = Players

class PlayerDeleteView(LoginRequiredMixin,DeleteView):
  model = Players
  success_url = reverse_lazy('players_list')

######################################################

# Post Views

class PostListView(ListView):
  model = Post

  def get_queryset(self):
    return Post.objects.filter(date_published__lte=timezone.now().order.by('-date_published'))

class PostDetailView(DeleteView):
  mode = Post

class CreatePostView(LoginRequiredMixin,CreateView):
  login_url = '/login/'
  redirect_field_name = 'golf_app/post_detail.html'
  form_class = PostForm
  model = Post

class PostUpdateView(LoginRequiredMixin,UpdateView):
  login_url = '/login/'
  redirect_field_name = 'golf_app/post_detail.html'
  form_class = PostForm
  model = Post

class PostDeleteView(LoginRequiredMixin,DeleteView):
  mode = Post
  success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin,ListView):
  login_url = '/login/'
  redirect_field_name = 'golf_app/post_list.html'
  model = Post

  def get_queryset(self):
    return Post.objects.filter(date_published__isnull=True).order.by('date_created')

#####################################################

# Comment functions

@login_required
def post_publish(request,pk):
  post = get_object_or_404(Post,pk=pk)
  post.publish()
  return redirect('post_detail', pk=pk)

@login_required
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
 def comment_remove(request,pk):
   comment = get_object_or_404(Comment, pk=pk)
   post_pk = comment.post.pk
   comment.delete()
   return redirect('post_detail', pk=post.pk)