from rest_framework import serializers

from core.fields import CreatableSlugRelatedField
from core.models import Alias, Person, Movie


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
    aliases = CreatableSlugRelatedField(queryset=Alias.objects.all(),
                                        many=True,
                                        slug_field='alias')
    movies_as_actor = MovieAuxSerializer(many=True, read_only=True)
    movies_as_director = MovieAuxSerializer(many=True, read_only=True)
    movies_as_producer = MovieAuxSerializer(many=True, read_only=True)

    def create(self, validated_data):
        aliases = validated_data.pop('aliases')
        person = Person.objects.create(**validated_data)
        person.aliases.set(aliases)
        return person

    def update(self, instance, validated_data):
        aliases = validated_data.pop('aliases')
        instance.last_name = validated_data\
            .get('last_name', instance.last_name)
        instance.first_name = validated_data\
            .get('first_name', instance.first_name)
        instance.gender = validated_data\
            .get('gender', instance.gender)
        instance.aliases.set(aliases)
        instance.save()
        return instance

    class Meta:
        fields = [
            'id',
            'last_name',
            'first_name',
            'gender',
            'aliases',
            'movies_as_actor',
            'movies_as_director',
            'movies_as_producer',
        ]
        model = Person
