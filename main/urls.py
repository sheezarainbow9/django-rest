from rest_framework.routers import DefaultRouter
from .views import ConcessionariaViewset

app_name = 'api'

router = DefaultRouter(trailing_slash=False)
router.register(r'concessionaria', ConcessionariaViewset)

urlpatterns = router.urls
