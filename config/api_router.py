from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from citysound.users.api.views import UserViewSet
from citysound.tours.api.views import TourViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)
router.register("tours", TourViewSet)


app_name = "api"
urlpatterns = router.urls
