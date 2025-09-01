from rest_framework import generics, permissions
from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer
from django.http import JsonResponse
# Create your views here.

def home(request):
    return JsonResponse({
        "message": "🎬 Welcome to the Movie Recommender API!",
        "endpoints": {
            "movies": "/api/movies/",
            "ratings": "/api/ratings/",
        },
        "docs": "Future: link to API docs here"
    })

class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Retrieve/Update/Delete a single movie
class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# List or create ratings
class RatingListCreateView(generics.ListCreateAPIView):
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Rating.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Retrieve/Update/Delete a single rating
class RatingDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Rating.objects.filter(user=self.request.user)