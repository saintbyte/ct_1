from django.contrib import admin

from first_app.models import Food
from first_app.models import FoodCategory

admin.site.register(FoodCategory)
admin.site.register(Food)
