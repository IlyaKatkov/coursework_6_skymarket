from django.conf.urls import url
from django.urls import include, path, re_path
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = "users"

users_router = SimpleRouter()
users_router.register("users", UserViewSet, basename="users")

urlpatterns = [
    path('', include(users_router.urls)),
    path('users/auth/', include('djoser.urls')),
    path('users/', include('djoser.urls')), #GET список профилей пользователей, POST регистрация пользователя
    path('users/{id}/', include('djoser.urls')), #GET, PATCH, DELETE в соответствии с REST и необходимыми permissions (для администратора)
    path('users/me/', include('djoser.urls')), #GET PATCH получение и изменение своего профиля
    path('users/set_password/', include('djoser.urls')), #POST ручка для изменения пароля
    path('users/reset_password/', include('djoser.urls')), #POST ручка для направления ссылки сброса пароля на email
    path('users/reset_password_confirm/', include('djoser.urls')), #POST ручка для сброса своего пароля
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.jwt')),
    path('token/', TokenObtainPairView.as_view(), name="take_token"),
    path('token/refresh/', TokenRefreshView.as_view(), name="refresh_token"),
]
