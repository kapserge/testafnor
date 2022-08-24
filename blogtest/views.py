from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from django.shortcuts import redirect
from .models import Obfuscated
from .serializers import ObfuscatedSerializer
from rest_framework.response import Response



class detailApiView(viewsets.ViewSet):
    def list_obf(self, request):
        queyset = Obfuscated.objects.all()
        serializer = ObfuscatedSerializer(queyset, many=True)
        return Response(serializer.data)

    def get(self, request,pk=None):
        players = Obfuscated.objects.all()
        todo = get_object_or_404(players,pk=pk)
        serializer = ObfuscatedSerializer(todo)
        return Response(serializer.data)
    def error_404_view(request,*args, **kwargs):
        return redirect('/api/') 


    
