# Django / Django Rest 프레임워크 튜토리얼
----
> 시작 날짜: 2019.01.13(일)

> 목표: D.R.F로 로그인 인증 API 만들기

> (http://raccoonyy.github.io/drf3-tutorial-n) 👈 튜토리얼 시리즈로 훈련 
  
```text
Model에서 각각의 Model의 필드와 Model간의 관계를 설정해주고,
Serializers에서는 이러한 Model을 json, xml과 같이 클라이언트에 맞게 직렬화 해주거나
클라이언트의 request 파라미터를 서버가 알 수 있게 반직렬화 해준다.
그리고 일대일 일대다 다대다와 같은 모델에서 맽은 관계를 Serializers에서 직렬화하여 내려줄 수 있다.
View는 클라이언트의 Request를 받아서 그에 맞는 처리를 한 다음 Response를 해주는 역할을 한다.
Django에서 View는 3가지 종류가 있는데
* 함수형 View
* 클래스형 View
* 제네릭 클래스 기반 뷰가 존재한다.
Django에서는 제네릭 클래스 기반 뷰를 애용하며, Django가 제공해주는 View를 상속받으면
create메서드와 같은 기본 메서드를 직접 구현하지 않아도 된다.
queryset은 Django에서 Model을 다룰 때 사용하는 ORM이며, ORM은 SQL을 손쉽게 사용하기 위해, 또 특정 제약없이 공통적으로 모델에 대응하기 위한 도구이다?
View에서 serializer_class를 통해 Serializer를 설정해주면 그에 맞게 직렬화가 이뤄지나보다.
이러한 View에서는 Response처리나 Request에 따라 분기를 하거나 인증 과정을 추가할 수 있다.
urls은 Request와 View를 이어주는 역할을 하는것같다.
특정한 url로 유저가 REQUEST할 경우 그 REQUEST는 해당 url설정의 View에게 전달되는것같다.
client -> urls -> views -> models
client <- serializers <-  views  <- models
```

**View의 종류**
> 1. HttpResponse를 이용한 함수형 뷰
>> 함수형뷰를 사용해 template를 읽어 HttpResponse로 응답하는 과정
```python
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    
    context = {
        'latest_question_list': latest_question_list,
    }
    
    return HttpResponse(template.render(context, request))
```
> 2. render를 이용한 함수형 뷰
>> Django의 shortcuts.render를 사용하여 보다 간결하게 표현
```python
from django.shortcuts import render

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    context = {
        'lastest_question_list': latest_question_list,
    }

    return render(request, 'polls/index.html', context)
```
> 3. 제네릭 뷰 시스템(Generic views system)
>> 위의 반복되는 공통 부분을 패턴화하여 추상화 해두었다. 최소한 뷰가 어떤 모델을 사용할 것인지만 지정해주면 모두 상위 클래스가 알아서 처리해준다.
```python
from django.views.generic import ListView

class IndexView(ListView):
    model = Question
```