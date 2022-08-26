from django.urls import path

from .views import homeView, itemView, aboutView
 
urlpatterns = [
    path('', homeView, name='home'),
    path('product/<int:pk>', itemView, name='item'),
    
    path('about/', aboutView, name='about')
]
