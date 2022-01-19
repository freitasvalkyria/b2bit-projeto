from django.urls import include, path
from followers.views import FollowerView

app_name = 'followers'

urlpatterns = [
    path('api-auth/user/follow/', FollowerView.as_view())
]