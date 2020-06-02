"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # 原书中代码 url(r'', include('learning_logs.urls', namespace='learning_logs')),
    # 实际代码中需要由 app_name 组成的元组
    # learnings_logs
    url(r'', include(('learning_logs.urls', 'urls'), namespace='learning_logs')),
    # users
    url(r'^user/', include(('users.urls', 'urls'), namespace='users')),
]
