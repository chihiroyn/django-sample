"""
django_setup() を実行すると、Django の機能(モデルのインポートなど)が使えるようになる。
"""

import os
import sys
import django


def django_setup():
    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE', 'mysite.settings')
    base_dir = os.path.dirname(__file__)
    sys.path.append(os.path.join(base_dir, 'mysite'))
    django.setup()
