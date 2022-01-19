from rest_framework import routers
from posts.views import PostViewSet
from django.contrib import admin
from django.urls import path, include
from users.views import CreateUserView

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('followers.urls')),
    path ('api-auth/',  include ('rest_framework.urls')),
    path('api-auth/registration/', CreateUserView.as_view()), 
]