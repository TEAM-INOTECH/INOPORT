"""
URL configuration for transport project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include 
from django.contrib.auth import views as auth_views
from home.views import statistics
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = 'INOTECH'
admin.site.site_title = 'Yashraj Industries'
admin.site.index_title= 'Yashraj Industries'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', statistics, name='statistics'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


'''
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import statistics

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', statistics, name='statistics'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
'''