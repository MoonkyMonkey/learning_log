from django.conf.urls import url
# 书中的代码
# from django.contrib.auth.views import login
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    # 登录页面
    # 书中的
    # url(r'^login/$', login, {'template_name':'users/login.html'},
    #     name='login'),
    url(r'^login/$', LoginView.as_view(template_name='users/login.html'),
        name='login'),
    # 注销页面
    url(r'^logout/$', views.logout_view, name='logout'),
    # 注册页面
    url(r'^register/$', views.register, name='register'),
]
