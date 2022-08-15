from rest_framework import serializers

from first_app.models import Food
from first_app.models import FoodCategory


class FoodSerializer(serializers.ModelSerializer):
    additional = serializers.SerializerMethodField()

    def get_additional(self, obj):
        return (
            obj.additional.filter(is_publish=True)
            .exclude(internal_code__isnull=True)
            .values_list("internal_code", flat=True)
        )

    class Meta:
        model = Food
        fields = (
            "internal_code",
            "code",
            "name_ru",
            "description_ru",
            "description_en",
            "description_ch",
            "is_vegan",
            "is_special",
            "cost",
            "additional",
        )


class FoodListSerializer(serializers.ModelSerializer):
    foods = FoodSerializer(source="food_set", many=True, read_only=True)

    class Meta:
        model = FoodCategory
        fields = ("id", "name_ru", "name_en", "name_ch", "order_id", "foods")
