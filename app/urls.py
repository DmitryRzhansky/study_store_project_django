"""
Конфигурация URL для проекта app.

Список `urlpatterns` маршрутизирует URL к представлениям (views). Для получения дополнительной информации см.:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Примеры:
Функциональные представления
    1. Добавьте импорт:  from my_app import views
    2. Добавьте URL в urlpatterns:  path('', views.home, name='home')
Классовые представления
    1. Добавьте импорт:  from other_app.views import Home
    2. Добавьте URL в urlpatterns:  path('', Home.as_view(), name='home')
Включение другой конфигурации URL
    1. Импортируйте функцию include(): from django.urls import include, path
    2. Добавьте URL в urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from app import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('catalog/', include('goods.urls', namespace='catalog')),
    path('user/', include('users.urls', namespace='user')),
] 

if settings.DEBUG:
    urlpatterns += [path("__debug__/", include("debug_toolbar.urls")),] 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

