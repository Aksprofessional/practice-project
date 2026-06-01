from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Note
        fields="__all__"
    def validate_title(self,value):
        if len(value)<3:
            raise serializers.ValidationError(
                'Title too short'
            )
        return value