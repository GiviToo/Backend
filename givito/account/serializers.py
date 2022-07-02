from rest_framework import serializers

from givito.account.models import User

class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()
    class Meta:
        model = User
        exclude = ['password', 'id', 'deleted_at', 'groups', 'user_permissions', 'is_staff', 'is_superuser']
        read_only_fields = ['id', 'deleted_at', 'uuid', 'created_at', 'modified_at', 'is_staff', 'is_superuser', 'groups', 'user_permissions']

    def get_avatar(self, obj):
        if(obj.avatar == "" or obj.avatar == None):
            return None
        else:
            return obj.avatar.url

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(self.context['request'].data['password'])
        user.is_active = True
        user.save()
        return user
        

class ChangePasswordSerializer(serializers.Serializer):
    model = User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class UserMinimalSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ['name', 'avatar', 'uuid']