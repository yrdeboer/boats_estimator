from django.conf.urls import include, url
from logic import urls as logic_urls
from logic.views import estimate_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^logic/', include(logic_urls, namespace='logic')),
    url(r'^$', estimate_view),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
