from django.urls import path
from django.urls.resolvers import URLPattern
from .views import WheaterView, WheatersView

urlpatterns = [ 
    path('wheater/', WheatersView.as_view(), name='wheater'),
    path('wheater/<int:pk>/', WheaterView.as_view(), name='wheaterbyid')
]