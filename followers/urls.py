from django.urls import path
from followers.views import FollowerView

app_name = 'followers'

urlpatterns = [
    path('user/follow/', FollowerView.as_view())
]