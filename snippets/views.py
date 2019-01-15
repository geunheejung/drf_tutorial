from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions
from django.contrib.auth.models import User


# 👇 제네릭 클래스 기반 뷰
class SnippetList(generics.ListCreateAPIView):
    """
    코드 조각을 모두 보여주거나 새 코드 조각을 만듭니다.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        """
        인스턴스를 저장하는 과정을 조정하며, 요청이나 요청URL에서 정보를 가져와 원하는 대로 다룰 수 있다.
        create() 메서드는 검증한 요청 데이터에 더하여 'owner' 필드도 전달한다.
        :param serializer:
        :return:
        """
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

