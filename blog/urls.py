"""blog URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin

from blog.api.endpoints.index import IndexView
from blog.api.endpoints.articles import ArticlesView
from blog.api.endpoints.feed import LatestEntriesFeed
from blog.api.endpoints.profile import ProfileView
from blog.api.endpoints.links import LinksView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^$', IndexView.as_view(), name='index'),
    url('^articles/(?P<atype>[-0-9a-z]{36})/$', ArticlesView.as_view(), name='articles'),
    url('^latest/feed/$', LatestEntriesFeed(), name='articles'),
    url('links/$', LinksView.as_view(), name='links'),
    url(r'profile/$', ProfileView.as_view(), name='api-profile'),
    url(r'^api/', include('blog.api.urls')),
]
