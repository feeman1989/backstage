"""backstage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app.views import login,account_auth,machine_info,logout,index,alter_open_server_time,exec_sys_command,open_server,upload_file

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',login),
    url(r'^login/$', login),
    url(r'^account_auth/$', account_auth),
    url(r'^index/$', index),
    url(r'^machine_info/$', machine_info),
    url(r'^logout/$', logout),
    url(r'^alter_open_server_time/$', alter_open_server_time),
    url(r'^exec_sys_command/$', exec_sys_command),
    url(r'^open_server/$', open_server),
    url(r'^upload_file/$', upload_file),
]
