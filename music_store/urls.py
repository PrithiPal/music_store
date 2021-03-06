"""music_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

import games.views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',games.views.home,name='home'), 
    path('games/<int:game_id>',games.views.detail, name='detail'),
    path('order',games.views.order,name='order'),
    path('inventory',games.views.inventory,name='inventory'),
    path('exp',games.views.experiment,name='experiment'),
    path('order/<int:pk>',games.views.edit_order,name='edit_order')

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
