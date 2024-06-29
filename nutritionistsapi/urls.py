from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .yasg import schema_view

urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('v1/auth/', include('dj_rest_auth.urls')),
    path('v1/auth/registration/', include('dj_rest_auth.registration.urls')), # Uses CustomUserRegisterView
    path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('v1/', include('nutritionists.api.urls')),
    path('v1/', include('users.api.urls')),
    path('v1/', include('measurements.api.urls')),
]
