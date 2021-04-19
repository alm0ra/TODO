from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import (api_view, authentication_classes,
                                       permission_classes)
from rest_framework.generics import (CreateAPIView, ListAPIView,
                                     RetrieveUpdateDestroyAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Tasks
from .serializers import TaskSerializer


@api_view(['GET'])
def ApiOverview(request):

    api_urls = {
        'Task List':'/task-list/',
        'Done List':'/done-list/',
        'Detail View With UPDATE,DELETE':'/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Move To Done(Make a Task Done)':'/move-done/<str:pk>/',
        'Move To Tasks(Make a Task undone)':'/move-task/<str:pk>/',

    }
    return Response(api_urls)

class TaskList(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Tasks.objects.filter(status=False)
    serializer_class = TaskSerializer

class DoneList(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Tasks.objects.filter(status=True)
    serializer_class = TaskSerializer

class CreateTask(CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer

class TaskDetail(RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def MoveToDone(request, pk):
    tasks = Task.objects.get(pk=pk)
    tasks.status = True
    tasks.save()
    return Response("Moved To Done List Success")

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def MoveToTask(request, pk):
    tasks = Task.objects.get(pk=pk)
    tasks.status = False
    tasks.save()
    return Response("Moved To Task List Success")
