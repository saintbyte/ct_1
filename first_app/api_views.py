from django.db.models import Count
from django.db.models import Prefetch
from rest_framework import viewsets

from first_app.models import Food
from first_app.models import FoodCategory
from first_app.serializers import FoodListSerializer


class FoodViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = (
        FoodCategory.objects.filter(food__is_publish=True)
        .annotate(food_cnt=Count("food"))
        .filter(food_cnt__gt=0)
        .prefetch_related(
            Prefetch(
                "food",
                queryset=Food.objects.filter(is_publish=True),
                to_attr="food_set",
            )
        )
        .order_by("order_id")
    )
    serializer_class = FoodListSerializer
    permission_classes = []
