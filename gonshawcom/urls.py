"""gonshawcom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from settings import STATIC_URL, STATIC_ROOT, UPLOADS_URL, UPLOADS_ROOT
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index', include('content.urls')),
    url(r'^\Z', include('content.urls')),
    url(r'^content/', include('content.urls')),
]  + static(STATIC_URL, document_root=STATIC_ROOT) + static(UPLOADS_URL, document_root=UPLOADS_ROOT)


urlpatterns += staticfiles_urlpatterns()
