from rest_framework import serializers
from .models import Serie

class SerieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    release_date = serializers.DateField()
    rating = serializers.IntegerField()
    category = serializers.ChoiceField(choices=Serie.CATEGORIES_CHOICES)

    def create(self, validated_data):
        """
        Cree y devuelva una nueva instancia de `Serie`, dados los datos validados.
        """
        return Serie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Actualice y devuelva una instancia de `Serie` existente, dados los datos validados.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance

class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = ('id', 'name', 'release_date', 'rating', 'category')