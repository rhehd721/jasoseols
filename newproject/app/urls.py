from django.urls import path, include
from .views import index, create, detail, delete, update, my_index

urlpatterns = [
    path('', index, name ='index'),
    path('my_index/', my_index, name ='my_index'),
    path('create/', create, name ='create'),
    path('detail/<int:jss_id>', detail, name ='detail'),
    path('delete/<int:jss_id>', delete, name ='delete'),
    path('update/<int:jss_id>', update, name ='update'),
]
