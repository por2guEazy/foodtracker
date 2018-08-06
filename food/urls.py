from django.urls import path
from django.conf import settings 
from django.conf.urls import url 
from django.conf.urls.static import static 
from django.contrib.auth.views import login, logout



from . import views


#app_name = 'items'


urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    url(r'^login/$', login, {'template_name': 'food/login.html'}),
    url(r'^logout/$', logout, {'next_page': '/food/login'}),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.remove_item, name='remove_item'),
] 
# This will be used later to server images
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
