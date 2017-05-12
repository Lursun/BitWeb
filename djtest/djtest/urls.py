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
from management import views as management_views
reload(management_views)

urlpatterns = [
    url(r'^$', management_views.index),
    url(r'^Query/?$', management_views.Query),
    url(r'^QueryNode/?$', management_views.QueryNode),
    url(r'^JoinNode/?$', management_views.JoinNode),
    url(r'^Tx/?$', management_views.Tx),
    url(r'^reload/?$', management_views.reload_urls),
    url(r'^test/?$', management_views.test, name='home'),
    url(r'^add/?$', management_views.add, name='add'),
    url(r'^add2/(\d+)/(\d+)/?$', management_views.add2, name='add2'),
    url(r'^admin/', admin.site.urls),
]