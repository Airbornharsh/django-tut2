from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo
from .serializer import TodoSerializer
# from .models import Todo


@api_view(["GET"])
def home(request):
    return Response(data={"message": "Hello, world!"}, status=200)

@api_view(["GET"])
def get_todos(request):
    try:
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(data={"data": serializer.data}, status=200)
    except Exception as e:
        print("An exception occurred")
        return Response(data={"message": e}, status=400)

@api_view(["POST"])
def post_todo(request):
    try:
        data = request.data
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
            return Response(data={"message": "Todo creation failed"}, status=400)
    except Exception as e:
        print("An exception occurred")
        return Response(data={"message": e}, status=400)
