from django.urls import path
from django.urls.resolvers import URLPattern
from .views import WheaterView

urlpatterns = [ 
    path('wheater/', WheaterView.as_view(), name='wheater')
]