from django.urls import path
from .views import Properties

urlpatterns=[
    path('', Properties.as_view(), name='properties'),
    path("<int:id>", Properties.as_view(), name='property')
]