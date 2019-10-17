from rest_framework import serializers
from cars.models import Car
from blog.models import Blog
from django.contrib.auth.models import AnonymousUser
from common.serializers import UserSerializer


class PostsListSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Blog
        fields = ('id', 'user')


class PostDetailSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(PostDetailSerializer, self).__init__(*args, **kwargs)
        user = self.context['request'].user
        if not isinstance(user, AnonymousUser):
            self.fields['car'].queryset = Car.objects.filter(user=user)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Blog
        fields = '__all__'
