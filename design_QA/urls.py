"""design_QA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from wenjuan import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^manage/$', views.manage, name='manage'),
    url(r'^login/$', views.login, name='login'),
    url(r'^admin_manage/$', views.admin_manage, name='admin_manage'),
    url(r'^register/$', views.register, name='register'),
    url(r'^register_check/$', views.register_check, name='register_check'),
    url(r'^read_excel/$', views.read_excel, name='read_excel'),
    url(r'^download/$', views.download, name='download'),
    url(r'^Merit/$', views.Merit, name='Merit'),
    url(r'^Lucky/$', views.Lucky, name='Lucky'),
    url(r'^Efficiency/$', views.Efficiency, name='Efficiency'),
    url(r'^test/$', views.test, name='test'),

]
