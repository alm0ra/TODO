from django.urls import path
from . import views


urlpatterns = [

    path('/', views.ApiOverview, name="api-overview"),
    path('/task-list/', views.TaskList, name = "task-list"),
    path('/done-list/', views.DoneList, name = "done-list"),
    path('/task-detail/<str:pk>', views.TaskDetail, name = "task-detail"),
    path('/task-create/', views.CreateTask, name="task-create"),
    path('/task-update/<str:pk>', views.TaskUpdate, name="task-update"),
    path('/task-delete/<str:pk>', views.TaskDelete, name="task-delete"),
    path('/move-done/<str:pk>', views.MoveToDone, name="make-done"),
    path('/move-task/<str:pk>', views.MoveToTask, name="make-undone"),

]