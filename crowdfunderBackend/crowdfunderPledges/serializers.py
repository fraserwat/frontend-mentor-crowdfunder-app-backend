from rest_framework import serializers

from .models import Pledge


class PledgeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pledge
        fields = "__all__"
