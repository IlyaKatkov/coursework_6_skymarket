from django.urls import include, path, re_path
from djoser.views import UserViewSet
from rest_framework import routers
from rest_framework.routers import SimpleRouter

from ads.views import AdViewSet, AdListAPIView, AdCreateAPIView, AdRetrieveAPIView, AdUpdateAPIView, AdDestroyAPIView, CommentViewSet

app_name = "ads"

router = routers.SimpleRouter()
router.register('ads', AdViewSet, basename="ads")
router.register('comments', CommentViewSet, basename="comments")

urlpatterns = [
    path('ad/list/', AdListAPIView.as_view(), name='ad_list'),
    path('ad/view/<int:pk>/', AdRetrieveAPIView.as_view(), name='ad_view'),
    path('ad/create/', AdCreateAPIView.as_view(), name='ad_create'),
    path('ad/update/<int:pk>/', AdUpdateAPIView.as_view(), name='ad_update'),
    path('ad/delete/<int:pk>/', AdDestroyAPIView.as_view(), name='ad_delete'),
] + router.urls
