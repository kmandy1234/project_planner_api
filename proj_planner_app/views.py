from rest_framework.response import Response
from rest_framework import status
from . models import Board, Task, Team, User
from . serializers import BoardSerializer, TaskSerializer, TeamSerializer, UserSerializer
from django.http import Http404
from rest_framework.views import APIView
#Board
class BoardList(APIView):
    """
    list all boards or create a board
    """
    def get(self, request):
        boards = Board.objects.all()
        serializer = BoardSerializer(boards, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BoardSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class BoardDetail(APIView):
    """
    delete_board , add_task , update_task_status, view_board_detail
    """
    def get_object(self, board_id):
        """
        returns object instance to be used for detail view
        """
        try:
            return Board.objects.get(board_id=board_id)
        except Board.DoesNotExist:
            raise Http404
    
    #delete_board
    def delete(self, request, board_id):
        boards = self.get_object(board_id)
        boards.delete()
        return Response(status = status.HTTP_204_NO_CONTENT) 
        
    #update_board
    def put(self, request, board_id):
        boards = self.get_object(board_id)
        serializer = BoardSerializer(boards, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, board_id):
        boards = self.get_object(board_id)
        serializer = BoardSerializer(boards, data= request.data, partial = True )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    
    def get(self, request, board_id):
        boards = self.get_object(board_id)
        serializer = BoardSerializer(boards)
        return Response(serializer.data)


class BoardsTaskList(APIView):
    def get_board(self, board_id):
        try:
            return Board.objects.get(board_id = board_id)
        except Board.DoesNotExist:
            return Http404

    #list all task under the board 
    def get(self, request, board_id):
        board = self.get_board(board_id)
        tasks = Task.objects.filter(board_id = board)
        serializer = TaskSerializer(tasks, many = True)
        return Response(serializer.data)
    
    #add tasks under the board
    def post(self, request, board_id):
        #board = self.get_board(board_id)
        serializer = TaskSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
class BoardsTaskDetail(APIView):
    def get_board(self, board_id):
        try:
            return Board.objects.get(board_id = board_id)
        except Board.DoesNotExist:
            return Http404
    
    def get_task(self, board_id, task_id):
        try: 
            board = self.get_board(board_id)
            return Task.objects.get(board_id = board, task_id = task_id)
        except Task.DoesNotExist:
            return Http404

    #task detail
    def get(self, request, board_id, task_id):
        task = self.get_task(board_id, task_id)
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    
    def put(self, request, board_id, task_id):
        task = self.get_task(board_id, task_id)
        serializer = TaskSerializer(task, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, board_id, task_id):
        task = self.get_task(board_id, task_id)
        serializer = TaskSerializer(task, data= request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, board_id, task_id):
        task = self.get_task(board_id, task_id)
        task.delete()
        return Response(status=status.HTTP_200_OK)
        
  
#Team 
class TeamList(APIView):
    def get(self, request):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TeamSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


class TeamDetail(APIView):
    def get_object(self, team_id):
        """
        returns object instance to be used for detail view
        """
        try:
            return Team.objects.get(team_id=team_id)
        except Team.DoesNotExist:
            raise Http404

    #describe_team
    def get(self, request, team_id):
        team = self.get_object(team_id)
        serializer = TeamSerializer(team)
        return Response(serializer.data)
    
    #update_team
    def put(self, request, team_id):
        team = self.get_object(team_id)
        serializer = TeamSerializer(team, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status= status.HTTP_400_BAD_REQUEST)

    def patch(self, request, team_id):
        team = self.get_object(team_id)
        serializer = TeamSerializer(team, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status= status.HTTP_400_BAD_REQUEST)

    #delete_team
    def delete(self, request, team_id):
        team = self.get_object(team_id)
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class TeamUserList(APIView):
    def get_team(self, team_id):
        try:
            return Team.objects.get(team_id = team_id)
        except Team.DoesNotExist:
            raise Http404
    
    #get all users of the team
    def get(self, request, team_id):
        team = self.get_team(team_id)
        team_users = User.objects.filter(team_id = team)
        serializer = UserSerializer(team_users, many = True)
        return Response(serializer.data)
    

class UserDetail(APIView):
    def get_user(self, user_id):
        try:
            return User.objects.get(user_id = user_id)
        except User.DoesNotExist:
            raise Http404
    
    # describe user
    def get(self, request, user_id, team_id = None):
        user = self.get_user(user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    #update user
    def put(self, request, user_id, team_id = None):
        user = self.get_user(user_id)
        serializer = UserSerializer(user, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    

    def patch(self, request, user_id, team_id = None):
        user = self.get_user(user_id)
        serializer = UserSerializer(user, data= request.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    #delete user
    def delete(self, request, user_id, team_id = None):
        user = self.get_user(user_id)
        user.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
 
 
   
class TeamUserDetail(UserDetail):
    """
    def get_team(self, team_id):
        try:
            return Team.objects.get(team_id = team_id)
        except Team.DoesNotExist:
            raise Http404
    
    def get_user(self, user_id):
        try:
            return User.objects.get(user_id = user_id)
        except User.DoesNotExist:
            raise Http404
    
    def get(self, request, user_id):
        user = self.get_user(user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    #add user under a team
    def patch(self, request, team_id, user_id):
        team = self.get_team(team_id)
        user = self.get_user(user_id)
        if user.team_id is None:
            user.team_id = team
            user.save()
            serializer = UserSerializer(user)
            return Response(serializer.data, status= status.HTTP_200_OK)
        else:
            return Response(data= {'error': 'user is a member of team! choose another user'}, status=status.HTTP_406_NOT_ACCEPTABLE)
            
            
    #remove user from the team
    def delete(self, request, team_id, user_id):
        team = self.get_team(team_id)
        user = self.get_user(user_id)
        if user.team_id is team:
            user.team_id = None
            user.save()
            serializer = UserSerializer(user)
            return Response(serializer.data, status= status.HTTP_200_OK)
        else:
            return Response(data= {'error': 'user is a member of team! choose another user'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    """

#user
class UserList(APIView):
    
    #list user 
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many = True)
        return Response(serializer.data)

    #create user
    def post(self, request):
        serializer = UserSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    

