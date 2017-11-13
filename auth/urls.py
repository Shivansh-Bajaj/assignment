#from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

#from . import views as local_views
from rest_framework.authtoken import views as rest_framework_views

#from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from . import views

@permission_classes((IsAuthenticated))
def protected_serve(request, path, document_root=None, show_indexes=False):
    return serve(request, path, document_root, show_indexes)

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^upload/$', views.upload_img, name='upload'),
    url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], protected_serve, {'document_root': settings.MEDIA_ROOT}),    
    url(r'^get_auth_token/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),
    #url(r'^api-token-auth/', obtain__token),
    #url(r'^api-token-auth/', obtain_jwt_token),
    #url(r'^api-token-verify/', verify_jwt_token),
    url(r'^register', views.signup, name='register'),
]

#urlpatterns = [
    # Session Login
#    url(r'^login/$', local_views.get_auth_token, name='login'),
#    url(r'^logout/$', local_views.logout_user, name='logout'),
#    url(r'^auth/$', local_views.login_form, name='login_form'),
#    url(r'^upload/$', local_views.upload_img, name='upload'),
#    url(r'^get_auth_token/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),
#] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


