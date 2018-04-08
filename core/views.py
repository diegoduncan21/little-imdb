from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Movie, Person
from .serializers.movies import (
    MovieCreateSerializer,
    MovieListSerializer,
)
from .serializers.persons import PersonSerializer


from url_filter.filtersets import ModelFilterSet


class PersonFilterSet(ModelFilterSet):
    class Meta(object):
        model = Person


class PersonViewSet(viewsets.ModelViewSet):
    """
    Persons endpoint.
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get_queryset(self):
        fs = PersonFilterSet(data=self.request.GET, queryset=self.queryset)
        return fs.filter()


class MovieViewSet(viewsets.ModelViewSet):
    """
    Movies endpoint.
    """
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return MovieCreateSerializer
        return MovieListSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        instance = Movie.objects.get(id=serializer.data.get('id'))
        return Response(MovieListSerializer(instance).data,
                        status=status.HTTP_201_CREATED,
                        headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance,
                                         data=request.data,
                                         partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(MovieListSerializer(instance).data)
