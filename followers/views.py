from followers.models import Follower
from .serializers import FollowerSerializer
from rest_framework.generics import CreateAPIView

class FollowerView(CreateAPIView):
    model = Follower
    serializer_class = FollowerSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)