from django.urls import path
from . import views


urlpatterns = [

    path('/', views.ApiOverview, name="api-overview"),
    path('/task-list/', views.TaskList.as_view(), name = "task-list"),
    path('/done-list/', views.DoneList.as_view(), name = "done-list"),
    path('/task-detail/<str:pk>', views.TaskDetail.as_view(), name = "task-detail"),
    path('/task-create/', views.CreateTask.as_view(), name="task-create"),

]