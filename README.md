# Little IMDb project.

## Some endpoint queries:

### Persons:
* `/api/v1/persons/?last_name=Horowitz`
* `/api/v1/persons/?last_name__icontains=Horo`
* `/api/v1/persons/?gender=male`
* `/api/v1/persons/?aliases__alias=tarantinesco`
* `/api/v1/persons/?movies_as_actor__title__iexact=alien`
* `/api/v1/persons/?movies_as_actor__release_year=1990`


### Movies:
* `/api/v1/movies/?title__contains=pulp`
* `/api/v1/movies/?release_year=1990`
* `/api/v1/movies/?release_year=1990&title__iexact=alien`
* `/api/v1/movies/?castings__aliases__alias__icontains=Winona`
* `/api/v1/movies/?castings__gender=female`
