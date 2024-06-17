from django.urls import path
from rest_framework import routers
from .views import CreateStripeLoad

router= routers.DefaultRouter()
router.register(r'stripe', CreateStripeLoad, basename="stripe")
urlpatterns = router.urls



