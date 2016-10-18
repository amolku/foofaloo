from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from foof.serializers import UserSerializer, GroupSerializer
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World")


# DRF for Users and Groups

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
