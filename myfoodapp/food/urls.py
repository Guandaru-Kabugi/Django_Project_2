from . import views
from django.urls import path
urlpatterns = [
    path('', views.index, name='index'),
    path('mine',views.item, name='item'),
    path('january', views.january, name='January')
]