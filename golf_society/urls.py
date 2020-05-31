"""golf_society URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from golf_app import Home

urlpatterns = [
    
    url(r'^$', Home.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'accounts/login/$',views.login,name='login'),
    url(r'accounts/logout/$',views.logout,name='logout',kwargs={'next_page':'/'}),
    url(r'^index/$',views.IndexListView.as_view(),name='index'),
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
