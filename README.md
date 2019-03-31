参考
----
https://docs.djangoproject.com/ja/2.0/intro/tutorial01/  

プロジェクトの作成
-----------------
    $ django-admin startproject mysite

サーバの起動
------------
    $ cd mysite
    $ python manage.py runserver
  
言語とタイムゾーンの設定
------------------------
    $ cd mysite
    $ vi settings.py
    LANGUAGE_CODE = 'ja'
    
    TIME_ZONE = 'Asia/Tokyo'

アプリケーションの作成
----------------------
    $ python manage.py startapp polls

    $ cd mysite/mysite
    $ vi settings.py

```python:mysite/settings.py
...
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
...
```

ビューの作成（固定文をresponseとして返す）
----------------------------------------

    $ cd mysite/polls
    $ vi views.py

```python:polls/views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

アプリケーションのURLconf設定
------------------------------

    $ cd mysite/polls
    $ vi urls.py

```python:polls/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

ルートのURLconfにアプリケーションのURLconfをインクルードさせる
--------------------------------------------------------------

    $ cd mysite
    $ vi urls.py

```python:mysite/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

モデルの作成
------------
https://docs.djangoproject.com/ja/2.0/intro/tutorial02/#creating-models

モデルからマイグレーションを作成
--------------------------------
    $ python manage.py makemigrations polls

マイグレーションの適用
----------------------
    $ python manage.py migrate

アプリをadmin上で編集できるようにする
-------------------------------------
    $ cd mysite/polls
    $ vi admin.py

```python:mysite/polls/admin.py
from .models import Question
admin.site.register(Question)
```

モデルでデータを操作する
------------------------
    $ python manage.py migrate
    
    >>> from polls.models import Choice, Question

    >>> Question.objects.all()
    <QuerySet []>

    >>> from django.utils import timezone
    >>> q = Question(question_text="What's new?", pub_date=timezone.now())
    >>> q.save()
    >>> Question.objects.all()
    <QuerySet [<Question: Question object (1)>]>

    >>> q.choice_set.create(choice_text='Not much', votes=0)
    <Choice: Not much>

    >>> q.question_text = "What's up?"
    >>> q.save()

管理ユーザーの作成
------------------
    $ python manage.py createsuperuser

urlsモジュールとビューとを結びつける
------------------------------------
    $ cd mysite/polls
    $ vi urls.py

```python:mysite/polls/urls.py
from . import views
urlpatterns = [
    # ex: /polls/5/
    path('<int:question_id>', views.detail, name='detail'),
]
```

テンプレートをロードし、コンテキストに値を入れ、テンプレートをレンダリングした結果をHttpResponseオブジェクトで返す
------------------------------------------------------------------------------------------------------------------
    $ cd mysite/polls
    $ vi views.py

```python:mysite/polls/views.py
from django.shortcuts import render

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
```

    $ cd mysite/polls/templates/polls
    $ vi index.html

```python:mysite/polls/template/polls/index.html
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```

ごく簡単なフォームのページを作成し、フォームに入力した値をGETメソッドで後続処理に渡す
-------------------------------------------------------------------------------------
    $ cd mysite/polls/templates/polls
    $ vi index.html

```python:mysite/polls/template/polls/index.html
<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="utf-8">
    <title>検索ページ</title>
  </head>

  <body>
    <form action="{% url 'search' %}" method="get">
      <input type="text" value="" name="keyword">
      <input type="submit" value="検索する！">
    </form>
  </body>
</html>
```
    $ cd mysite/polls
    $ vi views.py

```python:mysite/polls/views.py
def search(request):
    keyword = request.GET['keyword']
    return HttpResponse(keyword)
```

    $ cd mysite/polls
    $ vi urls.py

```python:mysite/polls/urls.py
urlpatterns = [
...
    path('search', views.search, name='search'),
]
```

同じくPOSTメソッドの場合
-----------------------
    $ cd mysite/polls/templates/polls
    $ vi index.html

```python:mysite/polls/template/polls/index.html
...
    <form action="{% url 'search' %}" method="post">
    {% csrf_token %}
...
```
    $ cd mysite/polls
    $ vi views.py

```python:mysite/polls/views.py
...
    keyword = request.POST['keyword']
...
```

テストを実行する
----------------
    $ python manage.py test polls

静的ファイルの置き場所（デフォルト）
------------------------------------
    mysite/polls/static/polls/

テンプレートから静的ファイルを読み込む
-------------------------------------------
    ...
    {% load static %}
    
    <link rel="stylesheet" type="text/css" href="{% static 'polls/style.css' %}">
    ...

HTTPSリダイレクトするようにする
-------------------------------

```python:mysite/settings.py
SECURE_SSL_REDIRECT = True
```

開発環境と本番環境とで環境設定を分ける
--------------------------------------

* settings.py を３つのファイルに分ける
* manage.py を修正する（開発環境向け）
* wsgi.py を修正する（本番環境向け）

https://leben.mobi/blog/python_django_settings/python/?unapproved=1557&moderation-hash=b5898a59dbc8eb9fa7db7eb59e8bd16e#comment-1557

* 他、settings.py を読み込んでいる処理を修正する（django.setup()を呼んでいる処理）← 忘れないように注意！

プロジェクトに設定済であるタイムゾーンの現在時刻を取得する
----------------------------------------------------------

```
    from django.utils import timezone
...
    now = timezone.localtime()
```

pip install pytz しておく必要があるらしい。
