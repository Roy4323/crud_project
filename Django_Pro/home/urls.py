from django.urls import path
from .import views

urlpatterns = [
    #path('hello/', views.say_hello),
    path('', views.say_hello, name='home'),
    path('try/', views.add_show, name='try'),
    path('delete/<int:id>', views.del_data, name='del_data'),
    path('update/<int:id>', views.upd_data, name='update_data'),
    path('db/', views.view_db, name='view_data')
]
