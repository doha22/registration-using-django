from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView # new
from  django.contrib.auth.urls import urlpatterns
from . import views
urlpatterns = [

     # path('login', include('django.contrib.auth.urls')),
    # path('login',TemplateView.as_view(template_name='login.html'), name='login'),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    # path('login',views.login,include('django.contrib.auth.urls') ,name='login')
    # path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.SignUp.as_view(), name='signup'),

]