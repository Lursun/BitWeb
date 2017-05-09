"""djtest URL Configuration

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
from p2p_web import views as p2p_web_views
reload(p2p_web_views)

urlpatterns = [
    url(r'^$', p2p_web_views.index),
    url(r'^Query/?$', p2p_web_views.Query),
    url(r'^QueryNode/?$', p2p_web_views.QueryNode),
    url(r'^AddNode/?$', p2p_web_views.JoinNode),
    url(r'^Tx/?$', p2p_web_views.Tx),
    url(r'^reload/?$', p2p_web_views.reload_urls),
    url(r'^test/?$', p2p_web_views.test, name='home'),
    url(r'^add/?$', p2p_web_views.add, name='add'),
    url(r'^add2/(\d+)/(\d+)/?$', p2p_web_views.add2, name='add2'),
    url(r'^admin/', admin.site.urls),
]
