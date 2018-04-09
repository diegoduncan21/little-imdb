# Little IMDb project.

## Some endpoint queries:

### Persons:
* `/api/v1/persons/?last_name=Horowitz`
* `/api/v1/persons/?last_name__icontains=Horo`
* `/api/v1/persons/?gender=male`
* `/api/v1/persons/?aliases__alias=tarantinesco`
* `/api/v1/persons/?movies_as_actor__title__icontains=alien`
* `/api/v1/persons/?movies_as_actor__release_year=1995`


### Movies:
* `/api/v1/movies/?title__icontains=pulp`
* `/api/v1/movies/?release_year=1997`
* `/api/v1/movies/?release_year=1995&title__icontains=brave`
* `/api/v1/movies/?castings__aliases__alias__icontains=Winona`
* `/api/v1/movies/?castings__gender=female`
