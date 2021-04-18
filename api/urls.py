from django.urls import path
from . import views


urlpatterns = [

    path('/', views.ApiOverview, name="api-overview"),
    path('/task-list/', views.TaskList, name = "task-list"),
    path('/done-list/', views.DoneList, name = "done-list"),

]