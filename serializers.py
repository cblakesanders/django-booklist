from django.contrib.auth.models import User
from users.models import Relationship
from rest_framework import serializers



class RelationshipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Relationship
        fields = ['followerUser', 'followingUser', 'status']

    def create(self, validated_data):
        relationship = Relationship(validated_data['followerUser'], 
                                    validated_data['followingUser'], 
                                    1
                                    )
        relationship.save()
        return relationship


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups']

