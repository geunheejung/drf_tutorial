from django.forms import widgets
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
    # source 인자로는 특정 필드를 지정 가능. 직렬화된 인스턴스의 속성 뿐만 아니라 마침표 표기 방식을 통해 특정 속성 탐색도 가능
    # ReadOnlyField는 직렬화에 사용되었을 땐 언제나 읽기 전용
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = (
            'id',
            'title',
            'code',
            'linenos',
            'language',
            'style',
            'owner'
        )


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')
