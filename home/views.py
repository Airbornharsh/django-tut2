from rest_framework.decorators import api_view, action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Todo
from .serializer import *
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication


class TodoView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            todos = Todo.objects.filter(user=request.user)
            serializer = TodoSerializer(todos, many=True)
            return Response(data={"data": serializer.data}, status=200)
        except Exception as e:
            print("An exception occurred")
            return Response(data={"message": e}, status=500)

    def post(self, request):
        try:
            data = request.data
            data["user"] = request.user.id
            serializer = TodoSerializer(data=data)
            print(serializer)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    data={
                        "message": "Todo created successfully",
                        "data": serializer.data,
                    },
                    status=200,
                )
            else:
                return Response(data={"message": serializer.errors}, status=400)
        except Exception as e:
            print("An exception occurred: ", e)
            return Response(data={"message": e}, status=500)

    def patch(self, request):
        try:
            data = request.data

            if not data.get("id"):
                return Response(data={"message": "id is required"}, status=400)

            obj = Todo.objects.get(id=data.get("id"))

            obj.done = data.get("done") if data.get("done") else obj.done
            obj.title = data.get("title") if data.get("title") else obj.title
            obj.description = (
                data.get("description") if data.get("description") else obj.description
            )

            obj.save()

            return Response(
                data={
                    "message": "Todo updated successfully",
                },
                status=200,
            )

        except Exception as e:
            print("An exception occurred: ", e)
            return Response(data={"message": e.args}, status=500)


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    @action(methods=["get"], detail=False)
    def get_timing_todos(self, request):
        try:
            todos = TimingTodo.objects.all()
            serializer = TimingTodoSerializer(todos, many=True)
            return Response(data={"data": serializer.data}, status=200)
        except Exception as e:
            print("An exception occurred")
            return Response(data={"message": e}, status=500)

    @action(methods=["post"], detail=False)
    def add_date_to_todo(self, request):
        try:
            data = request.data
            serializer = TimingTodoSerializer(data=data)
            if not serializer.is_valid():
                return Response(data={"message": serializer.errors}, status=400)

            serializer.save()
            return Response(data={"message": "Todo created successfully"}, status=200)
        except Exception as e:
            print("An exception occurred: ", e)
            return Response(data={"message": e.args}, status=500)
