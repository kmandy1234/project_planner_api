from django.contrib import admin

from . models import Board, Task, Team, User

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('board_id', 'name', 'desc', 'creation_time', 'president')
    readonly_fields = ('creation_time',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_id', 'title', 'desc', 'creation_time', 'status', 'team_id', 'board_id')
    readonly_fields = ('creation_time',)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_id', 'name', 'desc', 'admin')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'name', 'display_name','team_id', 'board_id')