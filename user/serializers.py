from rest_framework import serializers
from user.models import User
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)
    

    class Meta:
        model = User
        fields = ('username', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            )

        user.set_password(validated_data['password'])
        user.save()

        return user
class UserGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name','last_name')

class UserPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'first_name','last_name']
