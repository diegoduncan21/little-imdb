from django.db import models

from model_utils.models import TimeStampedModel


class Alias(TimeStampedModel):
    """
    Persons AKA.
    """
    alias = models.CharField(max_length=50)

    def __str__(self):
        return self.alias


class Person(TimeStampedModel):
    """
    Represents an Actors, Directors, Producers.
    """
    MALE = "male"
    FEMALE = "female"

    GENDERS = (
        (MALE, "Male"),
        (FEMALE, "Female"),
    )

    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10,
                              choices=GENDERS,
                              blank=True,
                              null=True)
    aliases = models.ManyToManyField(Alias,
                                     related_name='persons',
                                     blank=True)

    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)


class Movie(TimeStampedModel):
    title = models.CharField(max_length=100)
    release_year = models.PositiveIntegerField(blank=True, null=True)
    castings = models.ManyToManyField(Person,
                                      related_name='movies_as_actor',
                                      blank=True)
    directors = models.ManyToManyField(Person,
                                       related_name='movies_as_director',
                                       blank=True)
    producers = models.ManyToManyField(Person,
                                       related_name='movies_as_producer',
                                       blank=True)

    def __str__(self):
        return "{}({})".format(self.title, self.release_year)

    def release_year_in_roman(self):
        ROMAN = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

        result = ""
        for (arabic, roman) in ROMAN:
            (factor, self.release_year) = divmod(self.release_year, arabic)
            result += roman * factor
        return result
