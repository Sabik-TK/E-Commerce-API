from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from drf_yasg.views import get_schema_view as swagger_get_schema_view
from drf_yasg import openapi


schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Posts API",
        default_version='1.0.0',
        description="API documentation of App",
    ),
    public=True,
)


urlpatterns = [
    path('api-auth/', include('rest_framework.urls',)),
    path('admin/', admin.site.urls),
    path('auth/', include('drf_social_oauth2.urls', namespace='drf')),
    path('api/',include('apps.api.urls')),
    path('swagger/schema/', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-schema"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
