import imp
from django.urls import path
from .views import home, portfolio_detail
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', home, name='home'),
    path('portfolio_detail/<int:id>/', portfolio_detail, name='portfolio_detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)