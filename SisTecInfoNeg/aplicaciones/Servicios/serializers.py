from rest_framework import serializers
from .models import *

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ['id','nombre']



class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = ['id','modelo']



class EquipoSerializer(serializers.ModelSerializer):
    #marca = MarcaSerializer()
    #marca = str(marca)
    class Meta:
        model = Equipo
        fields = ['id','modelo','marca','tipoEquipo']
