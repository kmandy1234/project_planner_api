## project_planner_api
* This is project management API created for practise purpose. It has 4 models - Board, Team, Users, and Tasks.
* Board is the main managing body. It includes tasks under it, which is assigned to a single team to complete it.
* Tasks status can be - OPEN, IN_PROGRESS, COMPLETE, CLOSE. Each task will be given to a team to complete it.
* Team can be composed of any no of users and will work under a team leader. A single team can be assigned a single task at any given time.
* Users can be member of Team or Board or both, but a single user cannot be in 2 or more than 2 teams or boards. 


### API endpoints:
* List all boards or create a new board
<br><code>GET POST http://127.0.0.1:8000/boards</code>  

* Get details of a board, update or delete board
<br><code>GET PUT PATCH DELETE http://127.0.0.1:8000/boards/int:board_id</code>

* List all tasks under the board or create a new tasks
<br><code>GET POST http://127.0.0.1:8000/boards/int:board_id/tasks</code>

* Get details of a task, update or delete tasks
<br><code>GET PUT PATCH DELETE  http://127.0.0.1:8000/boards/int:board_id/tasks/int:tasks_id</code>

* List all the teams or create a new.
<br><code>GET POST http://127.0.0.1:8000/teams</code>

* Get details of a team, update or delete teams
<br><code>GET PUT PATCH DELETE http://127.0.0.1:8000/teams/int:team_id</code>

* List all the users of a team
<br><code>GET http://127.0.0.1:8000/teams/int:team_id/users</code>

* Get details of a user, update or delete user
<br><code>GET PUT PATCH DELETE http://127.0.0.1:8000/teams/int:team_id/users/int:user_id</code>

* List all the users or create a new user
<br><code>GET POST http://127.0.0.1:8000/users</code>

* Get details of a user, update or delete user
<br><code>GET PUT PATCH DELETE http://127.0.0.1:8000/users/int:user_id</code>







# 
