from django.urls import path
from .views import Users_views, User_Login

urlpatterns=[
    path('', Users_views.as_view(), name='Users_views'),
    path('<int:id>', Users_views.as_view(), name='User'),
    path('login/', User_Login.as_view(), name='Login')
]