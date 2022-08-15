from rest_framework import routers

from first_app.api_views import FoodViewSet

router = routers.DefaultRouter()
router.register(r"foods", FoodViewSet)
