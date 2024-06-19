"""
Конфигурация URL для проекта mysite.

Список `urlpatterns` направляет URL в представления. Для получения дополнительной информации см.:
https://docs.djangoproject.com/en/5.0/topics/http/urls/
Примеры:
Функциональные представления
    1. Добавьте import:  from my_app import views
    2. Добавьте URL в urlpatterns:  path('', views.home, name='home')
Представления на основе классов
    1. Добавьте import:  from other_app.views import Home
    2. Добавьте URL в urlpatterns:  path('', Home.as_view(), name='home')
Включение другого URLconf
    1. Import the include() функцию: from django.urls import include, path
    2. Добавьте URL в urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('category/<int:category_id>/', get_category),
]
