from rest_framework.routers import DefaultRouter

from . import viewsets

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('user_balance', viewsets.UserBalanceViewSet),

# The API URLs are now determined automatically by the router.
urlpatterns = router.urls
