from rest_framework import serializers
from teammembers.models import Member


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'
        extra_kwargs = {
            "userId": {"validators": []}
        }
