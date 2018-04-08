from rest_framework import serializers

from core.models import Alias, Person, Movie


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


class MovieListSerializer(serializers.HyperlinkedModelSerializer):
    castings = PersonAuxSerializer(many=True, read_only=True)
    directors = PersonAuxSerializer(many=True, read_only=True)
    producers = PersonAuxSerializer(many=True, read_only=True)

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


class MovieCreateSerializer(serializers.HyperlinkedModelSerializer):
    castings = serializers.PrimaryKeyRelatedField(
        queryset=Person.objects.all(),
        many=True)
    directors = serializers.PrimaryKeyRelatedField(
        queryset=Person.objects.all(),
        many=True)
    producers = serializers.PrimaryKeyRelatedField(
        queryset=Person.objects.all(),
        many=True)

    release_year = serializers.IntegerField()

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
