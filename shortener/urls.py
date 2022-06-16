
from django.urls import path, include
from . import views

urlpatterns = [
    
    path('', views.home_view, name='home'),
    path('<code>/', views.redirect_view, name = 'link_redirect')
]