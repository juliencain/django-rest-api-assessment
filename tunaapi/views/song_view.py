
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import Song, Artist, Genre


class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ('id', 'title', 'artist_id', 'album', 'length')
        depth = 1

class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = ('id', 'description')
        depth = 1

class SingleSongSerializer(serializers.ModelSerializer):

  genres = GenreSerializer(read_only=True, many=True)
  class Meta:
      model = Song
      fields = ('id', 'title', 'artist', 'album', 'length', 'genres')
      depth = 2
    
    
class SongView(ViewSet):
 

    def retrieve(self, request, pk):
    
        try:
            song = Song.objects.get(pk=pk)
            genres = Genre.objects.filter(songgenres__song_id=song)
            song.genres=genres.all()
            serializer = SingleSongSerializer(song)
            return Response(serializer.data)
        except Song.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
   
        songs = Song.objects.all()
    
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)
    
    def create(self, request):
 
        artist = Artist.objects.get(pk=request.data["artist_id"])

        song = Song.objects.create(
            title=request.data["title"],
            artist=artist,
            album=request.data["album"],
            length=request.data["length"],
        )
        serializer = SongSerializer(song)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
   

        id = pk
        song = Song.objects.get(pk=pk)
        song.title = request.data["title"]
        song.album = request.data["album"]
        song.length = request.data["length"]

        artist = Artist.objects.get(pk=request.data["artist_id"])
        song.artist_id = artist.id
        song.save()

        serializer = SongSerializer(song)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk):
        song = Song.objects.get(pk=pk)
        song.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
            

