from django.contrib import admin

from .models import Alias, Movie, Person


class MovieAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'release_year',
        'modified',
        'created',
    ]
    list_filter = [
        'release_year'
    ]
    search_fields = [
        'title',
    ]


class PersonAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'last_name',
        'first_name',
        'gender',
        'modified',
        'created',
    ]
    list_filter = [
        'gender'
    ]
    search_fields = [
        'last_name',
        'first_name',
    ]


admin.site.register(Alias)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Person, PersonAdmin)
