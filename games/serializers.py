from rest_framework import serializers

from games.models import Game


class GameSerializer(serializers.ModelSerializer):

    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Game
        fields = '__all__'
        read_only_fields = ('created_by',)
