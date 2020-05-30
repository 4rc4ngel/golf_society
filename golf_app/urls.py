from django.conf.urls import url
from golf_app import views

urlpatterns = [
  url(r'^$',views.PlayersListView.as_view(),name='player_list')
]