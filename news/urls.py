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
from django.views.decorators.cache import cache_page


from .views import *



urlpatterns = [
    
    path('register/', register, name ='register'),
    path('login/', user_login, name ='login'),
    path('logout/', user_logout, name ='logout'),
    path('contact/', contact, name ='contact'),
    # path('', index, name ='home'),
    # path('',cache_page() (HomeNews.as_view()), name ='home'),
    path('', HomeNews.as_view(), name ='home'),
    # path('category/<int:category_id>/', get_category, name = 'category'),
    path('category/<int:category_id>/', NewsByCategory.as_view(extra_context={'title':'Какой-то тайтл'}), name = 'category'),
    # path('news/<int:news_id>/', view_news, name = 'view_news'),
    path('news/<int:pk>/', ViewNews.as_view(), name = 'view_news'),
    # path('news/add-news/', add_news, name = 'add_news'),
    path('news/add-news/', CreateNews.as_view(), name = 'add_news'),
]
