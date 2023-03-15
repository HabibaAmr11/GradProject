from rest_framework import serializers

from museums.models import Museum, Collection, Timeline, Favorite


class MuseumSerializer(serializers.ModelSerializer):

    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Museum
        fields = '__all__'
        read_only_fields = ('created_by',)


class CollectionSerializer(serializers.ModelSerializer):

    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Collection
        fields = '__all__'
        read_only_fields = ('created_by',)


class TimelineSerializer(serializers.ModelSerializer):

    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Timeline
        fields = '__all__'
        read_only_fields = ('created_by',)


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'

