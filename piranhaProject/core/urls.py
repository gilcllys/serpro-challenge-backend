from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core import viewsets

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'user_balance', viewsets.UserBalanceViewSet, basename='user_balance'),

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]