from rest_framework import viewsets

from .models import Movie, Person
from .serializers.movies import (
    MovieCreateSerializer,
    MovieListSerializer,
)
from .serializers.persons import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    """
    Persons endpoint.
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class MovieViewSet(viewsets.ModelViewSet):
    """
    Movies endpoint.
    """
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return MovieCreateSerializer
        return MovieListSerializer
