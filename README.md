* 参考  
https://docs.djangoproject.com/ja/2.0/intro/tutorial01/  
  
* プロジェクトの作成  
`$ django-admin startproject mysite`  
  
* サーバの起動  
`$ cd mysite`  
`$ python manage.py runserver`  
  
* アプリケーションの作成  
`$ python manage.py startapp polls`  
  
* タイムゾーンの設定  
`$ cd mysite`  
`$ vi settings.py`  
`TIME_ZONE = 'Asia/Tokyo'`  
  
* モデルの作成  
https://docs.djangoproject.com/ja/2.0/intro/tutorial02/#creating-models  
  
* プロジェクトにアプリケーションを追加  
`$ vi settings.py`  
  
`INSTALLED_APPS = [`  
`        'polls.apps.PollsConfig',`  
`...`  
  
* モデルからマイグレーションを作成  
`$ python manage.py makemigrations polls`  
  
* マイグレーションの適用  
`$ python manage.py migrate`  

* アプリをadmin上で編集できるようにする
`$ cd mysite/polls`
`$ vi admin.py`
`from .models import Question`
`admin.site.register(Question)`

* 管理ユーザーの作成
`$ python manage.py createsuperuser`

* urlsモジュールとビューとを結びつける
`$ cd mysite/polls`
`$ vi urls.py`
`from . import views`
`urlpatterns = [`
`    # ex: /polls/5/`
`    path('<int:question_id>', views.detail, name='detail'),`
`]`
