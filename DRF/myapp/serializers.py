from rest_framework import serializers
from .models import Music

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__' # passa todos os campos vao ser serializados -> transformado em objeto json | tem como especificar tbm quais campos serao passados
        