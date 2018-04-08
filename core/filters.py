from url_filter.filtersets import ModelFilterSet

from .models import Person, Movie


class PersonFilterSet(ModelFilterSet):
    class Meta(object):
        model = Person


class MovieFilterSet(ModelFilterSet):
    class Meta(object):
        model = Movie
