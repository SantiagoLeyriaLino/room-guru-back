from django.urls import path
from .views import Properties, Rooms

urlpatterns=[
    path('', Properties.as_view(), name='properties'),
    path("<int:id>", Properties.as_view(), name='property'),
    path('rooms/', Rooms.as_view(), name='rooms'),
    path('rooms/<int:id>', Rooms.as_view(), name='room')
]