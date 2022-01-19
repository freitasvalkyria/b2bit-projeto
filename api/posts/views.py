from rest_framework.response import Response
from .serializers import PostSerializer 
from .models import Post
from rest_framework import viewsets, status
from rest_framework.decorators import action


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    def get_queryset(self):
        user = self.request.user
        return Post.objects.exclude(author=user).order_by('created_at').reverse()[:10]

    @action(methods=['get'], detail=False,url_path='followers', url_name='followers')
    def only_followers(self, request):
        logged_user = self.request.user
        posts = Post.objects.exclude(author=logged_user).extra(
            tables = ['followers_follower'], 
            where=['posts_post.author_id=followers_follower.following_user_id']
        ).values().distinct()
        return Response(posts,status=status.HTTP_200_OK)