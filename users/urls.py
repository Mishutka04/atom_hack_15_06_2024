from django.urls import path
from . import views


app_name = 'users'

urlpatterns = [
    path(
        'user/auth/email/',
        views.ObtainEmailCallbackToken.as_view(),
        name='auth_email',
        ),
]
