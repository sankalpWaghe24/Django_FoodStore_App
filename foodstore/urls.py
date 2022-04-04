
from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path("food/", include("food.urls")),
    path("account/", include("account.urls")),
    path("cart/", include("cart.urls")),
    url(r'^media/(?P<path>.*)$', serve,
        {'document_root':       settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,
        {'document_root': settings.STATIC_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
