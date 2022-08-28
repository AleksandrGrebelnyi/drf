from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from food.models import Food
from food.serializers import FoodSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework import permissions

# Create your views here.


class FoodViewSet(viewsets.ModelViewSet):  # the most popular view set ModelViewSet
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Food.objects.all()  # order_by('cat')
    serializer_class = FoodSerializer
    permission_classes = [permissions.IsAuthenticated]


# GenericViewSet use with mixin
# class FoodViewSet(mixins.CreateModelMixin,
#                   mixins.RetrieveModelMixin,
#                   mixins.UpdateModelMixin,
#                   mixins.ListModelMixin,
#                   GenericViewSet):
#     queryset = Food.objects.all()
#     serializer_class = FoodSerializer


