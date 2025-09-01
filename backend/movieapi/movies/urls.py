from django.urls import path
from . import views
from .views import home, MovieListCreateView, MovieDetailView, RatingListCreateView, RatingDetailView

urlpatterns = [
    path('', home, name='home'),  # Root route
    path('movies/', MovieListCreateView.as_view(), name='movie-list-create'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('ratings/', RatingListCreateView.as_view(), name='rating-list-create'),
    path('ratings/<int:pk>/', RatingDetailView.as_view(), name='rating-detail'),
]