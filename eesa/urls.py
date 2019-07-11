"""eesa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import eesa_courses
import eesa_main
import eesa_sci_center
import eesa_users
from eesa_courses import urls
from eesa_main import urls
from eesa_users import urls
from eesa_sci_center import urls
from eesa import settings

urlpatterns = [
    path('', include(eesa_main.urls)),
    path('admin/', admin.site.urls),
    path('courses/', include(eesa_courses.urls)),
    path('users/', include(eesa_users.urls)),
    path('scicenter/', include(eesa_sci_center.urls)),
    path('djga/', include('google_analytics.urls')),
    url(r'^', include('favicon.urls'))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
