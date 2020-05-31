from django.conf.urls import url
from golf_app import views

urlpatterns = [
  
  # player urls
  url(r'^players/$',views.PlayersListView.as_view(),name='player_list'),
  url(r'^players/(?P<pk>\d+)$',views.PlayersDetailView.as_view(),name='player_detail'),
  url(r'^players/new/$',views.CreatePlayerView.as_view(),name='new_player'),
  url(r'^players/(?P<pk>\d+)/edit/$',views.PlayerUpdateView.as_view(),name='edit_player'),
  url(r'^players/(?P<pk>\d+)/remove/$',views.PlayerDeleteView.as_view(),name='remove_player'),
  # post urls
  url(r'^post/$',views.PostListView.as_view(),name='post_list'),
  url(r'^post/(?P<pk>\d+)$',views.PostDetailView.as_view(),name='post_detail'),
  url(r'^post/new/$',views.CreatePostView.as_view(),name='new_post'),
  url(r'^post/(?P<pk>\d+)/edit/$',views.PostUpdateView.as_view(),name='edit_post'),
  url(r'^post/(?P<pk>\d+)/remove/$',views.PostDeleteView.as_view(),name='remove_post'),
  url(r'^drafts/$',views.DraftListView.as_view(),name='post_draft'),
  # Comments urls
  url(r'^post/(?P<pk>\d+)/comment/$',views.add_comment_to_post,name='add_comment_to_post'),
  url(r'^comment/(?P<pk>\d+)/approve/$',views.approve_comment,name='approve_comment'),
  url(r'^comment/(?P<pk>\d+)/remove/$',views.remove_comment,name='remove_comment'),
  url(r'^comment/(?P<pk>\d+)/publish/$',views.post_publish,name='post_publish')
]