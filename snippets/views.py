from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
'''
특정 콘텐츠 형태에 대한 요청이나 응답을 명시적으로 연결하지 않음.
request.data는 JSON 요청 뿐만 아니라 yaml과 같은 다른 포맷도 다룰 수 있다.
REST 프레임워크에서는 우리가 원하는 형태로 응답 객체를 렌더링해준다.
'''
@api_view(['GET', 'POST'])
def snippet_list(request, format=None):
    """
    코드 조각을 모두 보여주거나 새 코드 조각을 만듭니다.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk, format=None):
    """
    코드 조각 조회, 업데이트, 삭제
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

