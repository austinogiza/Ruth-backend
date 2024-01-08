from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Ruth's Portfolio API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@ruthikegah.com"),
      license=openapi.License(name="Ruth's License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
        path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('admin/', admin.site.urls),
        path('api-auth/', include('rest_framework.urls')),path('change-password/<uidb64>/<token>/',
         TemplateView.as_view(template_name="password_reset_confirm.html"),
         name='password_reset_confirm'),
        path('api/', include('portfolio.urls')),
        path('accounts/', include('allauth.urls')),
        path('rest-auth/', include('dj_rest_auth.urls')),
        path('rest-auth/registration/', include('dj_rest_auth.registration.urls'))


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
