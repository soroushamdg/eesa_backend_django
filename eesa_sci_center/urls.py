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
from django.urls import path

from eesa_sci_center import views

urlpatterns = [
    path('', views.index, name='scicenter_index'),
    path('cat=<int:cat_id>/', views.category_index, name = 'scicenter_cat_index'),
    path('pub=<int:pub_id>/', views.publisher_index, name= 'scicenter_pub_index')
]
