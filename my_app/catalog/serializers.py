
from rest_framework import serializers
from .models import Category, Skill


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', 'skill')


class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = ('name',)
