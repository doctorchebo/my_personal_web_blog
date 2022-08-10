from django.urls import include, path
from rest_framework import routers
from blog import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('email/', include('emailing.urls')),
    path('authentication/', include('authentication.urls')),
]