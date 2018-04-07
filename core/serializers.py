from rest_framework import serializers

from .models import Alias, Person, Movie


class MovieAuxSerializer(serializers.HyperlinkedModelSerializer):
    """
    Auxiliar Movie serializer to avoid circular error.
    """

    release_year = serializers.SerializerMethodField('release_year_in_roman')

    def release_year_in_roman(self, obj):
        return obj.release_year_in_roman()

    class Meta:
        fields = [
            'id',
            'title',
            'release_year',
        ]
        model = Movie


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    aliases = serializers.SlugRelatedField(queryset=Alias.objects.all(),
                                           many=True,
                                           slug_field='alias')
    movies_as_actor = MovieAuxSerializer(many=True)
    movies_as_director = MovieAuxSerializer(many=True)
    movies_as_producer = MovieAuxSerializer(many=True)

    class Meta:
        fields = [
            'last_name',
            'first_name',
            'gender',
            'aliases',
            'movies_as_actor',
            'movies_as_director',
            'movies_as_producer',
        ]
        model = Person


class PersonAuxSerializer(serializers.HyperlinkedModelSerializer):
    """
    Auxiliar Person serializer to avoid circular error.
    """
    aliases = serializers.SlugRelatedField(queryset=Alias.objects.all(),
                                           many=True,
                                           slug_field='alias')

    class Meta:
        fields = [
            'id',
            'last_name',
            'first_name',
            'gender',
            'aliases',
        ]
        model = Person


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    castings = PersonAuxSerializer(many=True)
    directors = PersonAuxSerializer(many=True)
    producers = PersonAuxSerializer(many=True)

    release_year = serializers.SerializerMethodField('release_year_in_roman')

    def release_year_in_roman(self, obj):
        return obj.release_year_in_roman()

    class Meta:
        fields = [
            'id',
            'title',
            'release_year',
            'castings',
            'directors',
            'producers',
        ]
        model = Movie
