from .serializers import PostSerializer 
from .models import Post
from rest_framework import viewsets

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    def get_queryset(self):
        user = self.request.user
        return Post.objects.exclude(author=user).order_by('created_at').reverse()[:10]
    
    