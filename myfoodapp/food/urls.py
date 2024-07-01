from . import views
from django.urls import path
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:item_id>/',views.detail,name='detail'),
    path('mine',views.item, name='item'),
    path('january', views.january, name='January')
]