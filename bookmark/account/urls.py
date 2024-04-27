from django.urls import path
from django.contrib.auth import views as auth_views
from .views import user_login, dashboard, signout

app_name = 'account'

urlpatterns = [
    # path('login/', user_login, name='login')
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', signout, name='logout'),

    # change password url
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    # path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # reset password url
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password-reset'),
    path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('', dashboard, name='dashboard'),
]
