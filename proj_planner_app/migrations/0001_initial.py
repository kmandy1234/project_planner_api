# Generated by Django 3.2.12 on 2022-04-03 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('board_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('desc', models.CharField(max_length=128)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('team_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('desc', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('display_name', models.CharField(max_length=64)),
                ('team_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='proj_planner_app.team')),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='proj_planner_app.user'),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=64, unique=True)),
                ('desc', models.CharField(max_length=128)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(1, 'Open'), (2, 'In Progress'), (3, 'Complete'), (4, 'Close')], default=0)),
                ('board_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proj_planner_app.board')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='proj_planner_app.team')),
            ],
        ),
        migrations.AddField(
            model_name='board',
            name='team_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='proj_planner_app.team'),
        ),
    ]