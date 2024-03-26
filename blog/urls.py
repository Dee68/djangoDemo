from django.urls import path
from .views import saySomething

urlpatterns = [
    path('', saySomething, name='saySomething')
]
