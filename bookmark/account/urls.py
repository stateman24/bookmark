from django.urls import path
from .views import user_login, dashboard, signout, register
from django.conf.urls.static import static
from django.conf import settings

app_name = 'account'

urlpatterns = [
    path('logout/', signout, name='logout'),
    path('', dashboard, name='dashboard'),
    path('register/', register, name='register')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)