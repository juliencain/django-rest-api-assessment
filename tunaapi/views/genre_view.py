
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import Genre, Song

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'description')
        depth = 1

class SongSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Song
        fields = ('id', 'title', 'artist_id', 'album', 'length')
        depth = 1

class SingleGenreSerializer(serializers.ModelSerializer):
    songs = SongSerializer(read_only=True, many=True)
    class Meta:
        model = Genre
        fields = ('id', 'description', 'songs')
        depth = 1
        
        
class GenreView(ViewSet):
    def retrieve(self, request, pk):
        try:
            genre = Genre.objects.get(pk=pk)
            songs = Song.objects.filter(genresongs__genre_id=genre)
            genre.songs=songs.all()
            serializer = SingleGenreSerializer(genre)
            return Response(serializer.data)
        except Genre.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        genres = Genre.objects.all()
    
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)
    
    def create(self, request):

        genre = Genre.objects.create(
            description=request.data["description"],
        )
        serializer = GenreSerializer(genre)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):

        id = pk
        genre = Genre.objects.get(pk=pk)
        genre.description = request.data["description"]

        genre.save()

        serializer = GenreSerializer(genre)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk):
        genre = Genre.objects.get(pk=pk)
        genre.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
            


