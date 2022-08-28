from rest_framework import serializers
from food.models import Food


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ('title', 'recipe', 'cat',)


# with 'cat' does not work because cat is ForeignKey for Food
# class FoodSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Food
#         fields = ('title', 'recipe',)


# create displayed attributes by yourself
# class FoodSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=225)
#     is_published = serializers.BooleanField(default=True)
#
