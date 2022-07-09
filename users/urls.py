from django.urls import path
from users.views import CreateUserView

app_name = 'users'

urlpatterns = [
    path('user/registration/', CreateUserView.as_view())
]