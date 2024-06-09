from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='homepage'),
    path('author/', include('author.urls')),
    path('category/<slug:brand_slug>/', views.home, name='brand_wise_post'),
    path('car/', include('car.urls')),
    path('brand/', include('brand.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)