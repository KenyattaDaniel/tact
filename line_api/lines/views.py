from django.contrib.auth.models import User

from rest_framework import permissions
from rest_framework import viewsets

from .models import Announcement, Event, Task
from .serializers import UserSerializer
from .serializers import AnnouncementSerializer, EventSerializer, TaskSerializer
from .permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Provides 'list' and 'detail' views of users.

    Authenticated users can see list, details of all active users.
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AnnouncementViewSet(viewsets.ModelViewSet):
    """
    Provides 'list', 'create', 'retrieve', 'update' and
    'destroy' actions for announcements.

    Authenticated users can see list, details of all created announcements.

    Authenticated users can create announcements, add them to
    owned lines and edit them.
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EventViewSet(viewsets.ModelViewSet):
    """
    Provides 'list', 'create', 'retrieve', 'update' and
    'destroy' actions for events.

    Authenticated users can see list, details of all created events.

    Authenticated users can create events, add them to
    owned lines and edit them.
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskViewSet(viewsets.ModelViewSet):
    """
    Provides 'list', 'create', 'retrieve', 'update' and
    'destroy' actions for tasks.

    Authenticated users can see list, details of all created tasks.

    Authenticated users can create tasks, add them to
    owned lines and edit them.
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
