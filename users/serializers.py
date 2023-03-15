from rest_framework import serializers
from users.models import User, ContactUs


class UserSerializer(serializers.ModelSerializer):

    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'nationality',
            'redeem_points',
            'created_by',
        ]
        read_only_fields = ('created_by',)


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'
