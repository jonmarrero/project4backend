from .models import Team
from rest_framework import serializers

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # Which model will get serialized by this class
        model = Team
        # Which fields should be included in the output
        fields = ['id', 'subject', 'details']