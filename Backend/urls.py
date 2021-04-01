from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<id>', views.delete, name='delete_name'),
    path('add', views.add, name='form'), 
    path('process', views.pro, name='process'),
    path('process2/<id>', views.pro2, name='pro'),
    path('edit/<id>', views.edit, name='edits')
]
