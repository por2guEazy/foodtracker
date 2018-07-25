from django.urls import path
from django.conf.urls import url 
from django.contrib.auth.views import login, logout



from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    url(r'^login/$', login, {'template_name': 'food/login.html'}),
    url(r'^logout/$', logout, {'next_page': '/food/login'}),
]
