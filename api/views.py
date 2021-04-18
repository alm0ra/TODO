from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.authentication import (BasicAuthentication,
                                           SessionAuthentication)
from rest_framework.decorators import (api_view, authentication_classes,
                                       permission_classes)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Tasks
from .serializers import TaskSerializer


@api_view(['GET'])
def ApiOverview(request):

    api_urls = {
        'Task List':'/task-list/',
        'Done List':'/done-list/',
        'Detail View':'/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/',
        'Move To Done(Make a Task Done)':'/move-done/<str:pk>/',
        'Move To Tasks(Make a Task undone)':'/move-task/<str:pk>/',

    }
    return Response(api_urls)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def TaskList(request):

    tasks = Tasks.objects.filter(status=False)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def DoneList(request):
    tasks = Tasks.objects.filter(status=True)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def TaskDetail(request, pk):
    tasks = Tasks.objects.get(pk=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def CreateTask(request):
    serializer = TaskSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def TaskUpdate(request, pk):
    tasks = Tasks.objects.get(pk=pk)
    serializer = TaskSerializer(instance=tasks,data = request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def TaskDelete(request, pk):
    tasks = Tasks.objects.get(pk=pk).delete()
    return Response("Delete SuccessFull")