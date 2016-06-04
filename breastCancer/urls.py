"""documentLibary URL Configuration

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
from breastCancerApp import views as breastCancerApp_views  # new
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^home/', breastCancerApp_views.home, name='home'),  # 注意修改了这一行
    url(r'^$', breastCancerApp_views.home),
    url(r'^displaySubjectItems/(\d+)/$', breastCancerApp_views.displaySubjectItems, name='displaySubjectItems'),
    url(r'^admin/', admin.site.urls),
]+ static(document_root=settings.STATIC_ROOT)
