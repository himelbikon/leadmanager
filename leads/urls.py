from rest_framework import routers
from .api import LeadViewSet

# Maybe its a magical alternative of urls
router = routers.DefaultRouter()
router.register('api/leads', LeadViewSet, 'leads')

urlpatterns = router.urls
