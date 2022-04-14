from django.db import models

# Create your models here.

class Board(models.Model):
    board_id = models.BigAutoField(primary_key= True)
    name = models.CharField(max_length=64, unique=True)
    desc = models.CharField(max_length=128)
    creation_time = models.DateTimeField(auto_now_add=True)
    president = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    class Status(models.IntegerChoices):
        OPEN = 1
        IN_PROGRESS = 2 
        COMPLETE = 3
        CLOSE = 4

    task_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64, unique=True)
    desc = models.CharField(max_length=128)
    creation_time = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=Status.choices, default= 0)
    team_id = models.ForeignKey('Team', on_delete=models.SET_NULL, null=True, blank=True)
    board_id = models.ForeignKey('Board', on_delete=models.CASCADE, )

    def __str__(self):
        return self.title

class Team(models.Model):
    team_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=64, unique=True)
    desc = models.CharField(max_length=128)
    admin = models.ForeignKey('User',on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=64, unique=True)
    display_name = models.CharField(max_length=64)
    team_id = models.ForeignKey('Team', on_delete=models.SET_NULL, null=True, blank=True)
    board_id = models.ForeignKey('Board', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


