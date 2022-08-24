from rest_framework import serializers
from .models import Obfuscated


class ObfuscatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Obfuscated
        #fields = '__all__'
        fields = ('id','NUMDOS','NUMDOSVERLING','ANCART','FILIERE','ETAPE','VERLING','FORMAT')