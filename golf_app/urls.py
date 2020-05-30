from django.conf.urls import url
from golf_app import views

urlpatterns = [
  # player urls
  url(r'^$',views.PlayersListView.as_view(),name='player_list'),
  url(r'^players/(?P<pk>\d+)$',views.PlayerDetailView.as_view(),name='player_detail'),
  url(r'^players/new/$',views.CreatePlayerView.as_view(),name='new_player'),
  url(r'^players/(?P<pk>\d+)/edit/$',views.PlayerUpdateView.as_view(),name='player_update')
  url(r'^players/(?P<pk>\d+)/remove/$',views.PlayerDeleteView.as_view(),name='remove_player')
  # post urls
  url(r'^$',views.PostListView.as_view(),name='post_list'),
  url(r(r'^post/(?P<pk>\d+)$'),views.PostDetailView.as_view(),name='post_detail'),
  url(r'^post/new/$',views.CreatePostView.as_view(),name='new_post'),
  url(r'^post/(?P<pk>\d+)/edit/$',views.PostUpdateView.as_view(),name='edit_post'),
  url(r'^post/(?P<pk>\d+)/remove/$',views.PostDeleteView.as_view(),name='remove_post'),
  url(r'^drafts/$',views.DraftListView.as_view(),name='draft_list'),
  # Comments urls
  url(r'^post/(?P<pk>\d+)/comment/$',views.add_comment_to_post,name='add_comment_to_post'),
  url(r'^comment/(?P<pk>\d+)/approve/$',views.comment_approve,name='comment_approve'),
  url(r'^comment/(?P<pk>\d+)/remove/$',views.comment_remove,name='comment_remove'),
  url(r'^comment/(?P<pk>\d+)/publish/$',views.post_publish,name='post_publish')
]