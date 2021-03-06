"""python_test URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^client-list/$', views.client_list, {'template_name': 'clients.html'}, name='client_list'),
    url(r'^client-list-data/$', views.client_list_data),
    url(r'^add-client/$', views.post_client, {'template_name': 'add-client.html'}, name='add_client'),
    url(r'^edit-client/(?P<client_id>[0-9]+)/$', views.post_client, {'template_name': 'add-client.html'}, name='edit_client'),
    url(r'^$', TemplateView.as_view(template_name="home.html"))
]
