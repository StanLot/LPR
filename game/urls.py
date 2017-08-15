from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^registration/login/$', auth_views.login, name='login'),
    url(r'^registration/logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
]
