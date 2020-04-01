from Main.viewsets import TechViewSet, TechViewSet1
from rest_framework import routers

router = routers.DefaultRouter()
router.register('sampleAPI1', TechViewSet)

router_config = routers.DefaultRouter()
router.register('sampleAPI2', TechViewSet1)

