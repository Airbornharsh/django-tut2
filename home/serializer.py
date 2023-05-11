from rest_framework import serializers
from .models import *
from django.template.defaultfilters import slugify


class TodoSerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField()

    class Meta:
        model = Todo
        fields = ["user","id", "title", "description", "slug", "done"]

    def get_slug(self, obj):
        return slugify(obj.title)

    def validate_title(self, value):
        if value == "":
            raise serializers.ValidationError("Title cannot be empty")
        return value

    def validate(self, data):
        if data["title"] == data["description"]:
            raise serializers.ValidationError(
                "Title and Description should be different"
            )

        return data


class TimingTodoSerializer(serializers.ModelSerializer):
    todo = TodoSerializer()

    class Meta:
        model = TimingTodo
        fields = ["id", "todo", "timing"]
        # depth = 1
