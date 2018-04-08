from django.contrib import admin
from django.urls import include, path

from rest_framework import routers
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view


from core.views import MovieViewSet, PersonViewSet

router = routers.DefaultRouter()
router.register('persons', PersonViewSet)
router.register('movies', MovieViewSet)

schema_view = get_swagger_view(title='Little IMDb')
asd_view = get_schema_view(title='Pastebin API')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls)),
    path('docs/', schema_view),
    path('schema/', asd_view),
]
