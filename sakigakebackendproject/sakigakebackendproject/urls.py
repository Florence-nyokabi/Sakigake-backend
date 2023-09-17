from django.contrib import admin
from django.urls import include, path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="MzaziConnect API",
        default_version='v1',
        description="MzaziConnect assignment and shops models endpoints",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="Your License"),

    public=True,
    permission_classes=(permissions.AllowAny,),
))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('school/' , include('school.urls')),
    path('assignment/', include('assignment.urls')),
    path('shop/', include('shop.urls')),
    path('teachers/', include('teachers.urls')),
    path('subjects/', include('subject.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),name='schema-redoc'),
    path("comments/", include ("comments.urls")),
    path("accounts/", include ("accounts.urls")),
]