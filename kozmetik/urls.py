"""
URL configuration for kozmetik project.

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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from appKozmetik .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',İndex,name='Anasayfa'),
    path('kategori/<id>/',Category,name='categorys'),
    path('detay/<id>/',Detail,name='detay'),
    path('kaydol/',Register,name='kaydol'),
    path('giris/',Login,name='giris'),
    path('cikis/',Logout,name='cikis'),
    path('profil/',Profil,name='profil'),
    path('ürünEkle/<product_id>/', ürünEkle,name='ürünEkle'),
    path('sepet/',Shopping,name='sepet')
    
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
