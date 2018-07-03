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
  
* モデルの作成  
https://docs.djangoproject.com/ja/2.0/intro/tutorial02/#creating-models  
  
* プロジェクトにアプリケーションを追加  
`$ vi settings.py`  
  
`INSTALLED_APPS = [`  
`    'polls.apps.PollsConfig',`  
`..`  