from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [

    path('/', views.ApiOverview, name="api-overview"),
    path('/task-list/', views.TaskList.as_view(), name = "task-list"),
    path('/done-list/', views.DoneList.as_view(), name = "done-list"),
    path('/task-detail/<str:pk>', views.TaskDetail.as_view(), name = "task-detail"),
    path('/task-create/', views.CreateTask.as_view(), name="task-create"),
    path('/move-done/<str:pk>', views.MoveToDone, name = "move-done"),
    path('/move-task/<str:pk>', views.MoveToTask, name = "move-task"),
    path('/api-token-auth/', obtain_auth_token, name="token-generator")

]