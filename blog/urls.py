from django.urls import path
from . import  views




urlpatterns = [
    path('', views.home, name='fish_home'),
    path('<int:post_id>', views.detail, name='detail'),
    path('about', views.about, name='fish_about')

]