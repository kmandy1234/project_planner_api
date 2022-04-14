from django import urls
from django.urls import path
from . import views

urlpatterns = [
    path('boards', views.BoardList.as_view()),
    path('boards/<int:board_id>', views.BoardDetail.as_view()),
    path('boards/<int:board_id>/tasks', views.BoardsTaskList.as_view()),
    path('boards/<int:board_id>/tasks/<int:task_id>', views.BoardsTaskDetail.as_view()),
    path('teams/', views.TeamList.as_view()),
    path('teams/<int:team_id>', views.TeamDetail.as_view()),
    path('teams/<int:team_id>/users', views.TeamUserList.as_view()),
    path('teams/<int:team_id>/users/<int:user_id>', views.TeamUserDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:user_id>', views.UserDetail.as_view())
]
