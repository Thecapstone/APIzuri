from rest_framework import generics
from .serializers import LinkSerializer
from .models import Link
from rest_framework.permissions import IsAdminUser


class PostListApi(generics.ListAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer
    permission_classes = [IsAdminUser]


class PostCreateApi(generics.CreateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer
    permission_classes = [IsAdminUser]


class PostDetailApi(generics.RetrieveAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer
    permission_classes = [IsAdminUser]


class PostUpdateApi(generics.UpdateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer
    permission_classes = [IsAdminUser]


class PostDeleteApi(generics.DestroyAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer
    permission_classes = [IsAdminUser]
