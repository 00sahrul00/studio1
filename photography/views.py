from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from .models import Studio, Photographer, Photoshoot
from .serializers import StudioSerializer, PhotographerSerializer, PhotoshootSerializer

# view untuk studio dengan class base view
class StudioList(APIView):
    """
    ini merupakan proses pengambilan data atau simpan data
    """
    permission_classes = [permissions.AllowAny]  # Memindahkan permission_classes ke dalam kelas tampilan
    def get(self, request, format=None):
        studio = Studio.objects.all()
        serializer = StudioSerializer(studio, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = StudioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudioDetail(APIView):
    """
    ambil data, edit atau hapus data
    """
    permission_classes = [permissions.AllowAny]  # Memindahkan permission_classes ke dalam kelas tampilan
    def get_object(self, pk):
        try:
            return Studio.objects.get(pk=pk)
        except Studio.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        studio = self.get_object(pk)
        serializer = StudioSerializer(studio)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        studio = self.get_object(pk)
        serializer = StudioSerializer(studio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        studio = self.get_object(pk=pk)
        studio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# view untuk photographer dengan class base view
class PhotographerList(APIView):
    """
    ini merupakan proses pengambilan data atau simpan data
    """
    permission_classes = [permissions.AllowAny]  # Memindahkan permission_classes ke dalam kelas tampilan
    def get(self, request, format=None):
        photographer = Photographer.objects.all()
        serializer = PhotographerSerializer(photographer, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = PhotographerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PhotographerDetail(APIView):
    """
    ambil data, edit atau hapus data
    """
    permission_classes = [permissions.AllowAny]  # Memindahkan permission_classes ke dalam kelas tampilan
    def get_object(self, pk):
        try:
            return Photographer.objects.get(pk=pk)
        except Photographer.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        photographer = self.get_object(pk)
        serializer = PhotographerSerializer(photographer)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        photographer = self.get_object(pk)
        serializer = PhotographerSerializer(photographer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        photographer = self.get_object(pk=pk)
        photographer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# view untuk photoshoot dengan class base view
class PhotoshootList(APIView):
    """
    ini merupakan proses pengambilan data atau simpan data
    """
    permission_classes = [permissions.AllowAny]  # Memindahkan permission_classes ke dalam kelas tampilan
    def get(self, request, format=None):
        photoshoot = Photoshoot.objects.all()
        serializer = PhotoshootSerializer(photoshoot, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = PhotoshootSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PhotoshootDetail(APIView):
    """
    ambil data, edit atau hapus data
    """
    permission_classes = [permissions.AllowAny]  # Memindahkan permission_classes ke dalam kelas tampilan
    def get_object(self, pk):
        try:
            return Photoshoot.objects.get(pk=pk)
        except Photoshoot.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        photoshoot = self.get_object(pk)
        serializer = PhotoshootSerializer(photoshoot)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        photoshoot = self.get_object(pk)
        serializer = PhotoshootSerializer(photoshoot, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        photoshoot = self.get_object(pk=pk)
        photoshoot.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
